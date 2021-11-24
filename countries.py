'''import pygal
world=pygal.maps.world.World()
world.title='COUNTRIES'
world.add('Random Data',{'aq':10,'cd':30,'de':40,'eg':50,'ga':45,'hk':23,'in':70,'jp':54,'nz':41,'kz':32,'us':66})
world.render_to_file('abc.svg')'''
# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.World()

# set the title of the map
worldmap.title = 'Countries'

# adding the countries
worldmap.add('Random Data', {
		'aq' : 10,
		'cd' : 30,
		'de' : 40,
		'eg' : 50,
		'ga' : 45,
		'hk' : 23,
		'in' : 70,
		'jp' : 54,
		'nz' : 41,
		'kz' : 32,
		'us' : 66
})

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")
