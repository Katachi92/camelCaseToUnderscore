#!/usr/bin/python3

import sys

def should_preced_with_underscore(string, iter):
    isFirst = iter == 0
    return (not isFirst) and string[iter - 1].islower() and string[iter].isupper()

def underscore(camel_case_string):
    result = ""
    for iter in range(0, len(camel_case_string)):
        print(camel_case_string)
        if should_preced_with_underscore(camel_case_string, iter):
            result = result + "_"
        result = result + camel_case_string[iter].upper()
    return result
        
    return camel_case_string[0]

for arg in sys.argv :
    print("constexpr auto {} = \"{}\"_s;".format(underscore(arg), arg))
