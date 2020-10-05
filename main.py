import sys
import os

import projecteuler.pe_5_smallest_multiple
import projecteuler.pe_6_sum_square_difference
import projecteuler.pe_8_largest_product_in_a_series
import projecteuler.pe_9_special_pythagorean_triplet
import pythonchallenge.pythonchallenge
import sololearn.easy
import sololearn.medium
import sololearn.hard


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} module [difficulty [challenge [*args]]]".format(sys.argv[0]))
        print("  - Module can be one of: {}".format(", ".join([[folder for folder in d if folder[0] != '.'] for p,d,f in os.walk(os.path.curdir) if p == '.'][0])))
        print("  - Difficulty can be one of: {}".format(", ".join([list(map(lambda x: x.replace(".py",""), f)) for p,d,f in os.walk(os.path.join(os.path.curdir,'sololearn')) if p == './sololearn'][0])))
        sys.exit(1)
    else:
        if sys.argv[1] == "pythonchallenge":
            pythonchallenge.pythonchallenge.main()
        else:
            try:
                getattr(sys.modules[sys.argv[1]+"."+sys.argv[2]], sys.argv[3])()
            except AttributeError:
                print('Module {}, difficulty {} has no challenge {}.')
                print('Available ones for {} {} are: {}')