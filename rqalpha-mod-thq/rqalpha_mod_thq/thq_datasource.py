import datetime

from rqalpha.data.base_data_source import BaseDataSource
import pandas as pd
from rqalpha.model.instrument import Instrument
from rqalpha.model.tick import TickObject


class THQDataSource(BaseDataSource):
    def __init__(self, path, custom_future_info):
        super(THQDataSource, self).__init__(path, custom_future_info)
        self._tickDF = pd.read_csv("E:\\BaiduNetdiskDownload\\storage\\000651.XSHE.csv")
        self._ins = Instrument({"order_book_id": "000651.XSHE", "symbol": "格力电器", "round_lot": 100, "type": "CS"})

    def get_merge_ticks(self, order_book_id_list, trading_date, last_dt=None):
        if last_dt is not None:
            raise NotImplementedError()
        if not "000651.XSHE" in order_book_id_list:
            raise NotImplementedError()
        df = self._tickDF.loc[(self._tickDF["day"] == trading_date.__format__('%Y-%m-%d'))]
        result = []
        year = trading_date.__getattribute__('year')
        month = trading_date.__getattribute__('month')
        day = trading_date.__getattribute__('day')
        for i in range(len(df)):
            row = df.iloc[i]
            dt = datetime.datetime(year, month, day, row["hour"], row["minute"], ["second"], 0)
            asks = row.loc[["a1_p", "a2_p", "a3_p", "a4_p", "a5_p"]].to_list()
            ask_vols = row.loc[["a1_v", "a2_v", "a3_v", "a4_v", "a5_v"]].to_list()
            bids = row.loc[["b1_p", "b2_p", "b3_p", "b4_p", "b5_p"]].to_list()
            bid_vols = row.loc[["b1_v", "b2_v", "b3_v", "b4_v", "b5_v"]].to_list()
            dic = {
                'datetime': dt,
                'open': 0.0,
                'last': row["current"],
                'high': row["high"],
                'low': row["low"],
                'prev_close': 0.0,
                'volume': row["volume"],
                'total_turnover': row["money"],
                'asks': asks,
                'ask_vols': ask_vols,
                'bids': bids,
                'bid_vols': bid_vols
            }
            result.append(TickObject(self._ins, dic))
        return result

    def available_data_range(self, frequency):
        return datetime.date(2020, 10, 9), datetime.date(2021, 3, 3)
