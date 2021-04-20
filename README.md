# Project Euler

This repository contains my solutions to 
[Project Euler](https://projecteuler.net/) problems.

The solutions are implemented in Python and also in Rust for some problems.

## Getting started

Use the `run.sh` script to compute the solution of a problem.

The following command will compute the solution for the n th problem:

```
./run.sh n
```

By default, the python solution is used. To run the Rust implementation,
use the command:

```
./run.sh -r n
```

Note: For `n = 0` the script will launch the tests of the library. These
tests can also be launched using the option `-t` or `--test`.

## Bench

A bench option has been added to the `run.sh` script. The bench will
measure the time needed to compute the solutions to the problems and
verify that the results are correct. The results displayed are time
comparison between Python and Rust implementation.

To run the bench and see the result, use the command:

```
./run.sh -b
```

There also two other options for the bench:

- `-d` or `--bench-display` or that will only display the results if the
bench has already been run.
- `-c` or `--bench-clean` to remove all the results of the bench.

## Repository organisation

- `src/problems`: contains all the files to resolve the problems. Every
solution is contained in a folder, for example, the solution to problem 10
is stored in the solder `src/problems/1-49/10`. These folders contain a
python script and a `rust` folder with the Rust implementation.
- `src/lib`: contains different functions that are used to resolve the
problems.
- `src/bench`: The scripts to run the bench. The folder contains also all the solutions to the Euler project found.
