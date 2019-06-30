#PUAnalysis
###Quickstart:
Here's a quick recipe for grabbing a copy PUA configured for 2018 MC: 

```
cmsrel CMSSW_10_2_14 #for 2018 analysis
cd CMSSW_10_2_14/src/
cmsenv
git cms-init 
git clone -b ZH-2018-MC https://github.com/GageDeZoort/PUAnalysis-VHTauTau.git
export USER_CXXFLAGS="-Wno-delete-non-virtual-dtor -Wno-error=unused-but-set-variable -Wno-error=unused-variable -Wno-error=sign-compare -Wno-error=reorder"
cd PUAnalysis
bash recipe.sh #Note Recipe13TeV.sh should be the full recipe, but keep it simple at first
scram b -j 10
```
Once everything's compiled, try running the analysis as follows: 

```
cd PUAnalysis
cmsRun TT-MC-Sync.py
```
The output ntuple is __analysis_VHtt_mmmt.root__, which corresponds to Z->mumu and H->tautau. 


