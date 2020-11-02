%% this is the main script for preprocessing timit and dimex data. 
% Possible inputs to corpora_pipeline are: 
    % subj: subject id, e.g. EC137
    % corpBlocks:number of patient's blocks that contain timit data, e.g.   [4 12 13 15 16]
    % corp_numbers: number of timit task blocks (1-5) or dimex task blocks (1-5, 11) for each of the data blcoks in corpBlocks. should be in the same order as corpBlocks
    % corpus: timit or dimex, as string
    % anin_to_use: which analog input to use for trial alignment, 1 - 3,
    % default: 2
    % z_flag: local (default) or global z-scoring
    % datapath: location of raw data on disk 
    % outpath: folder where results matrices are to be saved
addpath(genpath('../../ecog_scripts'))
addpath(genpath('/home/lgwilliams/mattl_scripts/TIMIT'))
addpath(genpath('/home/lgwilliams/yulia_scripts'))

subj = 'EC228';
corpBlocks = [28, 29, 31, 32, 33];
% subj = 'EC166';
% corpBlocks = [15:17 46 47 49];
% subj = 'EC175';
% corpBlocks =[2 3 6 8 9 14 16]; % [5 13 51 52 70];
 % subj = 'EC173';
% corpBlocks =[2 3 29 30 31]; % [5 13 51 52 70];

% subj = 'EC177';
% corpBlocks =[3 4 5 8 9]; % [5 13 51 52 70];
corp_numbers = [1:5]; % should be in the same order as corpBlocks above
anaBand = 'HilbAA_70to150_8band';
electrodes = 1:256;



corpus = 'BU'; % corpus to analyze
anin_to_use = 1*ones(size(corpBlocks));
z_flag = 'global';

% datapath = '/data_store1/human/prcsd_data/'; %, 'global_z'); %, 'pre_sent_zscoring');
% datapath = '/Users/yuliao/Dropbox/prcsd_data/'; %, 'global_z'); %, 'pre_sent_zscoring');
% outpath = '/userdata/yuliao/data/';%
% outpath = '/Users/yuliao/Dropbox/data/';
%[outpath, datapath] = setDatapath;
% datapath = '/userdata/yuliao/prcsd_data/'; %, 'global_z'); %, 'pre_sent_zscoring');
datapath = '/userdata/lgwilliams/prcsd_data/';
outpath = datapath;

corpora_pipeline(subj, corpBlocks, corp_numbers,corpus, anin_to_use, z_flag, datapath, outpath,electrodes,anaBand)
