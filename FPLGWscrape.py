import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

team_id = '1026982' ##insert your team id

driver = webdriver.Chrome()
url = f'https://fantasy.premierleague.com/entry/{team_id}/history'

driver.get(url)
driver.implicitly_wait(3)


tdata = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr')

gameweek = []
gw_points = []
transfers = []
transfercost = []
overall_points = []
rank = []
value = []

manager = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/h2')

gaffer = []

for name in manager:
    gaffer.append(name.text)

for row in tdata:
    GW = row.find_element(By.XPATH,'./td[1]').text
    GWP = row.find_element(By.XPATH,'./td[2]').text
    Transfers = row.find_element(By.XPATH,'./td[5]').text
    Tcost = row.find_element(By.XPATH,'./td[6]').text
    OVRP = row.find_element(By.XPATH,'./td[7]').text
    OR = row.find_element(By.XPATH,'./td[8]').text
    Value = row.find_element(By.XPATH,'./td[9]').text
    gameweek.append(GW)
    gw_points.append(GWP)
    transfers.append(Transfers)
    transfercost.append(Tcost)
    overall_points.append(OVRP)
    rank.append(OR)
    value.append(Value)

driver.quit()

gw_history = {'gameweek': gameweek, 'gwpoints': gw_points, 
'transfers': transfers, 'trasnfercost':transfercost, 'pointstotal':overall_points, 'or':rank, 'teamvalue': value}


history_df = pd.DataFrame.from_dict(gw_history)
history_df.to_csv(f'gw_history_{gaffer}.csv', index=False)




