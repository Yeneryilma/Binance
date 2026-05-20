import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "change-me")
    API_KEY = os.getenv("BINANCE_API_KEY", "")
    API_SECRET = os.getenv("BINANCE_API_SECRET", "")
    TRADING_MODE = os.getenv("TRADING_MODE", "paper")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "5000"))

    CONFIG = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'testnet': False,
        'interval': '5m',
        'interval_confirm': '15m',
        'min_candles': 300,
        'portfolio_usd': 500.0,
        'leverage': 5,
        'max_long': 8,
        'max_short': 8,
        'min_trade_usd': 5.0,

        'willr_window': 14,
        'willr_ob': -15,
        'willr_os': -85,

        'stoch_k': 14,
        'stoch_d': 3,
        'stoch_ob': 85,
        'stoch_os': 15,

        'rsi_span': 14,
        'rsi_ob': 65,
        'rsi_os': 35,

        'atr_span': 14,
        'atr_mult_initial_stop': 1.4,
        'trail_activation_mult': 1.2,
        'atr_mult_trail': 1.2,
        'atr_mult_take_profit': 10.0,

        'ema_fast': 50,
        'ema_slow': 200,
        'ema_htf_period':28,
        

        'vol_ma_period': 20,
        'vol_ratio_min': 1.2,

        'macd_fast': 12,
        'macd_slow': 26,
        'macd_signal': 9,

        'bb_period': 20,
        'bb_std': 2.0,

        'obv_ema_span': 20,

        'roc_period': 10,
        'roc_long_min_allowed': -5.0,
        'roc_short_max_allowed': 5.0,

        'atr_ma_period': 20,

        'use_rsi_filter': False,
        'use_ema_filter': False,
        'use_vol_filter': False,
        'use_htf_filter': False,
        'use_macd_filter': True,
        'use_bb_filter': False,
        'use_obv_filter': False,
        'use_roc_filter': False,
        'use_atr_trend_filter': False,
        'use_two_candle_confirm': False,
        'enable_reverse_exit': True,
        'enable_reverse_entry': True,

        'min_atr_pct': 0.003,
        'min_strength': 'Güçlü',
        'scan_interval_sec': 180,
        'request_delay': 0.2,
        'log_file': 'bot.log',
        'csv_file': 'closed_trades.csv',
        'trading_mode': TRADING_MODE,

        'symbols': ['BTCUSDT','ETHUSDT','RAVEUSDT','SOLUSDT','XAGUSDT',
    'DOGEUSDT','ZECUSDT','XRPUSDT','BLESSUSDT','HYPEUSDT',
    'ARIAUSDT','1000PEPEUSDT','MYXUSDT','BNBUSDT','ALPHAUSDT','ENJUSDT','TAOUSDT',
    'BARDUSDT','ADAUSDT','GIGGLEUSDT','ZAMAUSDT','PORT3USDT','AVAXUSDT',
    'ENAUSDT','PAXGUSDT','SUIUSDT','LINKUSDT','RIVERUSDT','CRCLUSDT','COAIUSDT',
    'DOTUSDT','WLDUSDT','NEARUSDT','UXLINKUSDT','SXPUSDT','APRUSDT',
    'AGIXUSDT','AAVEUSDT','TRUMPUSDT','TSLAUSDT','ASTERUSDT','WETUSDT','SIRENUSDT',
    'FARTCOINUSDT','ONUSDT','MEMEFIUSDT','LEVERUSDT','TRADOORUSDT',
    'PUMPUSDT','NEIROETHUSDT','BCHUSDT','A2ZUSDT','FILUSDT','FTMUSDT','WAVESUSDT',
    'XPLUSDT','LABUSDT','LTCUSDT','OMNIUSDT','YALAUSDT','AMBUSDT','BSWUSDT',
    'OCEANUSDT','VVVUSDT','1000SHIBUSDT','DASHUSDT','UNIUSDT','LDOUSDT',
    'STRAXUSDT','MONUSDT','PENGUUSDT','STOUSDT','RENUSDT','CRVUSDT',
    'UNFIUSDT','1000BONKUSDT','WLFIUSDT','FETUSDT','TRXUSDT','DGBUSDT','MSTRUSDT',
    'WIFUSDT','INXUSDT','AIOTUSDT','NEIROUSDT','APTUSDT',
    'ARBUSDT','PIPPINUSDT','AIAUSDT','CCUSDT','HIFIUSDT','BEATUSDT','BROCCOLI714USDT',
    'OMUSDT','INTCUSDT','VIRTUALUSDT','BRUSDT','AKEUSDT','OPUSDT','PLUMEUSDT',
    'CHESSUSDT','DUSDT','42USDT','SNTUSDT','MKRUSDT','TONUSDT','GALAUSDT','SIGNUSDT',
    'ALGOUSDT','ONDOUSDT','HOODUSDT','HEMIUSDT','EPTUSDT',
    'LITUSDT','ETCUSDT','XLMUSDT','HBARUSDT','TANSSIUSDT','SLERFUSDT',
    '4USDT','RENDERUSDT','BLZUSDT','XMRUSDT','PLAYUSDT','BUSDT','NIGHTUSDT',
    'TSTUSDT','BAKEUSDT','INUSDT','TREEUSDT',
    'CYSUSDT','BULLAUSDT','KITEUSDT','KOMAUSDT','OGUSDT','CAKEUSDT',
    'SKYAIUSDT','COINUSDT','PTBUSDT','MUSDT','USELESSUSDT',
    'PIXELUSDT','TRUUSDT','LOKAUSDT','ORDIUSDT','ONTUSDT','TIAUSDT',
    'FORMUSDT','0GUSDT','RDNTUSDT','COMPUSDT','AXSUSDT',
    'GUAUSDT','POWERUSDT','ZROUSDT','KEYUSDT','BIOUSDT','ICPUSDT','LIGHTUSDT',
    'SEIUSDT','REDUSDT','POLUSDT','TAKEUSDT','TRIAUSDT',
    'HUSDT','DRIFTUSDT','VOXELUSDT','INJUSDT','BROCCOLIF3BUSDT','BANUSDT',
    'BDXNUSDT','PNUTUSDT','ZENUSDT','IPUSDT','CHZUSDT','BOMEUSDT','MDTUSDT',
    'DUSKUSDT','MERLUSDT','PLTRUSDT','MUBARAKUSDT','FISUSDT','CUSDT',
    'BLURUSDT','ETHFIUSDT','KAITOUSDT','MAGMAUSDT','ATOMUSDT','TUTUSDT',
    'NVDAUSDT','HOLOUSDT','AMZNUSDT','1000FLOKIUSDT','SANDUSDT','PENDLEUSDT',
    'PUFFERUSDT','KLAYUSDT','RESOLVUSDT','JUPUSDT','COMMONUSDT',
    'STRKUSDT','PEOPLEUSDT','AVAAIUSDT','FIGHTUSDT','BANANAS31USDT',
    'FUNUSDT','AIOUSDT','SWARMSUSDT','REEFUSDT','SKATEUSDT',
    'ORDERUSDT','HIPPOUSDT','XNYUSDT','EIGENUSDT','PROMUSDT','JTOUSDT','JSTUSDT',
    'SOONUSDT','HOOKUSDT','SAHARAUSDT','DARUSDT','COLLECTUSDT','XANUSDT','SNXUSDT',
    'USDCUSDT','SUPERUSDT','STABLEUSDT','ONGUSDT','POLYXUSDT','XTZUSDT','ARCUSDT',
    'HUMAUSDT','PUMPBTCUSDT','SPXUSDT','FLOWUSDT','TURBOUSDT','EDUUSDT',
    'DEXEUSDT','MOODENGUSDT','ATUSDT','CUDISUSDT','XPINUSDT',
    'XPTUSDT','BASUSDT','FHEUSDT','HYPERUSDT','CTSIUSDT','WUSDT','ARUSDT',
    'EULUSDT','ARKMUSDT','BERAUSDT','MORPHOUSDT','LPTUSDT','GOOGLUSDT','COWUSDT',
    'XVGUSDT','YBUSDT','KERNELUSDT',]
    }

STRENGTH_ORDER = {'Normal': 1, 'Güçlü': 2, 'Çok Güçlü': 3}

