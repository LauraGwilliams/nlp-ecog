# Penn Part of Speech Tags

# for more info: https://www.clips.uantwerpen.be/pages/mbsp-tags

# Note:  these are the 'modified' tags used for Penn tree banking; these are the tags used in the Jet system. NP, NPS, PP, and PP$ from the original Penn part-of-speech tagging were changed to NNP, NNPS, PRP, and PRP$ to avoid clashes with standard syntactic categories.
# 	1.	CC--	Coordinating conjunction
# 	2.	CD--	Cardinal number
# 	3.	DT--	Determiner
# 	4.	EX--	Existential there
# 	5.	FW--	Foreign word
# 	6.	IN--	Preposition or subordinating conjunction
# 	7.	JJ--	Adjective
# 	8.	JJR--	Adjective, comparative
# 	9.	JJS--	Adjective, superlative
# 	10.	LS--	List item marker
# 	11.	MD--	Modal
# 	12.	NN--	Noun, singular or mass
# 	13.	NNS--	Noun, plural
# 	14.	NNP--	Proper noun, singular
# 	15.	NNPS--	Proper noun, plural
# 	16.	PDT--	Predeterminer
# 	17.	POS--	Possessive ending
# 	18.	PRP--	Personal pronoun
# 	19.	PRP$--	Possessive pronoun
# 	20.	RB--	Adverb
# 	21.	RBR--	Adverb, comparative
# 	22.	RBS--	Adverb, superlative
# 	23.	RP--	Particle
# 	24.	SYM--	Symbol
# 	25.	TO--	to
# 	26.	UH--	Interjection

# 	33.	WDT--	Wh-determiner
# 	34.	WP--	Wh-pronoun
# 	35.	WP$--	Possessive wh-pronoun
# 	36.	WRB--	Wh-adverb


# CC	conjunction, coordinating	and, or, but
# CD	cardinal number	five, three, 13%
# DT	determiner	the, a, these
# EX	existential there	there were six boys
# FW	foreign word	mais
# IN	conjunction, subordinating or preposition	of, on, before, unless
# JJ	adjective	nice, easy
# JJR	adjective, comparative	nicer, easier
# JJS	adjective, superlative	nicest, easiest
# LS	list item marker
# MD	verb, modal auxillary	may, should
# NN	noun, singular or mass	tiger, chair, laughter
# NNS	noun, plural	tigers, chairs, insects
# NNP	noun, proper singular	Germany, God, Alice
# NNPS	noun, proper plural	we met two Christmases ago
# PDT	predeterminer	both his children
# POS	possessive ending	's
# PRP	pronoun, personal	me, you, it
# PRP$	pronoun, possessive	my, your, our
# RB	adverb	extremely, loudly, hard
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	adverb, particle	about, off, up
# SYM	symbol	%
# TO	infinitival to	what to do?
# UH	interjection	oh, oops, gosh
# VB	verb, base form	think
# VBZ	verb, 3rd person singular present	she thinks
# VBP	verb, non-3rd person singular present	I think
# VBD	verb, past tense	they thought
# VBN	verb, past participle	a sunken ship
# VBG	verb, gerund or present participle	thinking is fun
# WDT	wh-determiner	which, whatever, whichever
# WP	wh-pronoun, personal	what, who, whom
# WP$	wh-pronoun, possessive	whose, whosever
# WRB	wh-adverb	where, when

# p, d, a - context
# everything else but not v

# anything else POS


POS_coarse_mapping = {'NN': 'n',  # NOUN
					  'NNS': 'n',
					  'NNP': 'n',
					  'NNPS': 'n',

					  'JJ': 'a',  # adjective
				   	  'JJR': 'a',
				   	  'JJS': 'a',
				   	  'CD': 'a', # number, but ... good enough
				   	  'PDT': 'a',

					  'PRP$': 'o',  # pronouns
					  'PRP': 'o',

					  'WP$': 'w',  # wh-words
					  'WP': 'w',
					  'WRB': 'w',
					  'WDT': 'w',

				   	  'MD': 'v',  # verb
					  'VB': 'v',
					  'VBD': 'v',
					  'VBG': 'v',
					  'VBN': 'v',
					  'VBP': 'v',
					  'VBZ': 'v',

					  'RB': 'r',  # adverb
					  'RBR': 'r',
					  'RBS': 'r',

					  'CC': 'c',   # coord_conj

					  'IN': 'p',  # prep_or_conj

					  'DT': 'd',  # determiner

					  'TO': 't', # to

					  'EX': 'x', # existenital there

					  'minor': 'minor',

					  'FW': 'z',  # does_not_appear
					  'LS': 'z',
					  'SYM': 'z',
					  'POS': 'z',

					  'RP': 'z', # up, down ... preps in phrasal verbs :)

					  '': 'z',   # pass
					  'mismatch': 'z',
					  'UH': 'z'}
