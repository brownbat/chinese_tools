vowels = "aeiouüAEIOUÜ"
vowels_with_tones = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"

# vowels_with_tones.upper() = "ĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ"
# vowels_with_tones + vowels_with_tones.upper = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ"

#  NOTE: add apostrophe between syllables before a, e, and o ( http://pinyin.info/romanization/hanyu/apostrophes.html )

initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
finals = [
  "a", "o", "e", "ai", "ei", "ao", "ou", "an", "en", "ang", "eng", "er",  # Group a Finals
  "i", "ia", "io", "ie", "iai", "iao", "iu", "ian", "in", "iang", "ing",  # Group i Finals
  "u", "ua", "uo", "uai", "ui", "uan", "un", "uang", "ong",               # Group u Finals
  "ü", "üe", "üan", "ün", "iong",                                         # Group ü Finals
]

all_syllables = ["a", "ai", "an", "ang", "ao", "ba", "bai", "ban", "bang", "bao", "bei",
"ben", "beng", "bi", "bian", "biao", "bie", "bin", "bing", "bo", "bu",
"ca", "cai", "can", "cang", "cao", "ce", "cen", "ceng", "cha", "chai",
"chan", "chang", "chao", "che", "chen", "cheng", "chi", "chong", "chou",
"chu", "chua", "chuai", "chuan", "chuang", "chui", "chun", "chuo", "ci",
"cong", "cou", "cu", "cuan", "cui", "cun", "cuo", "da", "dai", "dan",
"dang", "dao", "de", "dei", "den", "deng", "di", "dia", "dian", "diao",
"die", "ding", "diu", "dong", "dou", "du", "duan", "dui", "dun", "duo",
"e", "ei", "en", "eng", "er", "fa", "fan", "fang", "fei", "fen", "feng",
"fo", "fou", "fu", "ga", "gai", "gan", "gang", "gao", "ge", "gei", "gen",
"geng", "gong", "gou", "gu", "gua", "guai", "guan", "guang", "gui",
"gun", "guo", "ha", "hai", "han", "hang", "hao", "he", "hei", "hen",
"heng", "hong", "hou", "hu", "hua", "huai", "huan", "huang", "hui",
"hun", "huo", "ji", "jia", "jian", "jiang", "jiao", "jie", "jin", "jing",
"jiong", "jiu", "ju", "juan", "jue", "jun", "ka", "kai", "kan", "kang",
"kao", "ke", "ken", "keng", "kong", "kou", "ku", "kua", "kuai", "kuan",
"kuang", "kui", "kun", "kuo", "la", "lai", "lan", "lang", "lao", "le",
"lei", "leng", "li", "lia", "lian", "liang", "liao", "lie", "lin",
"ling", "liu", "lo", "long", "lou", "lu", "luan", "lun", "luo", "lü",
"lüe", "ma", "mai", "man", "mang", "mao", "me", "mei", "men", "meng",
"mi", "mian"]

# TODO: add erhua final 'r' to all_syllables, then add optional tone accents, optional tone numbers
