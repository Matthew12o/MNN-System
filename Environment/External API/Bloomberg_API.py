import pdblp

class BloombergAPI:
    def __init__(self):
        self.Connection = pdblp.BCon(debug=True, port=8194, timeout=5000)
        self.Connection.start()
    
    def _bdh(self, universe, fields, options):
        ''' Data Point Request '''
        response_raw = self.Connection.bdh(universe, fields, options) # Placeholder
        response_clean = self._cleanReponse(response_raw, 0)
        return response_clean
    
    def _bds(self, universe, fields, options):
        ''' Data Set Request '''
        response_raw = self.Connection.ref(universe, fields, options) # Placeholder
        response_clean = self._cleanReponse(response_raw, 1)
        return response_clean
    
    def RequestData(self, universe, fields, options, request_type=0):
        if request_type == 0:
            blp_response = self._bdh(universe, fields, options)
        else:
            blp_response = self._bds(universe, fields, options)
        return blp_response
    
    def _cleanReponse(self, response, response_type):
        if response_type == 0:
            ## clean logic
            cleaned_data = 0 # Placeholder
        else: 
            ## clean logic
            cleaned_data = 0 # Placeholder
        return cleaned_data
    




