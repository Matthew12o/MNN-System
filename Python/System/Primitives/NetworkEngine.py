class NetworkEngine:
    def parseNetworkData(self, file_path):
        with open(file_path, 'r') as network:
            for i, value in network:
                i 