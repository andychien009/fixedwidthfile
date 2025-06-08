# Overview
fixedlengthfile is a Python library that assists with work for any fixed length file.

While CSV file format is popular in the data analytics, much of the main frame input/output file remain to be fixed length file (see [appendix](#app-fll) to gain an understanding why). 

This library defines fixed length file as follows.
> data with 1 continuous string having no delimiter for each of the record, the deciphering of the data within the file need to be referenced using the length (and/or data type) definition file is supplied that is at match with the fixed length file

For example the file below
```
```

May have the definition file
```
```

That produces the dataset that looks like the following when parased out
```
```

# Prerequisit
This library does not have non Python core library (3.11) dependency. However, it is optionally dependant on the Pandas (https://pypi.org/project/pandas/) library should developer utilize functions that returns Pandas Dataframe.

# Installation

# Basic Uses


# Dedication

# Appendix
## Why is fixed length file sill favored by mainframe?
<a name="app-fll"/>

## Why does your library use 1 based positioning instead of 0 based?
<a name="app-fll"/>
