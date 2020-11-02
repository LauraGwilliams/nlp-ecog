# nlp-ecog
preprocessing and analysis scripts for our NLP project

# explanation of out stucture fields
%   out(sent).name: name of the wav file (e.g. 'f2bprlp1')
%   out(sent).sound: the sound waveform
%   out(sent).soundf: the sampling frequency of the sound waveform in Hz (usually 16000)
%   out(sent).dataf: the sampling frequency of the neural data
%   out(sent).aud: the spectrogram of this sentence (80 mel bands x time points, at dataf frequency)
%   out(sent).duration: duration of the trial in seconds
%   out(sent).Trials: the trial numbers
%   out(sent).befaft: number of seconds before and after to pad with silence
%   out(sent).resp: [nchans x n time pts], responses for this particular sentence
