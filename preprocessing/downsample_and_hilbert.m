current_dir = pwd;
disp(current_dir);

% params
load('../continuous_speech/timit_laterality/includedata.mat');
subjAll = subj;
blocknumsAll = corpBlocks;

% subjs and blocks
%subjAll = 'EC183', 'EC186'};
%blocknumsAll = {[49, 45, 43, 78, 79, 107], [2, 4, 15, 16, 22]};

subjAll = {'EC228'};
blocknumsAll = {[28, 29, 31, 32, 33]}; %{[2, 5, 8, 12, 15]};

% analysis params
alloutflags = [3]; % 3 - hga, 2 - 47 band all freq amplitude; 4 - only notch
outnames = {'HilbAA_70to150_8band'};%, 'AfterNotchNoCAR'};%; 'HilbAA_4to200_40band';'AfterCARandNotch','HilbAA_70to150_8band'};

% paths
output_dir = '/userdata/lgwilliams/prcsd_data/';
%input_dir = '/data_store1/human/prcsd_data/';
input_dir = output_dir;

% datapath = '/Users/yuliao/Dropbox/prcsd_data/' ;
%     datapath = '/data_store0/human/HTK_raw/' ;
%     datapath = '/Users/yuliao/Dropbox/prcsd_data/' ;


%% add matlab to path
mpath = fileparts(mfilename('fullpath'));
addpath(genpath(fullfile(mpath, '..','..','..', 'matlab')));
addpath(genpath('../prelimAnalysis_ALL'))

% addpath(genpath('../../ecog_scripts'))
%[outpath,datapath]=setDatapath;
carflag = 0; % 16 for 16-channel car
%% output high gamma analytic amplitude
for cs = 1:length(subjAll)
    subj = subjAll{cs};

    % derivative paths
    blockPath_in = fullfile(input_dir, subj);
    blockPath_out = fullfile(output_dir, subj);

    % loop through blocks for this subject
    blocknums = blocknumsAll{cs};
    for i = 1:length(alloutflags)
        coutfl = alloutflags(i);
        coutname = outnames{i};
        for cbl = 1:length(blocknums)

            block_number = num2str(blocknums(cbl));
            % get subj and block string
            subj_block = strcat(subj, '_B', block_number);
            disp(subj_block);

            cbpath = fullfile(blockPath_in, subj_block);
            %             coutpath = '/userdata/yuliao/prcsd_data/';
            %             copyfile(fullfile(blockPath, ['*_B' num2str(blocknums(cbl))]), fullfile(coutpath, subj));
            %             cbpath = fullfile(coutpath, subj,[subj '_B' num2str(blocknums(cbl))]);
            fprintf(2, 'Analyzing Block %s \n', cbpath);
            disp(cbpath);

            if ~exist(cbpath, 'dir')
                disp([subj ', block '  num2str(blocknums(cbl)) 'does not exist.']);
            else
		disp('ok are we going to try to make the hg now please');
                coutfolder = fullfile(blockPath_out, subj_block, coutname);
                disp(coutfolder);
		if ~exist(coutfolder, 'dir')
                    transformData(cbpath, 'outFlag', coutfl, 'CARFlag' ,carflag);
                else
                    if exist(fullfile(cbpath, 'RawHTK'), 'dir')
                        a = dir(fullfile(coutfolder, '*.htk'));
                        b = dir(fullfile(cbpath, 'RawHTK', '*.htk'));
                        if length(a)==length(b)
                            disp([subj ', block '  num2str(blocknums(cbl)) ' HG exists']);
                        else
                            disp([subj ', block '  num2str(blocknums(cbl)) ' HG not complete']);
                            transformData(cbpath, 'outFlag', coutfl, 'CARFlag' ,carflag);
                            
                        end
                    end
                end
            end
            fprintf(2, 'Finished Block %s \n ' , cbpath);
        end
    end
end
