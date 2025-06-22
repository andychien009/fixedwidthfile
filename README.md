# Overview
fixedwidthfile is a Python library that assists with the processing of fixed width file.

While CSV file format remain the popular non-propriatory data file formate in the field of data analytics, much of the main frame input/output file remain to be fixed width file (see [appendix](#app-fll) to gain an understanding why). 

This library defines fixed width file as follows.
> Data with one continuous string having no delimiter for each of the record field. The deciphering of the data fields within the record can only be achieved by cross-referencing a file specifciation/definition that accompany the fixed width file in question.

For example the data file below
```
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
```

May have the following definition/specification file. It is important to notice this package uses 1-based positioning for the string start/end character. This design choice is explained in the [appendix](#app-1based)
```
fname,start,end,decimal
F1,1,10,
F2,17,22,
F3,34,34,
F4,35,40,
```

That produces the csv dataset that looks like the following when parased out
```
F1,F2,F3,F4
0123456789,ghijkl,x,yz0123
0123456789,ghijkl,x,yz0123
0123456789,ghijkl,x,yz0123
0123456789,ghijkl,x,yz0123
0123456789,ghijkl,x,yz0123
```

# Prerequisit
This library does not have non Python core library (3.11) dependency. However, it is also dependent on the Pandas (https://pypi.org/project/pandas/) library for data processing methods using Pandas DataFrame.

Install pandas using
```
pip install pandas numpy
```

# Installation
This package is available from Pypi.org. Install as follows
```
pip install fixedwithfile
```

# Basic Uses
Example uses can be found in the source folder [example\sample.py]

Importing the librar
```
from fwf import FixedWidthFile
```

Building the field specification file in csv
```
fname,start,end,decimal
```

The following table explains the field specification
| Field Name | Purpose |
| ---------- | ------- |
| fname      | The field name of the column extracted in the header |
| start      | The starting character count of the field (1-based) |
| end      | The ending character count of the field (1-based) |
| decimal      | Should the extracted field be a decimal figure, attempt to convert field to numerical value with the decimal piont indicated in this field. For example extract with the field 12345 having the decimal 3 will produce 12.345 |

Back to Python, attaching the field specification to the fixedwidthfile definition
```
fwf = FixedWidthFile(FS)
```


# Dedication

# Appendix
## Why is fixed length file sill favored by mainframe?
<a name="app-fll"/>

## Why does your library use 1 based positioning instead of 0 based?
<a name="app-1based"/>
