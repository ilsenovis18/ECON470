import chardet

contract_info_path = '/Users/ilsenovis/Documents/GitHub/ECON470/data/input/CPSC_Contract_Info_2015_01.csv'

with open(contract_info_path, 'rb') as f:
    result = chardet.detect(f.read())

print(result)
