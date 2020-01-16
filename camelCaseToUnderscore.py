#!/usr/bin/python3

import sys
import fileinput

def should_preced_with_underscore(string, iter):
    isFirst = iter == 0
    return (not isFirst) and string[iter - 1].islower() and string[iter].isupper()

def underscore(camel_case_string):
    result = ""
    for iter in range(0, len(camel_case_string)):
        if should_preced_with_underscore(camel_case_string, iter):
            result = result + "_"
        result = result + camel_case_string[iter].upper()
    return result
        
    return camel_case_string[0]

if len(sys.argv) > 1 :
    text_values = sys.argv[1:]
else :
    text_values = fileinput.input();

for arg in text_values :
    sys.stdout.write("constexpr auto {} = \"{}\"_s;\n".format(underscore(arg).strip(), arg.strip()))
