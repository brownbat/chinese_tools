'''resources
https://en.wikibooks.org/wiki/Chinese_(Mandarin)/Table_of_Initial-Final_Combinations
'''

# OVERALL GOAL
# Wordlist to Anki deck
# Convert a wordlist (say, HSK) to a csv containing:
#   simplified/traditional, accented pinyin, CEDICT definition
#   (optionally name of wordlist and some kind of index)

# Secondary goals
#   validate and manipulate pinyin strings between accented and unaccented

# note TOCFL wordlists: https://www.tw.org/tocfl/index.html
# chinese SAT?


# just load the whole dictionary to memory
cedict = {}
location = ".//cedict_1_0_ts_utf-8_mdbg.txt"
with open(location, "rt") as cedict_file:
    for l in cedict_file.readlines():
        if l[0] == "#":
            pass
        else:
            trad_simp, pinyin_definition = l.split("[", 1)
            assert len(trad_simp.split()) == 2
            trad, simp = trad_simp.split()
            pinyin, definition = pinyin_definition.split("]", 1)
            definition = definition[2:-2]
            definition = definition.replace('|', '/')
            entry = [trad, simp, pinyin, definition]
            if trad not in cedict:
                cedict[trad] = entry
            else:
                if cedict[trad][1] != simp:
                    cedict[trad][1] += f"; {simp}"
                if pinyin not in cedict[trad][2]:
                    cedict[trad][2] += f"; {pinyin}"
                if definition not in cedict[trad][3]:
                    cedict[trad][3] += f"; {definition}"
            if simp not in cedict:
                cedict[simp] = entry


# wordlist to bsv scratchpad - values separated by |
cases = """倒
安靜
安排
爸爸""".split()

for c in cases:
    trad, simp, pinyin, definition = cedict[c]
    if trad != simp:
        print(f"{simp} ({trad})|{pinyin}|{definition}")
    else:
        print(f"{trad}|{pinyin}|{definition}")

""" # restore if accent_pinyin_syllables() fixed
    if trad != simp:
        print(f"{simp} ({trad})|{accent_pinyin_syllables(pinyin)}|{definition}")
    else:
        print(f"{trad}|{accent_pinyin_syllables(pinyin)}|{definition}")
"""


# Pinyin validation and manipulation

tests = [
    # VALID
    "bā",  # simple accented syllable
    "nǚ",  # with umlaut
    "fēngjì",  # two accented syllables without space
    "ma",  # unaccented (fifth tone accented pinyin)
    "bāba",  # accented and unaccented compound syllables
    "bā ba",  # with space
    "ni3",  # simple numbered syllable
    "feng1 li4",  # two numbered syllables with space
    "feng1li4",  # two numbered syllables without space
    "Ni3",  # initial cap
    "Bā",  # initial cap accented
    "Ma",  # initial cap unaccented
    "Tiān'ānmén",  # with apostrophe before vowel, initial capital
    "fēng​lì",  # two accented syllables with zero width space
    "Tiān​'ān​mén",  # zero width space then apostrophe
    "āiya!",  # accented compound with trailing legit punctuation
    "Āiya!",  # accented compound with trailing legit punctuation
    "NǙ",  # all caps
    "shuangr",  # erhua
    "shuangr3",  # numbered erhua and longest possible valid pinyin syllable
    "shuang3 r5",  # mdbg style numbered erhua

    # INVALID
    "fēng1",  # both accented and numbered INVALID
    "xmnma ",  # leading junk characters
    "Tiān'​ān​mén",  # zero width space AFTER apostrophe
    "hello",  # english word that coincidentally starts with valid pinyin chr
    "!ma",  # leading junk punctuation
    "ma-",  # trailing junk punctuation
    "ma ",  # trailing space
    " ma",  # leading space
    "​mén",  # leading zero width space
    " ma ",  # leading and trailing space
    "shuang9",  # bad number
    "shuang0",  # bad number 0
    "shuangr9",  # bad number erhua
    "shuangr0",  # bad number 0 erhua
    "ma13",  # additional digit unexpectedly follows legitimate pinyin number
    "'ānmén",  # starting with apostrophe (mostly invalid, mid-processing ok?)
    "nǙ",  # weird caps
]


valid_pinyin_syllables = [
    "a", "ai", "an", "ang", "ao", "ba", "bai", "ban", "bang", "bao", "bei",
    "ben", "beng", "bi", "bian", "biao", "bie", "bin", "bing", "bo", "bu",
    "ca", "cai", "can", "cang", "cao", "ce", "cen", "ceng", "cha", "chai",
    "chan", "chang", "chao", "che", "chen", "cheng", "chi", "chong", "chou",
    "chu", "chua", "chuai", "chuan", "chuang", "chui", "chun", "chuo", "ci",
    "cong", "cou", "cu", "cuan", "cui", "cun", "cuo", "da", "dai", "dan",
    "dang", "dao", "de", "dei", "den", "deng", "di", "dia", "dian", "diao",
    "die", "ding", "diu", "dong", "dou", "du", "duan", "dui", "dun", "duo",
    "e", "ei", "en", "eng", "er", "fa", "fan", "fang", "fei", "fen", "feng",
    "fo", "fou", "fu", "ga", "gai", "gan", "gang", "gao", "ge", "gei", "gen",
    "geng", "gong", "gou", "gu", "gua", "guai", "guan", "guang", "gui", "gun",
    "guo", "ha", "hai", "han", "hang", "hao", "he", "hei", "hen", "heng",
    "hong", "hou", "hu", "hua", "huai", "huan", "huang", "hui", "hun", "huo",
    "ji", "jia", "jian", "jiang", "jiao", "jie", "jin", "jing", "jiong", "jiu",
    "ju", "juan", "jue", "jun", "ka", "kai", "kan", "kang", "kao", "ke", "ken",
    "keng", "kong", "kou", "ku", "kua", "kuai", "kuan", "kuang", "kui", "kun",
    "kuo", "la", "lai", "lan", "lang", "lao", "le", "lei", "leng", "li", "lia",
    "lian", "liang", "liao", "lie", "lin", "ling", "liu", "lo", "long", "lou",
    "lu", "luan", "lun", "luo", "lü", "lüe", "ma", "mai", "man", "mang", "mao",
    "me", "mei", "men", "meng", "mi", "mian", "miao", "mie", "min", "ming",
    "miu", "mo", "mou", "mu", "na", "nai", "nan", "nang", "nao", "ne", "nei",
    "nen", "neng", "ni", "nian", "niang", "niao", "nie", "nin", "ning", "niu",
    "nong", "nou", "nu", "nuan", "nun", "nuo", "nü", "nüe", "o", "ou", "pa",
    "pai", "pan", "pang", "pao", "pei", "pen", "peng", "pi", "pian", "piao",
    "pie", "pin", "ping", "po", "pou", "pu", "qi", "qia", "qian", "qiang",
    "qiao", "qie", "qin", "qing", "qiong", "qiu", "qu", "quan", "que", "qun",
    "ran", "rang", "rao", "re", "ren", "reng", "ri", "rong", "rou", "ru",
    "ruan", "rui", "run", "ruo", "sa", "sai", "san", "sang", "sao", "se",
    "sen", "seng", "sha", "shai", "shan", "shang", "shao", "she", "shen",
    "sheng", "shi", "shou", "shu", "shua", "shuai", "shuan", "shuang", "shui",
    "shun", "shuo", "si", "song", "sou", "su", "suan", "sui", "sun", "suo",
    "ta", "tai", "tan", "tang", "tao", "te", "teng", "ti", "tian", "tiao",
    "tie", "ting", "tong", "tou", "tu", "tuan", "tui", "tun", "tuo", "wa",
    "wai", "wan", "wang", "wei", "wen", "weng", "wo", "wu", "xi", "xia",
    "xian", "xiang", "xiao", "xie", "xin", "xing", "xiong", "xiu", "xu",
    "xuan", "xue", "xun", "ya", "yan", "yang", "yao", "ye", "yi", "yin",
    "ying", "yo", "yong", "you", "yu", "yuan", "yue", "yun", "za", "zai",
    "zan", "zang", "zao", "ze", "zei", "zen", "zeng", "zha", "zhai", "zhan",
    "zhang", "zhao", "zhe", "zhei", "zhen", "zheng", "zhi", "zhong", "zhou",
    "zhu", "zhua", "zhuai", "zhuan", "zhuang", "zhui", "zhun", "zhuo", "zi",
    "zong", "zou", "zu", "zuan", "zui", "zun", "zuo", "r"
]
# r not always considered valid pinyin but "r5" often used in cedict for erhua

vowels_with_tones = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
tones_upper = "ĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ"
# traditionally pinyin uses the aeoiu order

initials = [
    "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh",
    "ch", "sh", "r", "z", "c", "s", "y"
    # y is not a traditional initial but helpful for text processing b/c it is
    # used in place of i at the beginning of syllables
    ]

finals = [
    # Group a Finals
    "a", "o", "e", "ai", "ei", "ao", "ou", "an", "en", "ang", "eng", "er",
    # Group i Finals
    "i", "ia", "io", "ie", "iai", "iao", "iu", "ian", "in", "iang", "ing",
    # Group u Finals
    "u", "ua", "uo", "uai", "ui", "uan", "un", "uang", "ong",
    # Group ü Finals
    "ü", "üe", "üan", "ün", "iong", "ue"
    # ue is not a traditional final but used in place of üe after j,q,x,y
]


def is_valid_numbered_pinyin_syllable(syl, allow_erhua=True):
    """
    Determines if syl is a valid numbered pinyin syllable

    TODO: retest
    """
    valid = False
    if (syl[:-1].lower() in valid_pinyin_syllables) and (
            syl[-1] in "12345"):
        valid = True
    if allow_erhua:
        if (syl[:-2].lower() in valid_pinyin_syllables) and (
                syl[-2].lower() == "r" and syl[-1] in "12345"):
            valid = True
    return valid


def last_vowel_idx(syl):
    for idx in range(len(syl)-1, -1, -1):
        if syl[idx] in "aeiouü" + vowels_with_tones:
            return idx
    return None


def is_valid_toneless_pinyin_syllable(syl, allow_erhua=True):
    if allow_erhua and syl[-1] == "r":
        stripped_syl = syl[:-1]
    else:
        stripped_syl = syl
    numbered_syl = stripped_syl + "1"
    return is_valid_numbered_pinyin_syllable(numbered_syl)


def is_valid_accented_pinyin_syllable(syl, allow_erhua=True):
    """
    Determines whether syl is a valid accented pinyin syllable
    """
    # lowercase
    test_syl = syl.lower()
    # remove accent
    accented_letters = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    unaccent = dict(zip(accented_letters, "aaaaeeeeiiiioooouuuuüüüü"))

    tone_idx = None
    accented_letter = None
    for idx, l in enumerate(test_syl):
        if l in accented_letters:
            tone_idx = idx
            accented_letter = l
            break
    if accented_letter is not None:
        test_syl = test_syl.replace(accented_letter,
                                    unaccent[accented_letter],
                                    1)

    # check valid syllable
    letters_valid = is_valid_toneless_pinyin_syllable(test_syl, allow_erhua)

    # check accent on right letter, if exists
    # tone on a, e, o in ou, then final vowel
    if "a" in test_syl:
        proper_tone_idx = test_syl.find("a")
    elif "e" in test_syl:
        proper_tone_idx = test_syl.find("e")
    elif "ou" in test_syl:
        proper_tone_idx = test_syl.find("o")
    else:
        proper_tone_idx = last_vowel_idx(test_syl)

    tone_valid = (tone_idx is None) or (tone_idx == proper_tone_idx)

    return letters_valid and tone_valid


def is_valid_pinyin_syllable(syl):
    return (is_valid_accented_pinyin_syllable(syl)
            or is_valid_numbered_pinyin_syllable(syl))


def first_pinyin_syllable_length(pinyin_string):
    """
    Identifies the length of the first complete pinyin syllable

    Returns None if issues.
    shuangr3 longest?
    """
    longest_possible = min(8, len(pinyin_string))
    for idx in range(longest_possible, 0, -1):
        if is_valid_pinyin_syllable(pinyin_string[:idx]):
            return idx
    return None


def first_pinyin_syllable(pinyin_string):
    syl_len = first_pinyin_syllable_length(pinyin_string)
    if syl_len is None:
        return None
    else:
        return pinyin_string[:syl_len]

def find_first_pinyin(pinyin_string):
    for start_idx in range(len(pinyin_string)):
        test_syl = first_pinyin_syllable(pinyin_string[start_idx:])
        if test_syl is None:
            pass
        else:
            return test_syl
    return None
    

def strip_pinyin(syl):
    """
    Remove tone, remove punctuation, lowercase

    TODO: Currently just grabs first syllable, do for full stream
    """
    test_syl = syl.lower()
    tone_vowels = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    vowels_mask = "aaaaeeeeiiiioooouuuuüüüü"
    out_syl = ""
    for l in test_syl:
        if l in "abcdefghijklmnopqrstuüvwxyz ":
            out_syl += l
        elif l in tone_vowels:
            out_syl += vowels_mask[tone_vowels.find(l)]
    out_str = ""
    for idx in range(len(out_syl)):
        tmp_len = first_pinyin_syllable_length(out_syl[idx:])
        if tmp_len is not None:
            return(out_syl[idx:idx+tmp_len])
            # this only does one syllable            
    return out_syl


def proper_tone_idx(syl):
    # finds the index of where the accent mark goes
    # note if strip_pinyin ever strips a, e, ou - it could cause a subtle bug
    # this would be more stable if it clearly identified how much was stripped
    # and indexed from there
    test_syl = strip_pinyin(syl)
    if "a" in test_syl:
        proper_tone_idx = syl.find("a")
    elif "e" in test_syl:
        proper_tone_idx = syl.find("e")
    elif "ou" in test_syl:
        proper_tone_idx = syl.find("o")
    else:
        proper_tone_idx = last_vowel_idx(test_syl)
    return proper_tone_idx


def numbered_to_marked(syl):
    # TODO lookup marked letter in vowels_with_tones
    # currently failing to even find all valid numbered pinyin syllables?
    # probably b/c that replies false if multiple syllables
    # TODO test
    retval = None

    tone_dictionary = {"a":"āáǎàa",
                       "e":"ēéěèe",
                       "i":"īíǐìi",
                       "o":"ōóǒòo",
                       "u":"ūúǔùu",
                       "ü":"ǖǘǚǜü"}
    if is_valid_numbered_pinyin_syllable(syl):
        if syl == "r5":
            retval = "r"
        else:
            tone = int(syl[-1])-1
            pti = proper_tone_idx(syl)
            tone_letter = syl[pti]
            if tone == 5:
                accented_letter = tone_letter
            else:
                accented_letter = tone_dictionary[tone_letter][tone]
            retval = syl.replace(tone_letter, accented_letter)[:-1]
    return retval


def mdbg_to_marked(mdbg_pinyin, remove_spaces=True):
    # TODO fails on feng1li4 b/c no space between feng1 and li4
    # mdbg adds spaces between pinyin syllables though so is this ok?
    mdbg_syls = mdbg_pinyin.split()
    outstr = ""
    for syl in mdbg_syls:
        if is_valid_numbered_pinyin_syllable(syl):
            outstr += numbered_to_marked(syl)
        else:
            outstr += syl
        if not remove_spaces:
            outstr += " "
    return outstr


test_function = mdbg_to_marked
print(f"\nTesting {test_function.__name__}()")
for t in tests:
    print(f"{t}: {test_function(t)}")
exit()


"""
MODEL TO IMPLEMENT:

1. split string into first pinyin + tail, or junk leading chars + tail

is_valid_numbered_pinyin_string
# should we ignore whitespace, punctuation, caps?
# implement strict first
is_valid_accented_pinyin_string
is_valid_pinyin_string


split_pinyin_syllables
# split out nonpinyin letters into separate clusters?
# strip them?
# fail early
combine_pinyin_syllables
# add apostrophes appropriately

string:
 numbered_to_accent
 accent_to_numbered
 (preserve whitespace, preserve caps, preserve punctuation,
    preserve non-pinyin syllables?)
"""

