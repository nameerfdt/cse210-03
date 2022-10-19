import random

class Word:
    # Word class for the parachute program.
    # The responsibility of Word is to generate a random word for the player to guess.

    # Word list for the single difficulty program containing words with 4 or 5 letters.
    word_list = ["AREA", "ABYSS", "BABY", "BALMY", "CASH", "CAPER", "DEAL", "DEBUT",
    "EDGE", "EDIFY", "FISH", "FEMUR", "GIRL", "GLOVE", "HELP", "HOVER", "IDEA", "IDIOT",
    "JACK", "JEWEL", "KIND", "KINGS", "LAND", "LEVER", "MISS", "MARRY", "NAME", "NINJA",
    "OVAL", "ORGAN", "POST", "PSALM", "QUIZ", "QUEST", "ROAD", "ROGUE", "SIZE", "SCENE",
    "TOUR", "TITHE", "USER", "URBAN", "VARY", "VIRUS", "WIFE", "WAGON", "XYST", "XENON",
    "YEAR", "YEAST", "ZEAL", "ZONES"]

    # Word list for the easy difficulty containing words with 3 or 4 letters.
    easy_list = ["AIR", "AIM", "BED", "BOY", "COB", "COW", "DAD", "DOG", "EGG", "END",
    "FOX", "FUN", "GUM", "GYM", "HEM", "HOT", "ICE", "ILL", "JAR", "JAM", "KID", "KIN",
    "LAW", "LAG", "MET", "MOB", "NOR", "NET", "OLD", "OUR", "PAW", "PIE", "QOU", "QUE",
    "RAT", "ROB", "SAT", "SEW", "TOE", "TUB", "USE", "UGH", "VAT", "VIE", "WAX", "WED",
    "YET", "YOU", "ZIP", "ZOO", "ACID", "AGED", "BATH", "BEAR", "COAT", "COPE", "DAWN",
    "DEBT", "EVIL", "EVER", "FELT", "FIRM", "GOLF", "GONE", "HARM", "HOLY", "IRON", "INCH",
    "JUST", "JURY", "KNEW", "KIND", "LAKE", "LADY", "MEAT", "MILK", "NOSE", "NINE", "OKAY",
    "OVER", "PASS", "PLAY", "QUIT", "QUAD", "RING", "RANK", "SAFE", "SIZE", "TWIN", "TUNE",
    "UPON", "USED", "VIEW", "VICE", "WARM", "WHOM", "XRAY", "XYST", "YEAH", "YEAR", "ZERO",
    "ZONE"]

    # Word list for the medium difficulty containing words with 5 letters.
    medium_list = ["ABOVE", "ACORN", "ADEPT", "AGAPE", "BAKER", "BANJO", "BACON", "BEVEL",
    "CALF", "CARAT", "CIDER", "CLEFS", "DEBTS", "DECAY", "DINKY", "DIRGE", "EDICT", "ELVES",
    "ELOPE", "EMBED", "FAUNA", "FARCE", "FATED", "FETCH", "GAUGE", "GENRE", "GRAPH", "GUILD",
    "HERBS", "HATED", "HIRED", "HEDGE", "ICONS", "INCUR", "ISSUE", "IDIOT", "JEWEL", "JOKES",
    "JUICY", "JUMPS", "KNIFE", "KNOWS", "KINGS", "KINDS", "LASER", "LEASE", "LEVER", "LUNAR",
    "MACRO", "METRO", "MICRO", "MYTHS", "NASAL", "NOTCH", "NOVEL", "NYLON", "OASIS", "OPTED",
    "OXIDE", "OUGHT", "PEACE", "PILOT", "PLANT", "PSALM", "QUOTE", "QUILT", "QUEUE", "QUERY",
    "RANCH", "RENAL", "RESIN", "RUGBY", "SATIN", "SCARY", "SIXTH", "SWEAR", "TEMPO", "TAXES",
    "THIEF", "TOKEN", "UNTIL", "USAGE", "ULTRA", "UNITE", "VAGUE", "VEGAN", "VOLTS", "VINYL",
    "WAGES", "WASTE", "WEIGH", "WELSH", "XANAX", "XENON", "XEROX", "XYLIC", "YEAST", "YOUTH",
    "YIELD", "YACHT", "ZONES", "ZEBUS", "ZAZZY"]

    # Word list for the hard difficulty containing words with 6 or 7 letters.
    hard_list = ["ADVICE", "ALMOST", "ASPECT", "ANSWER", "BACKED", "BEAUTY", "BEHALF",
    "BISHOP", "CASTLE", "CAUGHT", "COMBAT", "COURSE", "DANGER", "DEBATE", "DEPUTY", "DRIVEN",
    "EASILY", "EDITOR", "EMPIRE", "EXPAND", "FACTOR", "FINGER", "FRIEND", "FORMAT", "GUILTY",
    "GOLDEN", "GATHER", "GARDEN", "HANDLE", "HARDLY", "HEALTH", "HONEST", "IMPACT", "INJURY",
    "ISLAND", "ITSELF", "JUNIOR", "JERSEY", "JOSEPH", "JIGSAW", "KAHUNA", "KENNEL", "KELTER",
    "KNIGHT", "LAUNCH", "LINKED", "LUCENT", "LUXURY", "MARGIN", "MAINLY", "MOVING", "MOTHER",
    "NATION", "NATIVE", "NEARBY", "NIGHTS", "OBJECT", "OBTAIN", "ORIGIN", "ORANGE", "PARENT",
    "PLENTY", "POLICY", "PRISON", "QUAKES", "QUEAZY", "QUILTS", "QUARTZ", "RANDOM", "REGARD",
    "RETAIN", "RETURN", "SECTOR", "SHOULD", "SOUGHT", "SOVIET", "TARGET", "THROWN", "TOWARD",
    "TWELVE", "UNIQUE", "UPDATE", "USEFUL", "UNABLE", "VICTIM", "VISUAL", "VENDOR", "VARIED",
    "WALKER", "WEIGHT", "WONDER", "WRIGHT", "XANADU", "XENONS", "XYLOMA", "XYSTUS", "YACHTS",
    "YACKED", "YAGERS", "YAKUZA", "ZANILY", "ZARCOS", "ZAPPED", "ZANIER", "ABSCENCE", "ABILITY",
    "ANXIETY", "ANXIOUS", "BROTHER", "BESIDES", "BENEATH", "BEARING", "CALIBER", "CAUTION",
    "CHRONIC", "COMPLEX", "DESPITE", "DYNAMIC", "DISTANT", "DISEASE", "ECONOMY", "EXPENSE",
    "EXPLAIN", "EXCITED", "FACTORY", "FORTUNE", "FOREIGN", "FEATURE", "GENETIC", "GIGABIT",
    "GATEWAY", "GENERAL", "HEAVILY", "HISTORY", "HIMSELF", "HOWEVER", "IMAGING", "INITIAL",
    "INTENSE", "INVOLVE", "JOINTLY", "JOURNAL", "JUSTICE", "JOURNEY", "KILLING", "KEEPING",
    "KNOWING", "KITCHEN", "LEISURE", "LIBERTY", "LICENSE", "LISTING", "MAXIMUM", "MEASURE",
    "MENTION", "MIXTURE", "NERVOUS", "NUCLEAR", "NOWHERE", "NETWORK", "OPERATE", "OPTICAL",
    "OPENING", "ORGANIC", "PORTION", "PREMIER", "PRIVACY", "PROFILE", "QUALIFY", "QUARTER",
    "QUALITY", "QUAKILY", "ROUTINE", "RECEEIPT", "REALITY", "REALIZE", "SOCIETY", "SUBJECT",
    "SURVIVE", "SUSTAIN", "THEATRE", "TURNING", "THERAPY", "TENSION", "UNKNOWN", "UNUSUAL",
    "UPGRADE", "UNIFORM", "VARIETY", "VIOLENT", "VIRTUAL", "VEHICLE", "WESTERN", "WELFARE",
    "WHEREAS", "WELCOME", "XYLENOL", "XYLONIC", "XIPHOID", "XIBALBA", "YAHTZEE", "YAKUTSK",
    "YANKIES", "YAGGERS", "ZAMARRA", "ZAKUSKI", "ZABIANS", "ZAPATEO"]

    def __init__(self):
        pass

    def get_word(self): # Get a random word from the word list.
        # Get the length of the word list.
        length = len(self.word_list)

        # Generate a random number within range.
        index = (random.randrange(0, (length - 1)))

        # Get a word from the list using the random number.
        random_word = self.word_list[index]

        # Separate the random word into a list of letters.
        letter_list = list(random_word)

        # Return list of letters.
        return letter_list
