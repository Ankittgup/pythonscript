import pandas as pd
from alpha_vantage.timeseries import TimeSeries

class ScriptData:
    """Script Data class"""
    def __init__(self) -> None:
        self.ts_ob = TimeSeries("LNOYXG75DUBISWR7", output_format='pandas')
        self.data = dict()


    def fetch_intraday_data(self, symbol):
        self.data[symbol] = self.ts_ob.get_intraday(symbol=symbol, outputsize='full')

    def convert_intraday_data(self, symbol):
        if symbol in self.data:
            return self.data[symbol][0]
        else:
            return pd.DataFrame()

    def __contains__(self, symbol):
        return True if symbol in self.data else False





if __name__ == '__main__':
    ob = ScriptData()
    data = ob.fetch_intraday_data('GOOGL')
    df = ob.convert_intraday_data(data)
    print(df)