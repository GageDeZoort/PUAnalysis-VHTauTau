/*
 * DiCandidateSorterByZMass.h
 * Updated June 28th, 2019
 * By Gage DeZoort 
 *
 */

#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "Math/GenVector/VectorUtil.h"


template <class T>
class DiCandidateSorterByZMass : public edm::EDProducer {
  
 public:

  explicit DiCandidateSorterByZMass(const edm::ParameterSet& iConfig):
  src_(consumes<std::vector<T>>(iConfig.getParameter<edm::InputTag>("src")))
    {
      produces<std::vector<T> >();
    }
  
  ~DiCandidateSorterByZMass() {}
  
  
 private:
  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
  {
    using namespace edm;
    using namespace reco;
    
    std::vector<T> toBeSorted;
    Handle<std::vector<T> > cands;
    if(iEvent.getByToken(src_,cands)) 
      toBeSorted =  *cands;
    
    if(toBeSorted.size()>0) {
      Sorter sorter;
      std::sort(toBeSorted.begin(),toBeSorted.end(),sorter);
    }
    
    std::unique_ptr<std::vector<T> > out(new std::vector<T>);
    
    for(unsigned int i=0;i<toBeSorted.size();++i){
      //	tempSum=toBeSorted.at(i).leg1()->pt()+toBeSorted.at(i).leg2()->pt();
      //std::cout << "First Z mass: " << toBeSorted.at(i).leg1()->mass() << ", second Z mass: " << toBeSorted.at(i).leg2()->mass() << ", pt sum: " << tempSum << std::endl;
      out->push_back(toBeSorted.at(i));
    }
    
    iEvent.put(std::move(out),"");    

  } 

  //  template<class T>
  class Sorter {
  public:
    Sorter() 
      {}
    ~Sorter()
      {}
    bool operator()(T t1,T t2)
    {
      return (abs(t1.leg1()->mass()-91.2) < abs(t2.leg1()->mass()-91.2));
    } 
  };
  
      // ----------member data ---------------------------
      edm::EDGetTokenT<std::vector<T>>  src_;

};
