#include "FWCore/Framework/interface/MakerMacros.h"
#include "PUAnalysis/NtupleTools/plugins/StringBasedNtupleFiller.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairFiller, "PATMuTauPairFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATGenParticleFiller, "PATGenParticleFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairFiller, "PATEleTauPairFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATDiTauPairFiller, "PATDiTauPairFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuPairFiller, "PATMuPairFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATElePairFiller, "PATElePairFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuonFiller, "PATMuonFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATPFMETFiller, "PATPFMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMETFiller, "PATMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATGenMETFiller, "PATGenMETFiller");

//MODIFIED
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuMuMuQuadFiller, "PATMuMuMuMuQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuMuTauQuadFiller, "PATMuMuMuTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuTauTauQuadFiller, "PATMuMuTauTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuEleTauQuadFiller, "PATMuMuEleTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuEleMuQuadFiller, "PATMuMuEleMuQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuMuEleEleQuadFiller, "PATMuMuEleEleQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleMuMuQuadFiller, "PATEleEleMuMuQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleMuTauQuadFiller, "PATEleEleMuTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleTauTauQuadFiller, "PATEleEleTauTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleEleTauQuadFiller, "PATEleEleEleTauQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleEleMuQuadFiller, "PATEleEleEleMuQuadFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleEleEleEleQuadFiller, "PATEleEleEleEleQuadFiller");
