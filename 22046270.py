import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter


file_path = 'world_food_production.csv'
data = pd.read_csv(file_path)


# -------------------- 1st VISUALIZATION -------------------

food_types = [
    'Maize Production (tonnes)',
    'Rice  Production ( tonnes)',
    'Wheat Production (tonnes)',
    'Tomatoes Production (tonnes)',
    'Coffee, green Production ( tonnes)',
    'Meat, chicken  Production (tonnes)',
    'Bananas  Production ( tonnes)',
    'Apples Production (tonnes)'
]

data['Total Production'] = data[food_types].sum(axis=1)
best_food_type = data.loc[data['Total Production'].idxmax(), 'Entity']
def thousands_formatter(x, pos):
    return f'{int(x / 1000)}K'
plt.figure(figsize=(12, 8))
ax = sns.barplot(data=data, x='Entity', y='Total Production', hue='Entity', dodge=False)
plt.title('Total Production of Selected Food Types across Entities')
plt.xlabel('Food Types')
plt.ylabel('Total Production (in thousands)')
n = 10  
for ind, label in enumerate(ax.get_xticklabels()):
    if ind % n == 0:  
        label.set_visible(True)
    else:
        label.set_visible(False)

plt.xticks(rotation=90)
plt.legend().remove() 
ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))  
plt.tight_layout()


# Save the plot as a PNG file
plt.savefig("22046270_1.png", dpi=300)

# -------------------- 2nd VISUALIZATION -------------------


data['Total Production'] = data.iloc[:, 2:].sum(axis=1) / 1000 
global_production = data.groupby('Year')['Total Production'].sum().reset_index()
plt.figure(figsize=(12, 8))
plt.plot(global_production['Year'], global_production['Total Production'], marker='o', color='blue')
plt.title('Global Food Production Trends')
plt.xlabel('Year')
plt.ylabel('Production Quantity (Kilotons)') 
plt.grid(True)


# Save the plot as a PNG file
plt.savefig("22046270_2.png", dpi=300)

# -------------------- 3rd VISUALIZATION -------------------


selected_countries = ['China', 'India', 'United States', 'Brazil', 'Russia', 'Asia']
selected_food_types = [
    'Maize Production (tonnes)',
    'Rice  Production ( tonnes)',
    'Wheat Production (tonnes)',
    'Tomatoes Production (tonnes)',
    'Coffee, green Production ( tonnes)'
]

filtered_data = data[data['Entity'].isin(selected_countries)]
filtered_data = filtered_data[['Entity'] + selected_food_types]
melted_data = pd.melt(filtered_data, id_vars='Entity', value_vars=selected_food_types,
                      var_name='Food Type', value_name='Production (tonnes)')
melted_data['Production (tonnes)'] = melted_data['Production (tonnes)'] / 1000
plt.figure(figsize=(12, 8))
sns.barplot(data=melted_data, x='Entity', y='Production (tonnes)', hue='Food Type', dodge=True)
plt.title('Comparison of Food Production in Selected Countries')
plt.xlabel('Countries')
plt.ylabel('Production Quantity (Kilotons)')
plt.xticks(rotation=45)
plt.legend(title='Food Type', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.gca().set_yticklabels(['{:.0f}K'.format(y) for y in plt.gca().get_yticks()])


# Save the plot as a PNG file
plt.savefig("22046270_3.png", dpi=300)
# -------------------- 4th VISUALIZATION -------------------


selected_year = 2020
year_data = data[data['Year'] == selected_year]
continents = {
    'Africa': ['Algeria', 'Nigeria', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['Germany', 'France', 'United Kingdom'],
    'North America': ['United States', 'Canada', 'Mexico'],
    'Oceania': ['Australia', 'New Zealand'],
    'South America': ['Brazil', 'Argentina', 'Chile']
}
food_types = [
    'Maize Production (tonnes)',
    'Rice  Production ( tonnes)',
    'Wheat Production (tonnes)',
    'Tomatoes Production (tonnes)',
    'Coffee, green Production ( tonnes)',
    'Meat, chicken  Production (tonnes)',
    'Bananas  Production ( tonnes)',
    'Apples Production (tonnes)'
]

continent_data = pd.DataFrame()
for continent, countries in continents.items():
    continent_df = year_data[year_data['Entity'].isin(countries)]
    continent_df = continent_df[food_types].sum().reset_index()
    continent_df.columns = ['Food Type', 'Total Production']
    continent_df['Continent'] = continent
    continent_data = pd.concat([continent_data, continent_df], ignore_index=True)

def thousands_formatter(x, pos):
    return f'{int(x / 1000)}K'
plt.figure(figsize=(12, 8))
ax = sns.barplot(data=continent_data, x='Continent', y='Total Production', hue='Food Type', dodge=True)
plt.title(f'Total Production of Selected Food Types by Continent in {selected_year}')
plt.xlabel('Continent')
plt.ylabel('Total Production (in thousands)')
plt.legend(title='Food Type', loc='upper right')
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# Save the plot as a PNG file
plt.savefig("22046270_4.png", dpi=300)