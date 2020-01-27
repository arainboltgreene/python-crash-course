# 8-6 City Names:
#print("\n Try It Yourself section")

#def city_country(city_name, country_name):
#    place = city_name + ' ' + country_name
#    return place.title()

#citycountry = get_formatted_name('Santiago, Chile')
# citycountry = get_formatted_name('Puente Alto, Chile')
# citycountry = get_formatted_name('Antofagasta, Chile')
#print(citycountry)

# 8-7 Album
def make_album(artist_name, album_title):
    album1 = {'name': artist_name, 'title': album_title}
    return album1

album = make_album('jimi hendrix', 'axis of love')
print(album)