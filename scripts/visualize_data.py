import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Load JSON data from a file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Plot the number of districts per province
def plot_districts_per_province(integrated_data):
    province_names = []
    district_counts = []
    
    for province in integrated_data:
        province_names.append(province['province_name_en'])
        district_counts.append(len(province['districts']))
    
    plt.figure(figsize=(10, 8))
    sns.barplot(x=district_counts, y=province_names, palette="viridis")
    plt.title('Number of Districts per Province')
    plt.xlabel('Number of Districts')
    plt.ylabel('Provinces')
    plt.tight_layout()
    plt.show()

# Plot a pie chart of subdistricts in selected districts
def plot_subdistrict_distribution(integrated_data, province_name, district_names):
    subdistrict_counts = defaultdict(int)
    
    for province in integrated_data:
        if province['province_name_en'] == province_name:
            for district in province['districts']:
                if district['district_name_en'] in district_names:
                    subdistrict_counts[district['district_name_en']] = len(district['subdistricts'])
            break
    
    plt.figure(figsize=(8, 8))
    plt.pie(subdistrict_counts.values(), labels=subdistrict_counts.keys(), autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title(f'Distribution of Subdistricts in Selected Districts of {province_name}')
    plt.show()

def main():
    # Load integrated data
    integrated_data = load_data('data/integrated_data.json')
    
    # Plot visualizations
    plot_districts_per_province(integrated_data)
    
    # Example: Plot subdistrict distribution for a specific province and a few districts
    plot_subdistrict_distribution(integrated_data, province_name="Bangkok", district_names=["Phra Nakhon", "Dusit"])

if __name__ == "__main__":
    main()
