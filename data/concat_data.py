import pandas as pd
import json

main_data = pd.read_csv('WHS_2018_med_lecz_serial.csv', encoding="latin")
flood_data = pd.read_json('flood-data.json', orient='records')
erosion_data = pd.read_json('erosion-data.json', orient='records')

# flood_data_high = flood_data.loc[df['scenario'] == 'High-End']
# erosion_data_high = erosion_data.loc[df['scenario'] == 'High-End']

years = [2020, 2030, 2050, 2100]
scenarios = ["RCP2.6", "RCP4.5", "RCP8.5", "High-End"]
for year in years:
  for scenario in scenarios:
    filtered_flood_data = flood_data.loc[(
        flood_data['year'] == year) & (flood_data['scenario'] == scenario)][['id_no', 'index']].rename({'index': str(year) + '_' + scenario + '_flood'}, axis=1)
    main_data = pd.merge(main_data, filtered_flood_data, left_on='id_no', right_on='id_no')
    filtered_erosion_data = erosion_data.loc[(
        erosion_data['year'] == year) & (erosion_data['scenario'] == scenario)][['id_no', 'index']].rename({'index': str(year) + '_' + scenario + '_erosion'}, axis=1)
    main_data = pd.merge(main_data, filtered_erosion_data, left_on='id_no', right_on='id_no')

main_data.to_csv('output.csv')


