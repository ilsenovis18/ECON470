import pandas as pd
import os

# Set local "month lists" to identify different files relevant for each year
monthlist_2006 = ["10", "11", "12"]
monthlist_2007 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2008 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2009 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2010 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2011 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2012 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2013 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2014 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthlist_2015 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

# Map each year to the corresponding monthlist
month_lists = {
    2006: monthlist_2006,
    2007: monthlist_2007,
    2008: monthlist_2008,
    2009: monthlist_2009,
    2010: monthlist_2010,
    2011: monthlist_2011,
    2012: monthlist_2012,
    2013: monthlist_2013,
    2014: monthlist_2014,
    2015: monthlist_2015
}

# Initialize the final dataframe for all years
contract_service_area = pd.DataFrame()

# Loop over each year and process the corresponding data
for year in range(2006, 2016):
    monthlist = month_lists[year]
    service_year = pd.DataFrame()

    for month in monthlist:
        ma_path = f"data/input/MA_Cnty_SA_2015_01.csv"
        
        # Read in the service area data for the given month
        service_area = pd.read_csv(
            ma_path,
            skiprows=1,
            names=["contractid", "org_name", "org_type", "plan_type", "partial", "eghp",
                   "ssa", "fips", "county", "state", "notes"],
            dtype={
                "contractid": str,
                "org_name": str,
                "org_type": str,
                "plan_type": str,
                "partial": "boolean",
                "eghp": str,
                "ssa": float,
                "fips": float,
                "county": str,
                "notes": str
            },
            na_values='*'
        )
        
        # Add the year and month columns
        service_area['month'] = month
        service_area['year'] = year
        
        # Append to the service_year dataframe
        service_year = pd.concat([service_year, service_area], ignore_index=True)
    
    # Fill missing FIPS codes by state and county
    service_year['fips'] = service_year.groupby(['state', 'county'])['fips'].apply(lambda x: x.ffill().bfill())
    
    # Fill missing plan_type, partial, eghp, org_type, and org_name by contractid
    service_year[['plan_type', 'partial', 'eghp', 'org_type', 'org_name']] = service_year.groupby('contractid')[['plan_type', 'partial', 'eghp', 'org_type', 'org_name']].apply(lambda group: group.ffill().bfill())
    
    # Collapse to yearly data by filtering rows where id_count is 1
    service_year['id_count'] = service_year.groupby(['contractid', 'fips']).cumcount() + 1
    service_year = service_year[service_year['id_count'] == 1]
    service_year = service_year.drop(columns=['id_count', 'month'])
    
    # Add to the final contract_service_area dataframe
    contract_service_area = pd.concat([contract_service_area, service_year], ignore_index=True)

# Save the final data to a .rds file (Note: Python uses .pkl for serialized objects)
contract_service_area.to_pickle("data/output/contract_service_area.pkl")