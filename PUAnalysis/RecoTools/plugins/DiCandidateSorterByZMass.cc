/*
 * DiCandidateSorterByZMass.cc
 * Updated June 28th, 2019
 * By Gage DeZoort 
 *
 */

#include "PUAnalysis/RecoTools/plugins/PATTauMatchSelector.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "PUAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "PUAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"
#include "PUAnalysis/RecoTools/plugins/DiCandidateSorterByZMass.h"

//MODIFIED
typedef DiCandidateSorterByZMass<PATMuTauPair> PATMuTauPairSorterByZMass; //mt
typedef DiCandidateSorterByZMass<PATMuPair> PATMuPairSorterByZMass; //mm
typedef DiCandidateSorterByZMass<PATElecPair> PATElePairSorterByZMass; //ee
typedef DiCandidateSorterByZMass<PATElecMuPair> PATEleMuPairSorterByZMass; //em
typedef DiCandidateSorterByZMass<PATElecTauPair> PATEleTauPairSorterByZMass; //et
typedef DiCandidateSorterByZMass<PATMuMuMuTauQuad> PATMuMuMuTauQuadSorterByZMass; //mmmt
typedef DiCandidateSorterByZMass<PATMuMuTauTauQuad> PATMuMuTauTauQuadSorterByZMass; //mmtt
typedef DiCandidateSorterByZMass<PATMuMuEleTauQuad> PATMuMuEleTauQuadSorterByZMass; //mmet
typedef DiCandidateSorterByZMass<PATMuMuEleMuQuad> PATMuMuEleMuQuadSorterByZMass; //mmem
typedef DiCandidateSorterByZMass<PATMuMuMuMuQuad> PATMuMuMuMuQuadSorterByZMass; //mmmm
typedef DiCandidateSorterByZMass<PATMuMuEleEleQuad> PATMuMuEleEleQuadSorterByZMass; //mmee
typedef DiCandidateSorterByZMass<PATEleEleEleTauQuad> PATEleEleEleTauQuadSorterByZMass; //eeet
typedef DiCandidateSorterByZMass<PATEleEleTauTauQuad> PATEleEleTauTauQuadSorterByZMass; //eett
typedef DiCandidateSorterByZMass<PATEleEleEleEleQuad> PATEleEleEleEleQuadSorterByZMass; //eeee
typedef DiCandidateSorterByZMass<PATEleEleMuTauQuad> PATEleEleMuTauQuadSorterByZMass; //eemt
typedef DiCandidateSorterByZMass<PATEleEleEleMuQuad> PATEleEleEleMuQuadSorterByZMass; //eeem
typedef DiCandidateSorterByZMass<PATEleEleMuMuQuad> PATEleEleMuMuQuadSorterByZMass; //eemm


DEFINE_FWK_MODULE(PATMuTauPairSorterByZMass);
DEFINE_FWK_MODULE(PATMuPairSorterByZMass);
DEFINE_FWK_MODULE(PATElePairSorterByZMass);
DEFINE_FWK_MODULE(PATEleTauPairSorterByZMass);
DEFINE_FWK_MODULE(PATEleMuPairSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuMuTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuTauTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuEleTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuEleMuQuadSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuMuMuQuadSorterByZMass);
DEFINE_FWK_MODULE(PATMuMuEleEleQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleEleTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleTauTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleEleEleQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleMuTauQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleEleMuQuadSorterByZMass);
DEFINE_FWK_MODULE(PATEleEleMuMuQuadSorterByZMass);




/* NOTES:
 *
 * typedef DiCandidateSorterByZMass<PATMuTrackPair> PATMuTrackPairSorterByZMass;
 * typedef DiCandidateSorterByZMass<PATEleTrackPair> PATEleTrackPairSorterByZMass;
 * DEFINE_FWK_MODULE(PATMuTrackPairSorterByZMass);
 * DEFINE_FWK_MODULE(PATEleTrackPairSorterByZMass);
 *
 */
