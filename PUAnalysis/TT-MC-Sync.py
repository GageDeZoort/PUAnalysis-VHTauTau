# -------------------------
#      TT-MC-Sync.py
# -------------------------
#  Updated: Jun 22nd, 2019
#     by Gage DeZoort
#
#  see "notes" below file! 
# _________________________

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

#FrontierConditions_GlobalTag_condDBv2_cff just imports FrontierConditions_GlobalTag_cff
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

# Updated global tag for 2018 MC
process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v12'

# "Options" PSet 
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
 
# Set maxEvents to 20,000
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20000)
)

# Load the message logger, see every 10th message
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

# Source MC file - currently using a VBF->H->TauTau sample for testing purposes
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("root://cmsxrootd-site.fnal.gov//store/mc/RunIIAutumn18MiniAOD/ZHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/910000/A9AA2575-5E36-014E-B28F-AF41FC2AE9A4.root", "root://cmsxrootd-site.fnal.gov//store/mc/RunIIAutumn18MiniAOD/ZHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/F93DAE09-2189-B642-A1F6-F6EBD428B8B7.root", "root://cmsxrootd-site.fnal.gov//store/mc/RunIIAutumn18MiniAOD/ZHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/ED3564A1-67EE-B749-934E-29E913EE785F.root"),
                            inputCommands=cms.untracked.vstring('keep *', 'keep *_l1extraParticles_*_*',)
                            )

# defaultReconstruction(_,MC,EMB) from the analysisTools.py config file
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstructionMC(process,'HLT',
        [
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v'
        ])

# EventSelection from hTauTau_cff files
process.load("PUAnalysis.Configuration.hTauTau_Sync_cff")

process.metCalibration.applyCalibration = cms.bool(False)

# Name of the path (preselection, cutflow) from hTauTau_cff

#MODIFIED
#process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
process.eventSelection_mmmt = cms.Path(process.selectionSequence_mmmt)

# Collections of genparticles to keep
createGeneratedParticles(process,
        'genDaughters',
        [
            "keep++ pdgId = {Z0}",
            "keep pdgId = {tau+}",
            "keep pdgId = {tau-}",
            "keep pdgId = {mu+}",
            "keep pdgId = {mu-}",
            "keep pdgId = 6",
            "keep pdgId = -6",
            "keep pdgId = 11",
            "keep pdgId = -11",
            "keep pdgId = 25",
            "keep pdgId = 35",
            "keep pdgId = 37",
            "keep pdgId = 36"
            ]
        )
createGeneratedParticles(process,
        'genTauCands',
        [
            "keep pdgId = {tau+} & mother.pdgId()= {Z0}",
            "keep pdgId = {tau-} & mother.pdgId() = {Z0}"
            ]
        )

# Import/call function that makes EventTree, specifies variables for it 
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree 

#MODIFIED
addDiTauEventTree(process,'EventTree_mmmt','MuMuMuTau', fileNameString="analysis_VHtt_mmmt.root")

#For debugging, describes objects passing each selection step
addEventSummary(process,True,'TT','eventSelection_mmmt', fileNameString = 'analysis_VHtt_mmmt.root')




# -------
#  NOTES 
# -------

# Additional datasets (check CMSSW compatibility carefully):
# ----------------------------------------------------------
# "/store/mc/RunIIFall17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/
#  RECOSIMstep_94X_mc2017_realistic_v10-v1/00000/0293A280-B5F3-E711-8303-3417EBE33927.root"
# "/store/mc/RunIIFall17MiniAODv2/VBFHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/
#  PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/D092A5CA-B343-E811-96EB-002590E7D7C2.root"
# 'file:event-21753.root'
# '/store/mc/RunIISpring16MiniAODv1/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/
#  PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/10000/06A0B340-8025-E611-8262-B8CA3A708F98.root'
# 'file:VBFHttFXFX.root',
# '/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/
#  PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
# "/store/mc/RunIIAutumn18MiniAOD/VBFHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/
#  102X_upgrade2018_realistic_v15_ext1-v1/110000/CA6B3CD3-D2D5-784D-B2F9-78770C9E4BD9.root"

# Triggers Used:
# ------------------
# - HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v
#   ...tautau for 2018 MC and data run >= 317509
# - HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v
#   ...tautau for 2018 data < 317509
# - HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v
#   ...tautau for 2018 MC and data run >= 317509

# Old Triggers:
# ------------------------
# 'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v'
# 'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'
# 'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v'

# Default Reconstruction (analysisTools):
# ---------------------------------------------
# - The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
# - analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
# - files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
# - defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
# - needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
# - different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#   found in RecoTools/plugins/

# Event Selection:
# -----------------
# Most of the selections for the analysis go in hTauTau_cff
# The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#   this configuration then the sequence will start over with another di-candidate pair.
# The final 'sorting' is implemented there as well, either by di-tau PT or isolation.

# GenParticle Selection
# -----------------------
# Specifies which gen particles we wish to keep, this collection is used in the
# RecoTools/interface/CompositePtrCandidateT1T2MEtAlgorithm.h
# Most of the algorithm tools are done in the composite ptr candidate algorithm
#     module.

# addDiTauEventTree (config->python->tools->ntupletools)
# -------------------------------------------------------
# Create the Ntuples, the name "analysis_htautau.root" is set here as well
# This takes the output from the configuration sequence and fills
#    the tree that will later be used for plotting. Notice the names
#    added here 'diTauOS' is the default, however, this 'diTauOS' can
#    be replaced with any of the labled collections produced in htautau_cff.py
#    in order to create two different trees, one with all the final selections
#    and one with looser selections.


# process.GlobalTag.globaltag = '94X_mc2017_realistic_v15'
