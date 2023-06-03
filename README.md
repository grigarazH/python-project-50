# Difference Generator:
[![Actions Status](https://github.com/grigarazH/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/grigarazH/python-project-50/actions)
[![Python CI](https://github.com/grigarazH/python-project-50/actions/workflows/py-ci.yml/badge.svg)](https://github.com/grigarazH/python-project-50/actions/workflows/py-ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/d2783c38770166bfa05f/maintainability)](https://codeclimate.com/github/grigarazH/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d2783c38770166bfa05f/test_coverage)](https://codeclimate.com/github/grigarazH/python-project-50/test_coverage)

This program generates differences between two JSON or YAML files.
3 formats of output are supported: stylish, plain and JSON.


## Requirements

* Python 3.11+
* Poetry 1.4.1+

## Installation

1. Go to source directory
2. Run
   
```
make install
make build
make package-install
```


## Using
To view help, use the follwoing command:
```
gendiff -h
```
To use the program, use the following command:

```
gendiff [-f FORMAT] file1_path file2_path
```

where `FORMAT` is output format, 
`file1_path`, `file2_path` are paths to files.



## Preview

### Flat JSON
[![asciicast](https://asciinema.org/a/VOKSoqxp2aWsDiRtQyHKPLY7D.svg)](https://asciinema.org/a/VOKSoqxp2aWsDiRtQyHKPLY7D)

### Flat YAML
[![asciicast](https://asciinema.org/a/QkNmSXxc4YLvSO8IrSRCybt5D.svg)](https://asciinema.org/a/QkNmSXxc4YLvSO8IrSRCybt5D)

### Nested stylish
[![asciicast](https://asciinema.org/a/pR2m1h2Ge7E2xj2LYpJ0yWLdB.svg)](https://asciinema.org/a/pR2m1h2Ge7E2xj2LYpJ0yWLdB)

### Nested plain
[![asciicast](https://asciinema.org/a/SIAtYwcc4E8RPONM5i0Y8yXYk.svg)](https://asciinema.org/a/SIAtYwcc4E8RPONM5i0Y8yXYk)

### Nested JSON
[![asciicast](https://asciinema.org/a/GsbCzmDVKuEcUhobQOcEw2g4I.svg)](https://asciinema.org/a/GsbCzmDVKuEcUhobQOcEw2g4I)