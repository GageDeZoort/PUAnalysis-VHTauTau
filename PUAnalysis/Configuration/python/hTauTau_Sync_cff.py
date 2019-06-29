# 
# hTauTau_Sync_cff.py
# Updated June 28th, 2019
# By Gage DeZoort 
#

import FWCore.ParameterSet.Config as cms
from PUAnalysis.Configuration.tools.CutSequenceProducer import *

# Initialize a cut sequence producer for MuMuMuTau
mmmt = CutSequenceProducer(initialCounter = 'initialEvents_mmmt', pyModuleName = __name__, pyNameSpace = locals())

# Build the Z->MuMu collection 
mmmt.addDiCandidateModule('mmmtMuMu', 'PATMuPairProducer', 'slimmedMuons', 'slimmedMuons', 'slimmedMETs', '', 'slimmedJets', 1, 9999, text = 'mmmtMuMu', leadingObjectsOnly = False, dR = 0.3, recoMode = "", genParticles = 'genDaughters')

# Add baseline muon selection criteria 
mmmt.addSelector('MuMuCharge', 'PATMuPairSelector', 'charge==0', 'MuMuCharge')
mmmt.addSelector('MuMuRelIso', 'PATMuPairSelector', 'leg1.PFIsoLoose&&leg2.PFIsoLoose', 'MuMuRelIso')
mmmt.addSelector('MuMuEta', 'PATMuPairSelector', 'abs(leg1.eta())<2.4&&abs(leg2.eta())<2.4', 'MuMuEta')
mmmt.addSelector('MuMuPt', 'PATMuPairSelector', 'leg1.pt()>10&&leg2.pt()>10', 'MuMuPt')
mmmt.addSelector('MuMuLooseID', 'PATMuPairSelector', 'leg1.isLooseMuon()&&leg2.isLooseMuon()', 'MuMuLooseID')

# Build the H->MuTau collection
mmmt.addDiCandidateModule('mmmtMuTau', 'PATMuTauPairProducer', 'slimmedMuons', 'slimmedTaus', 'slimmedMETs', '', 'slimmedJets', 1, 9999, text='mmmtMuTau', leadingObjectsOnly = False, dR = 0.3, recoMode = "", genParticles = 'genDaughters')

# Build the ZH->MuMuMuTau collection 
mmmt.addDiCandidateModule('MuMuMuTau', 'PATMuMuMuTauQuadProducer', 'mmmtMuMu', 'mmmtMuTau', 'slimmedMETs', '', 'slimmedJets', 1, 9999, text = 'MuMuMuTau', leadingObjectsOnly = False, dR = 0.01, recoMode = "", genParticles = 'genDaughers')

# Add further baseline selection criteria
mmmt.addSelector('mmmtLeadingZMuID', 'PATMuMuMuTauQuadSelector', 'leg1.leg1.isGlobalMuon()&&leg1.leg1.isTrackerMuon()&&leg1.leg2.isTrackerMuon()&&leg1.leg2.isTrackerMuon()', 'mmmtLeadingZMuID')
mmmt.addSelector('mmmtHiggsMuID','PATMuMuMuTauQuadSelector','leg2.leg1.isGlobalMuon()&&leg2.leg1.isTrackerMuon()','mmmtHiggsMuID')

#Add a sorter for the leptons
#TODO

#Return a selection sequence
selectionSequence_mmmt = mmmt.returnSequence()



