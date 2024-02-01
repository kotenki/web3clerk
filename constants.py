user_states = {
    "default":          0,
    "add":              1,
    "add-token":        2,
    "add-token-price":  3,
    "delete":           4,
    "delete-id":        5
}


alert_states = {
    "inactive": 0,
    "active": 1
}

# add dictionary builder for supported_tokens from file
supported_tokens = {
"0X": "ZRX",
"1INCH": "1INCH",
"AAVE": "AAVE",
"AGORIC": "BLD",
"ALCHEMIX-USD": "ALUSD",
"ALGORAND": "ALGO",
"AMP-TOKEN": "AMP",
"ANKR": "ANKR",
"APECOIN": "APE",
"APENFT": "NFT",
"APTOS": "APT",
"ARWEAVE": "AR",
"AUDIUS": "AUDIO",
"AVALANCHE-2": "AVAX",
"AXELAR": "AXL",
"AXIE-INFINITY": "AXS",
"BABY-DOGE-COIN": "BABYDOGE",
"BALANCER": "BAL",
"BASIC-ATTENTION-TOKEN": "BAT",
"BINANCE-USD": "BUSD",
"BINANCECOIN": "BNB",
"BITCOIN": "BTC",
"BITCOIN-CASH": "BCH",
"BITCOIN-CASH-SV": "BSV",
"BITCOIN-GOLD": "BTG",
"BITDAO": "BIT",
"BITTORRENT": "BTT",
"BLOCKSTACK": "STX",
"CARDANO": "ADA",
"CASPER-NETWORK": "CSPR",
"CDAI": "CDAI",
"CELO": "CELO",
"CELSIUS-DEGREE-TOKEN": "CEL",
"CHAIN-2": "XCN",
"CHAINLINK": "LINK",
"CHIA": "XCH",
"CHILIZ": "CHZ",
"COIN-OF-THE-CHAMPIONS": "COC",
"COINMETRO": "XCM",
"COMPOUND-ETHER": "CETH",
"COMPOUND-GOVERNANCE-TOKEN": "COMP",
"COMPOUND-USD-COIN": "CUSDC",
"CONSTELLATION-LABS": "DAG",
"CONVEX-CRV": "CVXCRV",
"CONVEX-FINANCE": "CVX",
"COSMOS": "ATOM",
"CRYPTO-COM-CHAIN": "CRO",
"CURVE-DAO-TOKEN": "CRV",
"DAI": "DAI",
"DAO-MAKER": "DAO",
"DASH": "DASH",
"DECENTRALAND": "MANA",
"DECRED": "DCR",
"DEFICHAIN": "DFI",
"DIGIBYTE": "DGB",
"DOGECOIN": "DOGE",
"DOGELON-MARS": "ELON",
"ECASH": "XEC",
"ECOMI": "OMI",
"ELROND-ERD-2": "EGLD",
"ENERGY-WEB-TOKEN": "EWT",
"ENJINCOIN": "ENJ",
"EOS": "EOS",
"ERGO": "ERG",
"ESCOIN-TOKEN": "ELG",
"ETHEREUM": "ETH",
"ETHEREUM-CLASSIC": "ETC",
"ETHEREUM-NAME-SERVICE": "ENS",
"ETHOS": "VGX",
"EVMOS": "EVMOS",
"FANTOM": "FTM",
"FILECOIN": "FIL",
"FLOW": "FLOW",
"FORTA": "FORT",
"FRAX": "FRAX",
"FRAX-SHARE": "FXS",
"FTX-TOKEN": "FTT",
"GALA": "GALA",
"GATECHAIN-TOKEN": "GT",
"GEMINI-DOLLAR": "GUSD",
"GMX": "GMX",
"GNOSIS": "GNO",
"GOLEM": "GLM",
"HARMONY": "ONE",
"HAVVEN": "SNX",
"HEDERA-HASHGRAPH": "HBAR",
"HELIUM": "HNT",
"HIVE": "HIVE",
"HOLOTOKEN": "HOT",
"HUOBI-BTC": "HBTC",
"HUOBI-TOKEN": "HT",
"ICON": "ICX",
"IMMUTABLE-X": "IMX",
"INTERLAY": "INTR",
"INTERNET-COMPUTER": "ICP",
"IOSTOKEN": "IOST",
"IOTEX": "IOTX",
"JUNO-NETWORK": "JUNO",
"JUST": "JST",
"KADENA": "KDA",
"KAVA": "KAVA",
"KINTSUGI": "KINT",
"KLAY-TOKEN": "KLAY",
"KUCOIN-SHARES": "KCS",
"KUSAMA": "KSM",
"KYBER-NETWORK-CRYSTAL": "KNC",
"LEO-TOKEN": "LEO",
"LIDO-DAO": "LDO",
"LIQUITY-USD": "LUSD",
"LISK": "LSK",
"LITECOIN": "LTC",
"LIVEPEER": "LPT",
"LOOPRING": "LRC",
"MAGIC-INTERNET-MONEY": "MIM",
"MAIAR-DEX": "MEX",
"MAKER": "MKR",
"MATIC-NETWORK": "MATIC",
"MERIT-CIRCLE": "MC",
"MINA-PROTOCOL": "MINA",
"MONERO": "XMR",
"MOONBEAM": "GLMR",
"MSOL": "MSOL",
"MXC": "MXC",
"NEAR": "NEAR",
"NEM": "XEM",
"NEO": "NEO",
"NERVOS-NETWORK": "CKB",
"NEXO": "NEXO",
"NUCYPHER": "NU",
"NXM": "NXM",
"OASIS-NETWORK": "ROSE",
"OEC-TOKEN": "OKT",
"OKB": "OKB",
"OLYMPUS": "OHM",
"OMISEGO": "OMG",
"ONTOLOGY": "ONT",
"OPTIMISM": "OP",
"OSMOSIS": "OSMO",
"PANCAKESWAP-TOKEN": "CAKE",
"PAX-GOLD": "PAXG",
"PAXOS-STANDARD": "USDP",
"PLAYDAPP": "PLA",
"POCKET-NETWORK": "POKT",
"POLKADOT": "DOT",
"POLYMATH": "POLY",
"QTUM": "QTUM",
"QUANT-NETWORK": "QNT",
"RADIX": "XRD",
"RAVENCOIN": "RVN",
"RENDER-TOKEN": "RNDR",
"RESERVE-RIGHTS-TOKEN": "RSR",
"RIPPLE": "XRP",
"ROCKET-POOL": "RPL",
"SAFEMOON-2": "SFM",
"SECRET": "SCRT",
"SERUM": "SRM",
"SHIBA-INU": "SHIB",
"SIACOIN": "SC",
"SKALE": "SKL",
"SMOOTH-LOVE-POTION": "SLP",
"SOLANA": "SOL",
"SONGBIRD": "SGB",
"STAKED-ETHER": "STETH",
"STELLAR": "XLM",
"STEPN": "GMT",
"SUSHI": "SUSHI",
"SWEATCOIN": "SWEAT",
"SWIPE": "SXP",
"SYNAPSE-2": "SYN",
"TENSET": "10SET",
"TERRA-LUNA": "LUNC",
"TERRA-LUNA-2": "LUNA",
"TERRAUSD": "USTC",
"TETHER": "USDT",
"TETHER-EURT": "EURT",
"TETHER-GOLD": "XAUT",
"TEZOS": "XTZ",
"THE-GRAPH": "GRT",
"THE-OPEN-NETWORK": "TON",
"THE-SANDBOX": "SAND",
"THETA-FUEL": "TFUEL",
"THETA-TOKEN": "THETA",
"THORCHAIN": "RUNE",
"TOKENIZE-XCHANGE": "TKX",
"TRON": "TRX",
"TRUE-USD": "TUSD",
"TRUST-WALLET-TOKEN": "TWT",
"UMA": "UMA",
"UNISWAP": "UNI",
"USD-COIN": "USDC",
"USDD": "USDD",
"VECHAIN": "VET",
"VEGA-COIN": "VEGA",
"WAVES": "WAVES",
"WAX": "WAXP",
"WOO-NETWORK": "WOO",
"WRAPPED-BITCOIN": "WBTC",
"XDCE-CROWD-SALE": "XDC",
"YEARN-FINANCE": "YFI",
"ZCASH": "ZEC",
"ZEBEC-PROTOCOL": "ZBC",
"ZELCASH": "FLUX",
"ZENCASH": "ZEN",
"ZILLIQA": "ZIL",
"SUI": "SUI",
"JUPITER": "JUP"

}