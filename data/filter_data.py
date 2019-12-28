import pandas as pd

main_data = pd.read_csv('whs_risk_full.csv', encoding="latin")
# id_nos = [788, 733, 712, 394, 825, 1533, 809, 963, 97, 1240, 95, 125, 978, 570]
id_nos = [809, 963, 97, 1240, 95, 125, 978, 570]

filter_data = main_data[main_data.id_no.isin(id_nos)]
filter_data.to_csv('filtered_whs.csv')
