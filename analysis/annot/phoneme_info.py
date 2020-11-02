# multi valued (MV) feature system which uses traditional phonetic categories such as manner, place

# taken from this paper: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.66.8392&rep=rep1&type=pdf

feature_names_MV = ['phonation', 'manner', 'place', 'frontback', 'roundness',
                    'centrality']

# explanation of entries:

# phonation:
# v = voiced
# uv = unvoiced
# NOTE: all vowels are considered voiced

# manner:
# v = vowel
# o = obstruent
# f = fricative
# a = approximant
# n = nasal

# place:
# lo = low vowel
# m = mid vowel
# h = high vowel
# l = labial
# d = dental
# c = coronal
# g = glottal
# v = velar

# frontback:
# b = back
# f = front

# roundness
# u = unrounded
# r = rounded

# centrality
# c = central

# NOTE: 's' means silence and 'n' means it doesn't apply (i think)

phone_to_feature_MV = {
'aa': ['v', 'v', 'lo', 'b', 'u', 'c'],
'ae': ['v', 'v', 'lo', 'f', 'u', 'f'],
'ah': ['v', 'v', 'lo', 'f', 'u', 'f'],
'ao': ['v', 'v', 'm', 'b', 'r', 'f'],
'aw': ['v', 'v', 'm', 'b', 'r', 'f'],
'ax': ['v', 'v', 'm', 'n', 'u', 'c'],
'ax-h': ['v', 'v', 'm', 'n', 'u', 'c'],
'axr': ['v', 'v', 'm', 'n', 'u', 'c'],
'ay': ['v', 'v', 'm', 'f', 'u', 'f'],
'b': ['v', 'o', 'l', 'f', 'u', 'n'],
'bcl': ['uv', 'o', 'l', 'f', 'u', 'n'],
'ch': ['uv', 'f', 'c', 'f', 'u', 'n'],
'd': ['v', 'o', 'c', 'f', 'u', 'n'],
'dcl': ['uv', 'o', 'c', 'f', 'u', 'n'],
'dh': ['v', 'f', 'd', 'f', 'u', 'n'],
'dx': ['v', 'o', 'c', 'f', 'u', 'n'],
'eh': ['v', 'v', 'm', 'f', 'u', 'f'],
'el': ['v', 'a', 'c', 'f', 'u', 'f'],
'em': ['v', 'n', 'l', 'f', 'u', 'n'],
'en': ['v', 'n', 'c', 'f', 'u', 'n'],
'eng': ['v', 'n', 'v', 'b', 'u', 'n'],
'er': ['v', 'a', 'v', 'b', 'u', 'f'],
'ey': ['v', 'v', 'h', 'f', 'u', 'f'],
'f': ['uv', 'f', 'd', 'f', 'u', 'n'],
'g': ['v', 'o', 'v', 'b', 'u', 'n'],
'gcl': ['uv', 'o', 'v', 'b', 'u', 'n'],
'hh': ['uv', 'f', 'g', 'b', 'u', 'n'],
'hv': ['v', 'f', 'g', 'b', 'u', 'n'],
'ih': ['v', 'v', 'h', 'f', 'u', 'f'],
'ix': ['v', 'v', 'h', 'f', 'u', 'f'],
'iy': ['v', 'v', 'h', 'f', 'u', 'f'],
'jh': ['v', 'f', 'c', 'f', 'u', 'n'],
'k': ['uv', 'o', 'v', 'b', 'u', 'n'],
'kcl': ['uv', 'o', 'v', 'b', 'u', 'n'],
'l': ['v', 'a', 'c', 'f', 'u', 'n'],
'm': ['v', 'n', 'l', 'f', 'u', 'n'],
'n': ['v', 'n', 'c', 'f', 'u', 'n'],
'ng': ['v', 'n', 'v', 'b', 'u', 'n'],
'nx': ['v', 'n', 'c', 'f', 'u', 'n'],
'ow': ['v', 'v', 'h', 'b', 'r', 'f'],
'oy': ['v', 'v', 'h', 'b', 'r', 'f'],
'p': ['uv', 'o', 'l', 'f', 'u', 'n'],
'pcl': ['uv', 'o', 'l', 'f', 'u', 'n'],
'q': ['uv', 'o', 'g', 'b', 'u', 'n'],
'r': ['v', 'a', 'v', 'b', 'u', 'n'],
's': ['uv', 'f', 'c', 'f', 'u', 'n'],
'sh': ['uv', 'f', 'c', 'f', 'u', 'n'],
't': ['uv', 'o', 'c', 'f', 'u', 'n'],
'tcl': ['uv', 'o', 'c', 'f', 'u', 'n'],
'th': ['v', 'f', 'd', 'f', 'u', 'n'],
'uh': ['v', 'v', 'h', 'b', 'r', 'f'],
'uw': ['v', 'v', 'h', 'b', 'r', 'f'],
'ux': ['v', 'v', 'h', 'b', 'r', 'f'],
'v': ['v', 'f', 'd', 'f', 'u', 'n'],
'w': ['v', 'a', 'l', 'f', 'r', 'n'],
'y': ['v', 'a', 'v', 'b', 'u', 'n'],
'z': ['v', 'f', 'c', 'f', 'u', 'n'],
'zh': ['v', 'f', 'c', 'f', 'u', 'n'],
'sil': ['s', 's', 's', 's', 's', 's'],
'h#': ['s', 's', 's', 's', 's', 's'],
'epi': ['s', 's', 's', 's', 's', 's'],
'pau': ['s', 's', 's', 's', 's', 's']
}