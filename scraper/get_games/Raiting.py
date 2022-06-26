import props
from selenium import webdriver


def get_raitings(league_path, driver):
    driver.get(league_path + props.table)
    teams_div = driver.find_elements_by_class_name('tableCellParticipant__name')
    driver.implicitly_wait(10)
    for i in range(len(teams_div)):
        score = len(teams_div)-i
        if teams_div[i].text in props.top_teams:
            score += 5
        props.raitings[teams_div[i].text] = score
    print(league_path, " is done!")
