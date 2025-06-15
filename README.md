# Overview
fixedlengthfile is a Python library that assists with work for any fixed length file.

While CSV file format is popular in the data analytics, much of the main frame input/output file remain to be fixed length file (see [appendix](#app-fll) to gain an understanding why). 

This library defines fixed length file as follows.
> Data with one continuous string having no delimiter for each of the record. The deciphering of the data fields within the record can be achieved by referenced a file specifciation/definition that corresponds to the fixed length file.

For example the file below
```
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz
```

May have the definition/specification file. It is important to notice this package uses 1-based positioning for the string start/end character. This design choice is explained in the [appendix](#app-1based)
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
This library does not have non Python core library (3.11) dependency. However, it is optionally dependant on the Pandas (https://pypi.org/project/pandas/) library should developer utilize functions that returns Pandas Dataframe.

Install pandas using

```
pip install pandas numpy
```

# Installation

# Basic Uses


# Dedication

# Appendix
## Why is fixed length file sill favored by mainframe?
<a name="app-fll"/>

## Why does your library use 1 based positioning instead of 0 based?
<a name="app-1based"/>
