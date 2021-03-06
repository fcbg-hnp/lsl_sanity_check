# Introduction

**lsl_sanity_check** has been implemented for a quick sanity check of the LSL streams contained in a .xdf file (recorded with [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder)).

It will load the file and display the available stream's info + data.

# Prerequisites
 **lsl_sanity_check** uses Python 3 and depends on following packages:
   - numpy
   - pyxdf

# Installation

Clone the repository:
```
git clone https://github.com/fcbg-hnp/lsl_sanity_check
```
Run setup script:
```
pip install -e .
```

# Usage

### From terminal
```bash
cd ./lsl_sanity_check
python lsl_sanity_check.py
```
Then provided the path to the .xdf file to analyse.

### As a module
```python
from lsl_sanity_check import lsl_sanity_check

lsl_sanity_check("path2file")
```

# Uninstallation
```bash
pip uninstall lsl_sanity_check
```
