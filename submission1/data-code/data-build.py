import pandas as pd

# Construct file paths dynamically
contract_info_path = '/Users/ilsenovis/Documents/GitHub/ECON470/data/input/CPSC_Contract_Info_2015_01.csv'
enroll_info_path = '/Users/ilsenovis/Documents/GitHub/ECON470/data/input/CPSC_Enrollment_Info_2015_01.csv'
county_sa_info_path = '/Users/ilsenovis/Documents/GitHub/ECON470/data/input/MA_Cnty_SA_2015_01.csv'

# Read in your datasets using the dynamically constructed paths
contract_info = pd.read_csv(contract_info_path, encoding='ISO-8859-1')
enroll_info = pd.read_csv(enroll_info_path, encoding='ISO-8859-1')
county_sa_info = pd.read_csv(county_sa_info_path, encoding='ISO-8859-1')

print(enroll_info.columns)
print(county_sa_info.columns)

# Rename 'Contract Number' to 'Contract ID' in enroll_info
enroll_info.rename(columns={'Contract Number': 'Contract ID'}, inplace=True)

print(enroll_info.columns)
print(county_sa_info.columns)

# Now you can perform the merge with 'Contract ID'
merged_enrollment_data = pd.merge(enroll_info, county_sa_info, on='Contract ID', how='inner')

# View the first few rows of the merged data
print(merged_enrollment_data.head())