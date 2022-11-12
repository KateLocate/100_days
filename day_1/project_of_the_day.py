# https://replit.com/@appbrewery/band-name-generator-end

GREETING = 'Welcome to the Band Name Generator.'
ASK_CITY = 'What`s the name of the city you grew up in?'
ASK_PET_NAME = 'What`s your pet`s name?'
NAME_COMPONENTS = (ASK_CITY, ASK_PET_NAME)
TELL_BAND_NAME = 'Your band name could be'
SPACE = ' '

print(GREETING)

band_name = ''
for component in NAME_COMPONENTS:
    band_name += input(component + '\n')
    band_name += SPACE
band_name.rstrip(SPACE)

print(TELL_BAND_NAME, band_name)
