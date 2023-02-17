from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pandas as pd

def get_data(region_index):
    # Initializing webdriver
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)



    driver.get('http://vlr.gg/rankings')
    print('Success!', driver.title)
    players = []
    time.sleep(3)
    for k in range(1,11):
        try:
            team = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[4]/div[' + str(region_index) +']/table/tbody/tr['+ str(k) +']/td[2]')
            team.click()
            time.sleep(1)

            for j in range(0,6):
                competitors = driver.find_elements_by_class_name('team-roster-item')
                # try:
                #     player = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[4]/div[2]/div['+ str(j) +']')
                #     player.click()
                # except:
                #     # sometimes the xpath is different depending on the team
                #     player = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[1]/a/div[2]/div['+ str(j) +']')
                #
                #     player.click()
                # print('clicked player')
                competitors[j].click()
                time.sleep(0.5)

                all_button = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/a[4]')
                all_button.click()
                # print('clicked all button')
                time.sleep(0.2)

                username      = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[1]/div[1]/div[2]/div[1]/h1').text
                for i in range(1,10):
                    try:
                        agent         = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[1]/img').get_attribute('src')
                        matches       = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[2]').text
                        rounds        = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[3]').text
                        rating        = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[4]').text
                        acs           = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[5]').text
                        kd            = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[6]').text
                        adr           = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[7]').text
                        kast          = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[8]').text
                        kpr           = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[9]').text
                        apr           = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[10]').text
                        fkpr          = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[11]').text
                        fdpr          = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[12]').text
                        kills         = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[13]').text
                        deaths        = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[14]').text
                        assists       = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[15]').text
                        first_kills   = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[16]').text
                        first_deaths  = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr['+ str(i) +']/td[17]').text

                        # parse the image url to get the agent name
                        agent = agent.split('/')[-1].split('.')[0]

                        players.append({"Username" : username,
                        "Agent" : agent,
                        "Matches" : matches,
                        "Rounds" : rounds,
                        "Rating" : rating,
                        "ACS" : acs,
                        "KD" : kd,
                        "ADR" : adr,
                        "KAST" : kast,
                        "KPR" : kpr,
                        "APR" : apr,
                        "FKPR" : fkpr,
                        "FDPR" : fdpr,
                        "K" : kills,
                        "D" : deaths,
                        "A" : assists,
                        "FK" : first_kills,
                        "FD" : first_deaths,
                        "Region" : region_index})

                        # print('collected data', i)
                    except:
                        # sometimes will parse through coach or player with little/no matches
                        print('No data available')

                # get back to the original page and start the loop again
                print('Collected data on', username)
                time.sleep(0.25)
                driver.back()
                time.sleep(0.25)
                driver.back()
                time.sleep(0.25)
            print('Team data collected. Progress: {}/10'.format(k))
            driver.back()
            time.sleep(1)

        except:
            print('Scraping terminated before reaching 10 teams. Obtained {}/10'.format(k-1))
            break


    time.sleep(5)
    driver.quit()



    return pd.DataFrame(players)
