#!/bin/python3

import sys

def read_sol(path_sol):
    """
    Read the file and return a tab containing the solution
    for each problem
    """
    tab  = {}
    index = 1

    f_sol      = open(path_sol, "r")
    list_lines = f_sol.readlines()

    for line in list_lines:
        if line != "\n":
            tab[index] = int(line)
        index += 1

    return tab

def get_ind(version):
    """
    Return 0 if it's the python version
    1 for rust
    2 otherwise
    """
    if version == "Python":
        return 0
    elif version == "Rust":
        return 1
    else:
        return 2

def get_res(path_sol, path_res):
    """
    Return Tab containing the time to compute in python and in rust
    -1 if the problem was not computed
    """
    tab_sol = read_sol(path_sol)

    f_res = open(path_res, "r")

    results = {}

    for line_file in f_res:
        res = []
        for el in line_file.split(" "):
            res.append(el)

        version = res[0]
        nb_pb   = int(res[1])
        result  = int(res[-1])
        time    = float(res[3][1:]) # Escaping (

        # Verifying that the correct result was found
        if (tab_sol[nb_pb] != result):
            print("The {} version for the problem {} does not find the correct result!".format(version, nb_pb))
            print("\t {} found but {} was expected...".format(result, tab_sol[nb_pb]))
            exit(1)

        if not nb_pb in results:
            results[nb_pb] = [-1, -1]

        results[nb_pb][get_ind(version)] = time

    return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Missing parameters...")
        exit(1)

    path_sol = sys.argv[1]
    path_res = sys.argv[2]

    results = get_res(path_sol, path_res)

    # Doing stats with the results
    nb_rust         = 0
    nb_python       = 0
    sum_time_python = 0
    sum_time_rust   = 0
    min_python_time = -1
    min_python_nb   = -1

    for (nb_pb, times) in results.items():
        if times[0] != -1:
            sum_time_python += times[0]
            nb_python       += 1

        if times[1] != -1:
            sum_time_rust += times[1]
            nb_rust       += 1

        if times[0] != -1 and times[1] != -1:
            percent_decrease = 100.0 * (times[0] - times[1]) / times[0]
            print("Problem {} : {}s (Python), {}s (Rust), {}%"\
                    .format(nb_pb, times[0], times[1], percent_decrease))

    # Display results
    print("{} problems resolved correctly".format(len(results)))
    print("")
    print("-----------------------------------------------------")
    print("|                   |     Python    |      Rust     |")
    print("| Nb pbs resolved   |  {:>10}   |  {:>10}   |".format(nb_python, nb_rust))
    print("| Total time in s   | {:12.6f}  | {:12.6f}  |"\
                    .format(sum_time_python, sum_time_rust))
    print("| Average time in s | {:12.6f}  | {:12.6f}  |"\
            .format(sum_time_python/nb_python, sum_time_rust/nb_rust))
    print("-----------------------------------------------------")
