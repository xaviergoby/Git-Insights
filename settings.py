import os

##### Primary proj working dir paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")

##### Map(pings) of Configuration & Representation Formats)
# Standardised conventions to abide by:
# Dataframe Column Names Representations
COL_NAMES_CMPLT = ["timestamp", "open", "high", "low", "close", "volume",
                   "close_time", "quote_av", "trades", "tb_base_av",
                   "tb_quote_av", "ignore"]

COL_NAMES_ABBVR = ["T", "O", "H", "L", "C", "V", "CT", "QV", "N", "TB", "TQ", "I"]

# Default column names of BIG, MID & SMALL standard format df formats
DEF_NUMIDX_CMPLT_DF_FORMAT_COLS = ["timestamp", "open", "high", "low", "close", "volume",
                                   "close_time", "quote_av", "trades", "tb_base_av",
                                   "tb_quote_av", "ignore"]

DEF_NUMIDX_OHLCV_DF_FORMAT_COLS = ["timestamp", "open", "high", "low", "close", "volume"]

DEF_COL_ABBRV_TITLE_MAP = {"T": "timestamp", "V": "volume", "CT": "close_time",
                          "QV": "quote_av", "N": "trades", "TB": "tb_base_av",
                          "TQ": "tb_quote_av", "I": "ignore"}
