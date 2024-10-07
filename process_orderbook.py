import numpy as np
import pandas as pd
import json
import os

class orderbook():
    bids = {}
    asks = {}

    max_bid = -1
    min_ask = np.inf

    def __init__(self, path):
        for date in sorted(os.listdir(path)):
            with open(f"historical_orderbook/{perp}/{date}") as file:
                for line in file:
                    try:
                        json_data = json.loads(line)
                    except json.JSONDecodeError:
                        print("Invalid JSON encountered and skipped.")
                        continue
                    
                    if json_data["type"] == "snapshot" and pd.to_datetime(date := date[:-5]) not in self.bids:
                        snapshot = json_data["data"]
                        date = pd.to_datetime(date)
                        self.bids[date] = {}
                        self.asks[date] = {}
                        for bid in snapshot["b"]:
                            self.bids[date][bid_p := float(bid[0])] = float(bid[1])
                            self.max_bid = max(self.max_bid, bid_p)
                        for ask in snapshot["a"]:
                            self.asks[date][ask_p := float(ask[0])] = float(ask[1])
                            
                            self.min_ask = min(self.min_ask, ask_p)
                    elif json_data["type"] == "delta":
                        pass

                    print(self.bids)
                    # print(json_data)
                    raise KeyboardInterrupt



    def make_bid(self, bid):
        pass 

    def make_ask(self, ask):
        pass

    def calc_spread(self):
        return None


if __name__ == "__main__":
    for perp in os.listdir("historical_orderbook/"):
        book = orderbook(f"historical_orderbook/{perp}")
        