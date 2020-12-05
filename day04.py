#!/usr/bin/env python3
import re

filename = 'input/day04'

passport_fields = [
    'byr', #Birth year
    'iyr', #Issue year
    'eyr', #Expiration year
    'hgt', #Height
    'hcl', #Hair color
    'ecl', #Eye color
    'pid', #Passport ID
    'cid' #Country ID
]
#Sort these for easier comparison later
passport_fields_no_cid = sorted(passport_fields[:-1])
passport_fields = sorted(passport_fields)

passports = []
#Read in the data, parsing to individual passports
with open(filename,'r') as passport_data:
    passport=""
    for line in passport_data:
        line = line.strip()
        if line: #non-blank lines are True
            #append data to current passport
            passport = ' '.join((passport, line))
        else:
            #Blank lines are data breaks, so commit current info
            passport = passport.strip()
            #Convert current info to dictionary
            fields = dict([x.split(':') for x in passport.split(' ')])
            passports.append(fields)
            passport = "" #Reset for next passport

#Part2: validation
def valid_range(field, low, high):
    try:
        field = int(field)
    except:
        return False #if it isn't parsable as an int, it's invalid
    return low <= field <= high

def valid_byr(byr):
    #Four digits, at least 1920, at most 2002.
    return valid_range(byr, 1920, 2002)

def valid_iyr(iyr):
    #Four digits, at least 2010, at most 2020
    return valid_range(iyr, 2010, 2020)

def valid_eyr(eyr):
    #Four digits, at least 2020, at most 2030
    return valid_range(eyr, 2020, 2030)

def valid_hgt(hgt):
    #Number followed by 'cm' or 'in'
    #cm at least 150, at most 193.
    #in at least 59, at most 76.
    if len(hgt) > 2 and hgt[-2:] in ('in', 'cm'):
        num = hgt[:-2]
        unit = hgt[-2:]
    else:
        return False

    if unit == 'cm':
        return valid_range(num, 150, 193)
    else: #inches
        return valid_range(num, 59, 76)

valid_hcl_pattern = re.compile(r'#[0-9a-f]{6}')
def valid_hcl(hcl):
    #a # followed by six characters 0-9, a-f
    return re.fullmatch(valid_hcl_pattern, hcl) != None

valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def valid_ecl(ecl):
    #Must be in the valid list
    return ecl in valid_eye_colors

valid_pid_pattern = re.compile(r'[0-9]{9}')
def valid_pid(pid):
    #Nine digit number, including leading zeroes.
    return re.fullmatch(valid_pid_pattern, pid) != None

validate = {
    'byr': valid_byr,
    'iyr': valid_iyr,
    'eyr': valid_eyr,
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': valid_pid,
    'cid': lambda x: True #Not validated
}

first_valid = 0
second_valid = 0
for passport in passports:
    keys = sorted(passport.keys()) #sort to match order
    if keys == passport_fields or keys == passport_fields_no_cid:
        #Part1: Count the number of passports with valid field config, regardless of values
        first_valid += 1

        #Part2: Cound valid passports, including valid values
        fields_valid = True
        for k in keys:
            #Must pass all validations to be True
            fields_valid = fields_valid and validate[k](passport[k])
        if fields_valid:
            second_valid += 1

print(f'Valid field passports: {first_valid}')
print(f'Valid value passports: {second_valid}')

