import sys
import os

import projecteuler.pe_5_smallest_multiple
import projecteuler.pe_6_sum_square_difference
import projecteuler.pe_8_largest_product_in_a_series
import projecteuler.pe_9_special_pythagorean_triplet
import projecteuler.pe_10_summation_of_primes
import projecteuler.pe_11_largest_product_in_grid
import projecteuler.pe_12_highly_divisible_triangular_number
import projecteuler.pe_13_large_sum
import projecteuler.pe_14_longest_collatz_sequence
import projecteuler.pe_16_power_digit_sum
import projecteuler.pe_17_number_letter_counts
#import projecteuler.pe_18_maximum_path_sum_I
import projecteuler.pe_19_counting_sundays
import projecteuler.pe_20_factorial_digit_sum
import projecteuler.pe_21_amicable_numbers
import projecteuler.pe_22_names_scores
import projecteuler.pe_23_non_abundant_sums
import projecteuler.pe_24_lexicographic_permutations
import projecteuler.pe_25_1000_digit_fibonacci_number
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