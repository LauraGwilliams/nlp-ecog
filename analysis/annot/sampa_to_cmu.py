# Authors: Laura Gwilliams <leg5@nyu.edu>
#		   (Partly adapted from code from Tal Linzen)
# License: BSD (3-clause)
# Purpose: convert SAMPA phonetic/syllabic/morphological transcription
# 		   into the more commonly used CMU transcription

import numpy as np

class ELP2CMU(object):

    single = {'S': 'SH', 'O': 'AO', 'I': 'AH', 'U': 'UH', 'h': 'HH',
            'V': 'AH', 'j': 'Y', 'o': 'OW', '4': 'D', 'T': 'TH',
            'Z': 'ZH',
            'u': 'UW', 'E': 'EH', 'i': 'IY', 'D': 'DH', 'A': 'AA',
            'I': 'IH', 'N': 'NG', 'a': 'AE', 'e': 'EY', '@': 'AH'}

    double = {'hw': 'W', 'OI': 'OY', 'aI': 'AY', 'dZ': 'JH',
            'aU': 'AW', '3`': 'ER', 'tS': 'CH', '@`': 'ER'}

    morphology = {'{': 'base_onset',
    			  '}': 'base_offset',
    			  '$}': 'base_offset',
    			  '--': 'bound',
    			  '<': 'prefix',
    			  '>': 'suffix'}

    symbol_set = '."%{-<>='

    def translate(self, s):

        s = s.replace('$', '') # remove link to whether pron changes
        s = s.replace('--', '-') # simplify the symbol for bound morphemes

        # init
        elp = []
        res = []
        primary_stress = []
        secondary_stress = []
        syllable_boundary = []

        i = 0
        while i < len(s):

            # if just stress/syllable boundary, skip
            if s[i] in '."%{-<>}':
                elp.append(s[i])
                i = i + 1

            # check for double-character symbols
            elif len(s) > i + 1 and s[i:i+2] in self.double:
            	elp_string = s[i:i+2]
            	res_string = self.double[elp_string]

            	# add syllable/stress info
            	if s[i-1] in self.symbol_set and i > 0:
            		res_string = ''.join([s[i-1], res_string])

            		if s[i-2] in self.symbol_set and i > 1:
            			res_string = ''.join([s[i-2], res_string])

            			if s[i-3] in self.symbol_set and i > 2:
            				res_string = ''.join([s[i-3], res_string])

            	if i < len(s)-1:
            	    if s[i+1] in '}=':
            	    	res_string = ''.join([s[i+1], res_string])

            		if i < len(s)-2:
            		    if s[i+2] in '}=':
            		    	res_string = ''.join([s[i+2], res_string])

            	# update counter
            	res.append(res_string)
            	elp.append(elp_string)
            	i = i + 2

            elif len(s) > i + 1 and s[i+1] == '=':
                res.append('AH')
                res_string = s[i].upper()

                # add syllable/stress info
                if s[i-1] in self.symbol_set and i > 0:
                	res_string = ''.join([s[i-1], res_string])

                	if s[i-2] in self.symbol_set and i > 1:
                		res_string = ''.join([s[i-2], res_string])

                		if s[i-3] in self.symbol_set and i > 2:
                			res_string = ''.join([s[i-3], res_string])

                if i < len(s)-1:
                    if s[i+1] in '}=':
                    	res_string = ''.join([s[i+1], res_string])

                	if i < len(s)-2:
                	    if s[i+2] in '}=':
                	    	res_string = ''.join([s[i+2], res_string])


                # update counter
                res.append(res_string)
                elp.append(''.join([]))
                i = i + 2

            elif s[i] in self.single:

                res_string = self.single[s[i]]

                # add syllable/stress info
                if s[i-1] in self.symbol_set and i > 0:
                    res_string = ''.join([s[i-1], res_string])

                    if s[i-2] in self.symbol_set and i > 1:
                        res_string = ''.join([s[i-2], res_string])

                        if s[i-3] in self.symbol_set and i > 2:
                            res_string = ''.join([s[i-3], res_string])

                if i < len(s)-1:
                    if s[i+1] in '}=':
                    	res_string = ''.join([s[i+1], res_string])

                	if i < len(s)-2:
                	    if s[i+2] in '}=':
                	    	res_string = ''.join([s[i+2], res_string])

                res.append(res_string)
                i = i + 1

            elif s[i] == 'r' and len(res) > 0 and res[-1] == 'ER':
                i = i + 1

            else:
                res_string = s[i].upper()

                # add syllable/stress info
                if s[i-1] in self.symbol_set and i > 0:
                    res_string = ''.join([s[i-1], res_string])

                    if s[i-2] in self.symbol_set and i > 1:
                    	res_string = ''.join([s[i-2], res_string])

                    	if s[i-3] in self.symbol_set and i > 2:
                    		res_string = ''.join([s[i-3], res_string])

                if i < len(s)-1:
                    if s[i+1] in '}=':
                    	res_string = ''.join([s[i+1], res_string])

                	if i < len(s)-2:
                	    if s[i+2] in '}=':
                	    	res_string = ''.join([s[i+2], res_string])

                res.append(res_string)
                i = i + 1
        #
        # # fix annoying problem with one of the phonemes being treated
        # # as separately incorrectly
        # if '.R' in res:
        #     loc = np.where(np.array(res) == '.R')[0][0]
        #     res[loc-1:loc+1] = [''.join(res[loc-1:loc+1])]
        #
        # if '}R' in res:
        #     loc = np.where(np.array(res) == '}R')[0][0]
        #     if 'AO' in res[loc-1]:
        #         res[loc-1:loc+1] = [''.join(res[loc-1:loc+1])]
        #
        # if '.L' in res:
        #     loc = np.where(np.array(res) == '.L')[0][0]
        #     if 'AH' in res[loc-1]:
        #         res[loc-1:loc+1] = [''.join(res[loc-1:loc+1])]
        #
        # if '}L' in res:
        #     loc = np.where(np.array(res) == '}L')[0][0]
        #     if 'AH' in res[loc-1]:
        #         res[loc-1:loc+1] = [''.join(res[loc-1:loc+1])]


        return res


def convert_to_cmu(s):
    elp2cmu = ELP2CMU()
    phoneme_list = elp2cmu.translate(s)
    syllable_boundary = [('.' in p)*1 for p in phoneme_list]
    syllable_boundary[0] = 1  # first phoneme always the beginning of a syllable
    syllable_offset = np.roll(syllable_boundary, -1)
    syllable_offset[-1] = 1  # last phoneme always the end of a syllable

    primary_stress = [('"' in p)*1 for p in phoneme_list]
    secondary_stress = [('%' in p)*1 for p in phoneme_list]

    base_onset = [('{' in p)*1 for p in phoneme_list]
    base_offset = [('}' in p)*1 for p in phoneme_list]
    bound = [('-' in p)*1 for p in phoneme_list]
    prefix = [('<' in p)*1 for p in phoneme_list]
    suffix = [('>' in p)*1 for p in phoneme_list]
    syllabic_consonant = [('=' in p)*1 for p in phoneme_list]

    return([phoneme_list, np.array([syllable_boundary, primary_stress, secondary_stress,
                     base_onset, base_offset, bound, prefix, suffix, syllable_offset,
                     syllabic_consonant])])
