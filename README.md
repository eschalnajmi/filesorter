# File Sorter

A simple GUI in pyqt to move files over from a source directory and copy them into a destination directory whilst sorting them in the process.

## How to run

1. Open your terminal and type in:
```
git clone https://github.com/eschalnajmi/filesorter.git
```
```
cd filesorter
```
2. Create and activate a conda environment by typing in:
```
conda env create -f environment.yaml
```
```
conda activate sort_files
```
3. Run the actual application by typing:
```
python main.py
```

## How it works

Given a source directory of files, it moves and sorts the files into directories based on a standard naming convention and a provided number of first characters in the files name.
For example, given files names ```test1111.txt``` ```test1112.txt``` ```test1121.txt``` and ```test113.txt```, a first character count of ```7``` and a naming convention of ```_00``` it would result in the desitnation directory looking like:
```
.
└── destination/
    ├── test111_00/
    │   ├── test1111.txt
    │   └── test1112.txt
    ├── test112_00/
    │   └── test1121.txt
    └── test113_00/
        └── test113.txt
```