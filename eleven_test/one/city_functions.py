
def get_city_name(cityname, countyname, population=""):
    if population:
        resultname = cityname.title()+", "+countyname.title()+" - population "+population;
    else:
        resultname = cityname.title() + " " + countyname.title();
    return resultname;

