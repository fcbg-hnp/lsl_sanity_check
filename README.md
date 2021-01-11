# Introduction

**lsl_sanity_check** has been implemented for a quick sanity check of the LSL streams of a .xdf file (recorded by [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder)).

# Prerequisites
 **lsl_sanity_check** depends on following packages:
    - pyxdf

# Installation

Clone the repository:
```
git clone https://github.com/fcbg-hnp/lsl_sanity_check
```
Run setup script:
```
python setup.py develop
```

# Usage

##From terminal
```
cd ./lsl_sanity_check
python lsl_sanity_check.py
```
Then provided the path to the .xdf file to analyse.
