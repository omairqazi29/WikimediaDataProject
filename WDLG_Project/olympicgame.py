class OlympicGame(object):
    hostCity = None
    lema = None
    numNations = None
    numAthletes = None
    numEvents = None
    openingDate = None
    closingDate = None
    stadiumName = None
    image = None
    latitude = None
    longitude = None

    def __init__(self, host_city, lema, num_nations, num_athletes, num_events, opening_date, closing_date, stadium):
        self.hostCity = host_city
        self.lema = lema
        self.numNations = num_nations
        self.numAthletes = num_athletes
        self.numEvents = num_events
        self.openingDate = opening_date
        self.closingDate = closing_date
        self.stadium = stadium

    def coordinates(self, longitude, latitude): #longitude E/W, latitude S/N
        self.longitude = longitude
        self.latitude = latitude

    def addmage(self, image):
        self.image = image
