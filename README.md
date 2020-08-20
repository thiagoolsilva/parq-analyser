[![CI status](https://github.com/thiagoolsilva/parq-analyser/workflows/CI/badge.svg)](https://github.com/thiagoolsilva/parq-analyser/actions?queryworkflow%3ACI+event%3Apush+branch%3Amaster)
[![License Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=true)](http://www.apache.org/licenses/LICENSE-2.0)


The project is related to provided a console program made in python to helps data science to analyser parquet files using the must commons functions provided by [pandas](https://pandas.pydata.org/) framework.



Check out below the overview of available functions available on the program:

```
$ parq-analyser -h

usage: parq-analyser [-h] [-P --path] [-H --head] [-T --tail] [-D --drop] [-C] [-verbose] [-v]

Process parquet file data

optional arguments:
  -h, --help  show this help message and exit
  -P --path   the path of parquet file
  -H --head   the numbers of the first rows to be returned. The default value is 5 and the maximum accepted is 199 and this is the default operation selected by program if
              no one is provided.
  -T --tail   the numbers of the last rows to be returned. The maximum number accepted is 199
  -D --drop   the numbers of the first rows to be dropped. The maximum number accepted is 199
  -C          Get total rows
  -verbose    enable verbose mode
  -v          shows the app version

Enjoy the program!
```

# Pre-Installation Requirements:

To run and install the app you must have the following specifications:

```
python >= 3.2
pip >= 20.1.1
pandas==1.0.5
tabulate==0.8.7
pyarrow
```

# QuickStart

## Download and usage

First of all you need to download a stable releases of the standalone parq-analyser binaries [here](https://github.com/thiagoolsilva/parq-analyser/releases).
Finally you can choose two options to run the program. 

### Install the program using whl file:

To install it you must use the following command.

```
pip install parse_parquet-X.X.X-py3-none-any.whl 
```

Check if no error happens in the terminal and type `parq-analyser -h` on it to get the program help information.

### Install the program in developer mode:

To do it you must type the command `pip install --editable .` to install it on your env python dependencies in developer mode. After that you can develop or run the app on terminal.

Ps: This approach will remove the parq-analyser from the path after it is closed.

## Using the library

After install it you can type  `parq-analyser -h` to get all information about the program.


### Reading the first N rows:

Type the command `parq-analyser -P yourParquetFile.parquet -H 3` to get the first N rows of parquet.

```
+----+---------+--------+
|    | Names   |   Ages |
|----+---------+--------|
|  0 | Thiago  |     34 |
|  1 | Lopes   |     33 |
|  2 | Silva   |     32 |
+----+---------+--------+
```

Ps: The maximum value accepted is 199

### Reading the last N rows:

Type the command `parq-analyser -P yourParquetFile.parquet -P 1` to get the last N rows of parquet.

```
+----+---------+--------+
|    | Names   |   Ages |
|----+---------+--------|
|  2 | Silva   |     32 |
+----+---------+--------+
```

Ps: The maximum value accepted is 199

### Drop the first N rows:

You can combine this command getting the first or last rows. In order to exemplify you can run the command 
`parq-analyser -D 1 -P test.paquet -T 2` to drop the first row and get the next ones.


```
+----+---------+--------+
|    | Names   |   Ages |
|----+---------+--------|
|  1 | Lopes   |     33 |
|  2 | Silva   |     32 |
+----+---------+--------+
```

Ps: The maximum value accepted is 199

### Gets the size of Paquet:

Type the command `parq-analyser -P yourParquetFile.parquet -C` to get the total rows of parquet file.

```
Total Rows: 2
```

# Features

This section is related to the features/bug fixes of project.

## Do you want to contribute?

I'd love if you contribute with the upcoming features or bug fixes. Go ahead and read the [CONTRIBUTING](CONTRIBUTING.md) file.

## Upcoming features

You can check it out for new features on [github](https://github.com/thiagoolsilva/parq-analyser/issues?q=is%3Aopen+is%3Aissue+label%3Aupcoming).

# Author

<img src="misc/myAvatar.png" width="40"/>

Follow me

[![Follow me](https://img.shields.io/badge/Medium-thiagoolsilva-yellowgreen)](https://medium.com/@thiagolopessilva)
[![Linkedin](https://img.shields.io/badge/Linkedin-thiagoolsilva-blue)](https://www.linkedin.com/in/thiago-lopes-silva-2b943a25/)
[![Twitter](https://img.shields.io/twitter/follow/thiagoolsilva?style=social)](https://twitter.com/thiagoolsilva)   

## License
```
Copyright (c) 2020  Thiago Lopes da Silva

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
