# Reserve File Splitter

## Overview

This project automates the process of splitting reserve data stored in Microsoft Excel into separate files based on unique elevation levels.

Given one or more reserve workbooks, the script identifies each unique value in the **`z`** (elevation level) column and generates:

* A new Excel workbook containing one worksheet for each elevation level.
* A folder containing CSV files, with one CSV corresponding to each elevation level.

This eliminates the need to manually filter, copy, and export reserve data, making the workflow significantly faster and less error-prone.

## Features

* Processes multiple reserve workbooks in a single run.
* Automatically groups data by unique **`z`** values.
* Creates a split Excel workbook for each input file.
* Exports each elevation level as an individual CSV file.
* Automatically creates output folders if they do not already exist.
* Uses the script's directory as the working directory, allowing it to be executed from anywhere.

## Input

The script expects Excel files following the naming convention:

```text
A1B1 RESERVE.xlsx
A1B2 RESERVE.xlsx
A2B1 RESERVE.xlsx
...
```
Each workbook must contain a column named **`z`**, which is used to separate the data.

## Output


For each input workbook, the script generates:


```text
A1B1 RESERVE_split.xlsx
A1B1/

├── 100.csv
├── 110.csv
├── 120.csv
└── ...

```


* **`*_split.xlsx`** contains one worksheet for each unique elevation.
* The output folder contains one CSV file per elevation level.


## Requirements


* Python 3.10 or later
* pandas

* openpyxl


Install the required packages using:

```bash
pip install pandas openpyxl
```


## Use Case


This tool is intended for reserve modeling and mining workflows where reserve data must be separated into individual elevation slices for downstream processing, analysis, or import into other software.

