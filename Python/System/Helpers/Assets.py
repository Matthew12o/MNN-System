import datetime as dt
import pandas as pd
import enum

## 

def getTimeElapsed(reference_1, reference_2=None):
    return dt.datetime.now() - reference_1 if reference_2 is None else reference_2 - reference_1

class AccountingType(enum.Enum):
    FIFO = 0
    LIFO = 1

## 
class Price:
    def __init__(self, identifier, time, bid=None, ask=None, mid=None, last=None):
        self.ID = identifier
        self.Time = time
        self.Bid = bid
        self.Ask = ask
        self.Last = last
        if mid is None and not bid is None and not ask is None:
            self.mid = (bid + ask)/2

class Position:
    def __init__(self, security):
        self.Security = security
        self.Quantity=0
        self.CostBasis=0
    
    def isLong(self):
        return True if self.Quantity >= 0 else False
    
    def getPositionValue(self):
        return self.Quanity * self.CostBasis

    def updatePosition(self, last_trade):
        d_quantity = last_trade.Quantity if last_trade.isLong else -last_trade.Quantity
        d_value = last_trade.Value if last_trade.isLong else -last_trade.Value
        cur_value = self.getPositionValue()
        self.Quantity += d_quantity
        self.CostBasis += (cur_value + d_value) / d_quantity

class Security:
    def __init__(self, identifier, accounting_type=AccountingType.FIFO):
        self.ID = identifier
        self.Prices = pd.DataFrame(data={'Time' : [], 'Ask' :[], 'Bid':[], 'Mid':[], 'Last':[]}).set_index(keys='Time')
        self.Position = Position(self)
        self.Trades = []
        self.ActiveTrades = []
        self.ClosedTrades = []
    
    def postNewTrade(self, trade):
        self.Trades.append(trade)
        self._netTrades()

    def _netTrades(self):
        last_trade = self.Trades[-1]
        for trade in self.ActiveTrades:
            if trade.isLong != last_trade.isLong:
                if trade.Quantity == last_trade.Quantity:
                    self._closeTrade(trade)
                    self._closeTrade(last_trade)
                elif trade.Quantity > last_trade.Quanity:
                    t_1, t_2 = self._getSeparatedTrades(trade, last_trade.Quantity)
                    self._closeTrade(t_1)
                    self._closeTrade(trade)
                    self.ActiveTrades.append(t_2)
                else:
                    t_1, t_2 = self._getSeparatedTrades(last_trade, trade.Quantity)
                    self._closeTrade(t_1)
                    self._closeTrade(trade)
                    self.ActiveTrades.append(t_2)
                    
    def _closeTrade(self, trade):
        trade.isClosed = True
        self.ClosedTrades.append(trade)

    def _getSeparatedTrades(self, trade, break_quantity):
        self.Trades.remove(trade)
        if trade.Quantity > break_quantity:
            # Create two trades from a single trade
            trade_1 = Trade(
                identifier='{}_1'.format(trade.ID), 
                side=trade.Side, 
                quantity=break_quantity, 
                cost_basis=trade.CostBasis, 
                time=trade.Time
                )
            trade_2 = Trade(
                identifier='{}_2'.format(trade.ID), 
                side=trade.Side, 
                quantity=trade.Quantity-break_quantity, 
                cost_basis=trade.CostBasis, 
                time=trade.Time
                )
            # Mark trades as partial trade
            trade_1.isPartial = True
            trade_2.isPartial = True
        return trade_1, trade_2

    def requestPrice(self):
        # contact API and request for price
        new_price = 0 # Placeholder 

        # check if valid
        if new_price.ID == self.ID:
            # last updated time
            self._convertToDataFrame(new_price)
        
    def _convertToDataFrame(self, price):
        p = pd.DataFrame({'Time':[price.Time], 'Ask':[price.Ask], 'Bid':[price.Bid], 'Mid':[price.Mid], 'Last':[price.Last]}).set_index(keys='Time')
        self.Prices.append(p, ignore_index=False)

    def getPrice(self):
        last_price_info = self.Prices.iloc[-1]
        time_elapsed = getTimeElapsed(last_price_info.index)
        return last_price_info, time_elapsed

class Trade:
    def __init__(self, identifier, side, quantity, cost_basis, time):
        self.ID = identifier
        self.Side = side
        self.isLong = True if side[0].upper() == 'B' else False
        self.Quantity = quantity
        self.CostBasis = cost_basis
        self.Time = time
        self.Value = self.Quantity * self.CostBasis
        self.isClosed = False
        self.isPartial = False
    
class Strategy:
    def __init__(self, description):
        self.Description = description
        self.Securities = []

    def addSecurity(self, security):
        self.Securities.append(security)
