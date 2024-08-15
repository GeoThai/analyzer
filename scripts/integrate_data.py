import json

# Load JSON data from files
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Integrate data by combining provinces, districts, and subdistricts
def integrate_data(provinces, districts, subdistricts):
    integrated_data = []

    # Create a lookup for districts and subdistricts by province and district IDs
    district_lookup = {}
    for district in districts:
        province_id = district['province_id']
        if province_id not in district_lookup:
            district_lookup[province_id] = []
        district_lookup[province_id].append(district)

    subdistrict_lookup = {}
    for subdistrict in subdistricts:
        district_id = subdistrict['district_id']
        if district_id not in subdistrict_lookup:
            subdistrict_lookup[district_id] = []
        subdistrict_lookup[district_id].append(subdistrict)

    # Integrate data
    for province in provinces:
        province_id = province['province_id']
        province_data = {
            "province_id": province_id,
            "province_name_en": province["province_name_en"],
            "province_name_th": province["province_name_th"],
            "districts": []
        }

        if province_id in district_lookup:
            for district in district_lookup[province_id]:
                district_id = district['district_id']
                district_data = {
                    "district_id": district_id,
                    "district_name_en": district["district_name_en"],
                    "district_name_th": district["district_name_th"],
                    "postal_code": district["postal_code"],
                    "subdistricts": []
                }

                if district_id in subdistrict_lookup:
                    district_data["subdistricts"] = subdistrict_lookup[district_id]

                province_data["districts"].append(district_data)

        integrated_data.append(province_data)

    return integrated_data

# Save the integrated data to a JSON file
def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # Load data
    provinces = load_data('data/provinces.json')
    districts = load_data('data/districts.json')
    subdistricts = load_data('data/subdistricts.json')
    
    # Integrate data
    integrated_data = integrate_data(provinces, districts, subdistricts)
    
    # Save integrated data
    save_data(integrated_data, 'data/integrated_data.json')
    
    print("Data integration complete. Integrated data saved to 'data/integrated_data.json'.")

if __name__ == "__main__":
    main()
