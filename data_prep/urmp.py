from tqdm import tqdm
import argparse
import shutil
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("--dataroot", type=str, default='../../datasets/urmp/', help="data root of flickr")
parser.add_argument("--outdir", type=str, default='../voice_conversion/data/data_urmp/', help="output directory")
args = parser.parse_args()
print(args)

# Gets the audio seperated wavs of a specific instrument from the URMP dataset
def get_audiosep_ins(ins):
    return glob.glob(args.dataroot + '**/AuSep*'+ins+'*.wav', recursive = True)

# Saves wavs belonging to speaker from list of speaker files
def urmp_prep_wavs(outdir, instrument_files, src):
    os.makedirs(outdir, exist_ok=True)
    for f in tqdm(instrument_files, desc="extracting ins %s"%src):
        shutil.copy(f, outdir)
        
trumpet_files = get_audiosep_ins('tpt')
violin_files = get_audiosep_ins('vn')
flute_files = get_audiosep_ins('fl')
mohanveena_files=get_audiosep_ins('mv')
cello_files = get_audiosep_ins('vc')
trombone_files = get_audiosep_ins('tbn')
viola_files = get_audiosep_ins('va')
oboe_files = get_audiosep_ins('ob')
saxophone_files = get_audiosep_ins('sax')
clarinet_files = get_audiosep_ins('cl')
# Data preparation
urmp_prep_wavs(args.outdir+'spkr_4', trumpet_files, 'tpt')
urmp_prep_wavs(args.outdir+'spkr_3', violin_files, 'vn')
urmp_prep_wavs(args.outdir+'spkr_2', flute_files, 'fl')  
#urmp_prep_wavs(args.outdir+'spkr_4', cello_files, 'vc')
urmp_prep_wavs(args.outdir+'spkr_1', mohanveena_files, 'mv')
urmp_prep_wavs(args.outdir+'spkr_8', trombone_files, 'tbn')
urmp_prep_wavs(args.outdir+'spkr_6', viola_files, 'va')
urmp_prep_wavs(args.outdir+'spkr_7', oboe_files, 'ob')
urmp_prep_wavs(args.outdir+'spkr_5', saxophone_files, 'sax')
urmp_prep_wavs(args.outdir+'spkr_9', clarinet_files, 'cl')  
