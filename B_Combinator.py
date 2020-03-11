# coding: utf-8
# -*- coding: utf-8 -*-


""" Combining the scraping results """
from datetime import datetime
import pickle
import Scrape.mylib.Constantes as CONST



ticketMa = pickle.load(open(CONST.PICKLE_FILE+'ticket.pickle','rb'))
ifCinema = pickle.load(open(CONST.PICKLE_FILE+'if_cinema.pickle','rb'))
ifConference = pickle.load(open(CONST.PICKLE_FILE+'if_conference.pickle','rb'))
ifSpectacle = pickle.load(open(CONST.PICKLE_FILE+'if_spectacle.pickle','rb'))
cineAtlas = pickle.load(open(CONST.PICKLE_FILE+'cinealtas.pickle','rb'))
#cervantes = pickle.load(open(CONST.PICKLE_FILE+'cervantes.pickle','rb'))
#tnm5 = pickle.load(open(CONST.PICKLE_FILE+'tnm5.pickle','rb'))

comb =  cineAtlas  +  ifCinema + ifSpectacle + ifConference + ticketMa

print('Combined')

""" Convert the file in Pandas """
import pandas as pd

df = pd.DataFrame(comb,columns=['titre','date','heure','image','lien','description','lieu'])

""" Sort the pandas following the date """

##need to convert first the date intodatetime
df['date'] = df['date'].apply(lambda date: datetime.strptime(date, "%d.%m.%Y"))
##Sort them
df.sort_values(by='date',inplace=True)
##Then reconvert them
df['date'] = df['date'].apply(lambda date: datetime.strftime(date, "%d.%m.%Y"))

# For testing the sorting
df.to_excel(CONST.JSON_FILE+"tableau_sorting.xlsx")

print('Generate DataFrame')

""" exclude the events that come before the actual day & later than a month """
# getting the actual date
from datetime import datetime
t = datetime.now()


#getting the date one month later
from datetime import timedelta
m_l = t + timedelta(days=30)


##need to convert first the date into datetime
df['date'] = df['date'].apply(lambda date: datetime.strptime(date, "%d.%m.%Y"))

df = df.loc[(df['date'] >= t) & (df['date'] <= m_l)]

print("****** *****")
df.to_excel(CONST.JSON_FILE+"tableau_after_today.xlsx")

#
# """ Generate JSON file """
# df.to_json(CONST.JSON_FILE+"whatsin.json",orient="records")

# For testing the date
df.to_excel(CONST.JSON_FILE+"tableau_dates.xlsx")

print("JSON generated")
