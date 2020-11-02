% Run the TIMIT analysis on a subject
% Pass this script to submit_job, for example:
%
% submit_job -e liberty.hamilton@ucsf.edu -o /home/libertyh/ec118_timit_test8.txt -m 20 -x matlab run_TIMIT_analysis.m
%
% This will produce an out structure in the TIMIT directory in your datapath that contains the 
% auditory and neural data aligned and indexed by sentence.
% Output fields include (for sentence 1, for example):
%
%   sent = 1;
%   out(sent).name: name of the wav file (e.g. 'fadg0_si1279')
%   out(sent).txt: the sentence text for this stimulus (e.g. 'Bricks are an alternative')
%   out(sent).sound: the sound waveform
%   out(sent).soundf: the sampling frequency of the sound waveform in Hz (usually 16000)
%   out(sent).dataf: the sampling frequency of the neural data
%   out(sent).aud: the spectrogram of this sentence (80 mel bands x time points, at dataf frequency)
%   out(sent).duration: duration of the trial in seconds
%   out(sent).Trials: the trial numbers
%   out(sent).befaft: number of seconds before and after to pad with silence
%   out(sent).resp: [nchans x n time pts], responses for this particular sentence
%   out(sent).phnmat: [59 x n time pts], binary phoneme matrix
%   out(sent).phnmatonset: [59 x n time pts], binary phoneme matrix, where only the onset of each phoneme
%			   is marked, rather than the phoneme's full duration.
% 
% Written by Liberty Hamilton, 2016

% Whether running on the server
server_flag = 1;

% Things to change depending on the subject
% Which TIMIT subset (must be in the same order as blocks)
% Which ANIN channel to use for event alignment 
% (normally ANIN2, but sometimes ANIN1 (mic) or ANIN3 if ANIN2 is bad)
% This can be different for each block, since you most likely would 
% want to use ANIN2, and only use ANIN1 if necessary.

% make a struct for the subjects
subject_struct = struct();

% fill info for each subject we want to analyse
subject_struct(1).subject = 'EC183';
subject_struct(1).blocks = {'EC183_B43', 'EC183_B45', 'EC183_B49', 'EC183_B67', 'EC183_B78', 'EC183_B79', 'EC183_B107'};
subject_struct(1).timit_nums = [1, 2, 5, 3, 1, 2, 4];
subject_struct(1).anin_nums = [2, 2, 2, 2, 2, 2, 2];
subject_struct(1).elects = 1:256; % which electrodes to include in the out structure

subject_struct(2).subject = 'EC118';
subject_struct(2).blocks = {'EC118_B5','EC118_B21','EC118_B58','EC118_B62','EC118_B82','EC118_B85'};
subject_struct(2).timit_nums = [5, 1, 2, 3, 4, 3];
subject_struct(2).anin_nums = [2, 2, 2, 2, 2, 2];
subject_struct(2).elects = 1:256; % which electrodes to include in the out structure

subject_struct(3).subject = 'EC186';
subject_struct(3).blocks = {'EC186_B2', 'EC186_B4', 'EC186_B15', 'EC186_B16', 'EC186_B22'};
subject_struct(3).timit_nums = [1, 2, 5, 3, 4];
subject_struct(3).anin_nums = [2, 2, 2, 2, 2];
subject_struct(3).elects = 1:256; % which electrodes to include in the out structure

subject_struct(4).subject = 'EC188';
subject_struct(4).blocks = {'EC188_B2', 'EC188_B3', 'EC188_B6', 'EC188_B7', 'EC188_B8', 'EC188_B11', 'EC188_B12', 'EC188_B13'};
subject_struct(4).timit_nums = [1, 2, 3, 4, 5, 3, 4, 5];
subject_struct(4).anin_nums = [2, 2, 2, 2, 2, 2, 2, 2];
subject_struct(4).elects = 1:256; % which electrodes to include in the out structure

subject_struct(5).subject = 'EC228';
subject_struct(5).blocks = {'EC228_B2', 'EC228_B5', 'EC228_B8', 'EC228_B12', 'EC228_B15'};
subject_struct(5).timit_nums = [1, 2, 3, 4, 5];
subject_struct(5).anin_nums = [2, 2, 2, 2, 2];
subject_struct(5).elects = 1:256; % which electrodes to include in the out structure


% loop through the subj structs :)
for ii = 5:5 %length(subject_struct);

    disp(ii);
    
    % get out the info of this subj
    subj = subject_struct(ii).subject;
    blocks = subject_struct(ii).blocks;
    timit_nums = subject_struct(ii).timit_nums;
    anin_nums = subject_struct(ii).anin_nums;
    elects = subject_struct(ii).elects;

    opts = struct();
    opts.cond = 'HilbAA_70to150_8band'; %'RawHTK'; % 'HilbAA_70to150_8band';
    opts.bef = 0.75;
    opts.aft = 0.75;
    opts.specflag = 'mel'; % for mel-band frequency spectrogram
    opts.logflag = 0; % whether to log-transform high gamma data
    opts.fs = 100;
    
    % print some info to the log file
    sprintf('subject=%s, datatype=%s', subj, opts.cond);

    if server_flag
        % Path to the data with HTK files
        datapath = sprintf('/userdata/lgwilliams/prcsd_data/%s', subj);
        % Path to the code
        codepath = '/home/lgwilliams/mattl_scripts/TIMIT/';
        % Path to the TIMIT stimuli
        stimpath = [codepath '/@ECSpeech/Sounds'];
        % Add the appropriate code to your path
        addpath(genpath(codepath));
    else
        % Path to the data with HTK files
        datapath = sprintf('/Users/mattleonard/Documents/Research/data/raw_data/%s', subj);
        % Path to the code
        codepath = '/Users/mattleonard/Documents/matlab/TIMIT';
        % Path to the TIMIT stimuli
        stimpath = [codepath '/@ECSpeech/Sounds'];
    end


    % Create the out structure, D matrix, PSI matrix, and hdf5 files for python STRF fitting
    out = TIMIT_analysis(subj, datapath, codepath, blocks, timit_nums, anin_nums, stimpath, elects, opts);
end
