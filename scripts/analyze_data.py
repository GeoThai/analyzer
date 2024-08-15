import json
from collections import defaultdict

# Load JSON data from files
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Analyze the number of districts per province
def analyze_districts_per_province(districts, provinces):
    district_count = defaultdict(int)
    
    for district in districts:
        province_id = district['province_id']
        district_count[province_id] += 1
    
    province_district_count = {province['province_name_en']: district_count[province['province_id']] for province in provinces}
    return province_district_count

# Analyze the number of subdistricts per district
def analyze_subdistricts_per_district(subdistricts, districts):
    subdistrict_count = defaultdict(int)
    
    for subdistrict in subdistricts:
        district_id = subdistrict['district_id']
        subdistrict_count[district_id] += 1
    
    district_subdistrict_count = {district['district_name_en']: subdistrict_count[district['district_id']] for district in districts}
    return district_subdistrict_count

# Find the province with the most districts
def find_province_with_most_districts(province_district_count):
    return max(province_district_count, key=province_district_count.get)

# Find the district with the most subdistricts
def find_district_with_most_subdistricts(district_subdistrict_count):
    return max(district_subdistrict_count, key=district_subdistrict_count.get)

def main():
    # Load data
    districts = load_data('data/districts.json')
    provinces = load_data('data/provinces.json')
    subdistricts = load_data('data/subdistricts.json')
    
    # Analyze data
    province_district_count = analyze_districts_per_province(districts, provinces)
    district_subdistrict_count = analyze_subdistricts_per_district(subdistricts, districts)
    
    # Find key insights
    province_with_most_districts = find_province_with_most_districts(province_district_count)
    district_with_most_subdistricts = find_district_with_most_subdistricts(district_subdistrict_count)
    
    # Output results
    print("Number of Districts per Province:")
    for province, count in province_district_count.items():
        print(f"{province}: {count}")
    
    print("\nNumber of Subdistricts per District:")
    for district, count in district_subdistrict_count.items():
        print(f"{district}: {count}")
    
    print(f"\nProvince with the most districts: {province_with_most_districts} ({province_district_count[province_with_most_districts]} districts)")
    print(f"District with the most subdistricts: {district_with_most_subdistricts} ({district_subdistrict_count[district_with_most_subdistricts]} subdistricts)")

if __name__ == "__main__":
    main()
