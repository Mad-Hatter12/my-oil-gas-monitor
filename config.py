"""Universe and site settings for the dashboard: Malaysia oil & gas.

Symbols are TradingView "EXCHANGE:TICKER" ids. Edit this file to add/remove names.
"""

# Site-level settings: everything sector-specific outside the lists below.
SITE = {
    "title": "Malaysia Oil & Gas Monitor",
    "short_title": "MY Oil & Gas",
    "description": "Bursa oil & gas stocks, regional energy indices, crude, gas, LNG, FX and newsflow.",
    "universe_label": "Bursa-listed upstream, services, FPSO, gas & downstream",
    # Default benchmark for every stock (a stock can override with "benchmark").
    "sector_index": "MYX:ENERGY",
    "sector_index_name": "Bursa Energy index",
    "sector_index_short": "Bursa Energy",
    "market_index": "FTSEMYX:FBMKLCI",
    "market_index_name": "FBM KLCI (market)",
    "regional_title": "Regional energy indices",
    "regional": [
        {"symbol": "MYX:ENERGY", "name": "Bursa Energy (MY)"},
        {"symbol": "SET:ENERG", "name": "SET Energy & Utilities (TH)"},
        {"symbol": "IDX:IDXENERGY", "name": "IDX Energy (ID)"},
    ],
    "commodity_groups": ["FX", "Crude", "Gas & LNG", "Products", "Coal"],
    # Extra words that make a sector headline Malaysia-relevant (on top of Malaysia/Bursa/ringgit/states).
    "local_keywords": r"Petronas|Petros|Malaysia Petroleum Management|MPM|RON95|Labuan|Bintulu|Kerteh",
    # The global market news card (fed by API_QUERIES).
    "supply_feed": {
        "title": "Global oil & gas market news",
        "sub": "OPEC+, crude, LNG and refining headlines",
        "label": "Global oil & gas",
        "tag": "Oil & gas markets",
        # A headline must match this to be kept.
        "keywords": r"oil|crude|Brent|WTI|OPEC\+?|LNG|natural gas|refin\w*|diesel|gasoline|jet fuel|"
                    r"barrels?|rigs?|drilling|upstream|downstream|petrochemicals?|shale",
    },
}

STOCKS = [
    # symbol, Bursa stock code, short, name, segment, news aliases (case-insensitive match in headlines)
    {"symbol": "MYX:DIALOG", "code": "7277", "short": "DIALOG", "name": "Dialog Group", "segment": "Midstream & services",
     "aliases": ["Dialog Group"]},
    {"symbol": "MYX:YINSON", "code": "7293", "short": "YINSON", "name": "Yinson Holdings", "segment": "FPSO",
     "aliases": ["Yinson"]},
    {"symbol": "MYX:ARMADA", "code": "5210", "short": "ARMADA", "name": "Bumi Armada", "segment": "FPSO",
     "aliases": ["Bumi Armada"]},
    {"symbol": "MYX:VELESTO", "code": "5243", "short": "VELESTO", "name": "Velesto Energy", "segment": "Drilling",
     "aliases": ["Velesto"]},
    {"symbol": "MYX:HIBISCS", "code": "5199", "short": "HIBISCS", "name": "Hibiscus Petroleum", "segment": "Upstream",
     "aliases": ["Hibiscus Petroleum"]},
    {"symbol": "MYX:DAYANG", "code": "5141", "short": "DAYANG", "name": "Dayang Enterprise", "segment": "O&G services",
     "aliases": ["Dayang Enterprise", "Dayang"]},
    {"symbol": "MYX:PENERGY", "code": "5133", "short": "PENERGY", "name": "Petra Energy", "segment": "O&G services",
     "aliases": ["Petra Energy"]},
    {"symbol": "MYX:WASCO", "code": "5142", "short": "WASCO", "name": "Wasco", "segment": "O&G services",
     "aliases": ["Wasco"]},
    {"symbol": "MYX:DELEUM", "code": "5132", "short": "DELEUM", "name": "Deleum", "segment": "O&G services",
     "aliases": ["Deleum"]},
    {"symbol": "MYX:UZMA", "code": "7250", "short": "UZMA", "name": "Uzma", "segment": "O&G services",
     "aliases": ["Uzma"]},
    {"symbol": "MYX:MISC", "code": "3816", "short": "MISC", "name": "MISC", "segment": "Shipping",
     "aliases": ["MISC Bhd", "MISC Berhad", "MISC Group"]},
    {"symbol": "MYX:PETGAS", "code": "6033", "short": "PETGAS", "name": "Petronas Gas", "segment": "Gas utility",
     "aliases": ["Petronas Gas", "PetGas"]},
    {"symbol": "MYX:GASMSIA", "code": "5209", "short": "GASMSIA", "name": "Gas Malaysia", "segment": "Gas utility",
     "aliases": ["Gas Malaysia"]},
    {"symbol": "MYX:PCHEM", "code": "5183", "short": "PCHEM", "name": "Petronas Chemicals", "segment": "Petrochemicals",
     "aliases": ["Petronas Chemicals", "PChem"]},
    {"symbol": "MYX:PETDAG", "code": "5681", "short": "PETDAG", "name": "Petronas Dagangan", "segment": "Downstream",
     "aliases": ["Petronas Dagangan", "PetDag"]},
    {"symbol": "MYX:PETRONM", "code": "3042", "short": "PETRONM", "name": "Petron Malaysia", "segment": "Downstream",
     "aliases": ["Petron Malaysia"]},
    {"symbol": "MYX:HENGYUAN", "code": "4324", "short": "HENGYUAN", "name": "Hengyuan Refining", "segment": "Downstream",
     "aliases": ["Hengyuan"]},
]

INDICES = [
    {"symbol": "MYX:ENERGY", "short": "Bursa Energy", "country": "MY"},
    {"symbol": "FTSEMYX:FBMKLCI", "short": "FBM KLCI", "country": "MY"},
    {"symbol": "SET:ENERG", "short": "SET Energy & Utilities", "country": "TH"},
    {"symbol": "IDX:IDXENERGY", "short": "IDX Energy", "country": "ID"},
]

# FX pairs: price = MYR per 1 unit of foreign currency (pair up = ringgit weaker).
# "synthetic" pairs have no direct TradingView listing and are computed as num / den.
# Add "fx": [...] to a stock above to show these on its company page.
COMMODITIES = [
    {"symbol": "FX_IDC:USDMYR", "short": "USD/MYR", "group": "FX",
     "drives": "Oil, gas and most charter, rig and FPSO contracts are priced in USD; a weaker ringgit lifts translated revenue."},
    {"symbol": "FX_IDC:SGDMYR", "short": "SGD/MYR", "group": "FX",
     "drives": "Singapore dollar against the ringgit."},
    {"symbol": "FX_IDC:CNYMYR", "short": "CNY/MYR", "group": "FX",
     "drives": "Chinese yuan against the ringgit."},
    {"symbol": "SYN:PLNMYR", "short": "PLN/MYR", "group": "FX",
     "synthetic": {"num": "FX_IDC:USDMYR", "den": "FX_IDC:USDPLN"},
     "drives": "Polish zloty against the ringgit. Computed as USD/MYR ÷ USD/PLN."},
    {"symbol": "ICEEUR:BRN1!", "short": "Brent", "group": "Crude",
     "drives": "Global crude benchmark: upstream revenue, Petronas spending and activity levels for services names."},
    {"symbol": "NYMEX:CL1!", "short": "WTI", "group": "Crude",
     "drives": "US crude benchmark; the Brent–WTI gap signals global supply balance."},
    {"symbol": "NYMEX:DCB1!", "short": "Dubai crude", "group": "Crude",
     "drives": "Asian sour-crude benchmark used to price Middle East barrels into Asian refineries."},
    {"symbol": "NYMEX:JKM1!", "short": "JKM LNG", "group": "Gas & LNG",
     "drives": "Asian spot LNG price: Malaysian LNG exports and LNG shipping demand."},
    {"symbol": "NYMEX:NG1!", "short": "Henry Hub", "group": "Gas & LNG",
     "drives": "US natural gas benchmark; sets the cost of US LNG exports competing in Asia."},
    {"symbol": "ICEENDEX:TFM1!", "short": "Dutch TTF", "group": "Gas & LNG",
     "drives": "European gas benchmark; competes with Asia for LNG cargoes."},
    {"symbol": "ICEEUR:ULS1!", "short": "Gasoil", "group": "Products",
     "drives": "Diesel/gasoil benchmark: refining margins for Hengyuan and Petron, and fuel costs for services and shipping."},
    {"symbol": "NYMEX:RB1!", "short": "RBOB gasoline", "group": "Products",
     "drives": "Gasoline benchmark: refining margins and pump-price pressure."},
    {"symbol": "NYMEX:HO1!", "short": "ULSD diesel", "group": "Products",
     "drives": "US diesel benchmark; with gasoline, a gauge of global refining cracks."},
    {"symbol": "ICEEUR:NCF1!", "short": "Newcastle coal", "group": "Coal",
     "drives": "Asian thermal coal benchmark: competes with gas in power generation."},
]

# Sector-level Google News queries (Malaysia edition), tagged as sector news.
SECTOR_QUERIES = [
    'Malaysia oil and gas stocks Bursa',
    'Petronas contract OR contracts OR award',
    'Petronas capex OR "activity outlook" OR spending',
    'Malaysia upstream "production sharing contract" OR PSC OR "marginal field"',
    'Sarawak Petros gas',
    'Malaysia Budget 2027 fuel subsidy OR RON95 OR diesel',
    'Malaysia LNG OR "gas tariff" OR "gas price"',
]

# Global oil & gas market news (not filtered to Malaysia), tagged with SITE["supply_feed"]["tag"].
API_QUERIES = [
    'OPEC+ output OR production OR quota',
    'oil prices Brent outlook',
    'LNG prices OR supply Asia',
    'Asia refining margins OR "crack spread"',
]

# Keyword tagging: (tag, regex). All matching tags are applied.
TAGS = [
    ("Earnings", r"\b(quarter|1Q|2Q|3Q|4Q|Q[1-4]|FY\d|net profit|earnings|revenue|EPS|results|dividend)\b"),
    ("Contract / award", r"\b(contracts?|awards?|awarded|LOA|letter of award|charter|tender|extension|"
                         r"work orders?|umbrella|PSC|RSC|EPCC|EPCIC|order ?book)\b"),
    ("M&A / corporate", r"\b(acqui|merger|takeover|privati|stake|IPO|listing|placement|rights issue|consolidation|SpA|disposal|bonus issue)\w*"),
    ("Policy / regulation", r"\b(government|ministry|minister|budget|subsid|RON95|tariff|regulat|policy|windfall|tax|BNM)\w*"),
    ("Analyst", r"\b(target price|TP|upgrade|downgrade|maintain|buy call|outperform|underperform|rating|analyst|research|stock picks?|market talk)\b"),
    ("Upstream / production", r"\b(production|output|barrels?|bpd|discover\w*|fields?|wells?|drilling|rigs?|FPSO|exploration|reserves)\b"),
    ("Management", r"\b(CEO|MD|managing director|chairman|resign|appoint|board)\b"),
    ("Commodity / prices", r"\b(Brent|crude|oil prices?|LNG|gas prices?|OPEC\+?|crack|refining margins?)\b"),
]
