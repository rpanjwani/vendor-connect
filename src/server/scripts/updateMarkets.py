from be_local_server.models import *
from datetime import *
from django.core.files import File 
from PIL import Image
import urllib


#-----------------------------------------------------------------------------------------------------
# MOSS STREET MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="1330 Fairfield Road", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8S 5J1", # Postal Code
	latitude=48.414895, # Latitude
	longitude=-123.347773, #Longitude
)

# Save it
a.save()

# # Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=4, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 10, 0, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 14, 0, 0), # (year, month, day, hour, minute, second)
# )

# # Save it
# h1.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/MSM.jpg'))
)

mp.save()

# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Moss Street Market", # Market name
	description="Moss Street Market is a vibrant community market that features Victoria's largest selection of local and organic produce.  The market has over 25 farmers vending with there are over 70 additional vendors offering handmade crafts, cards, clothing, jewelry, purses, toys, glass works, pottery, bath products, preserves, chocolates, baked goods, pesto, salsa, honey, and much much more. The Moss Street Market also has an activity tent for kids and live music each week.", # Market description
	photo=mp,
	webpage="http://www.mossstreetmarket.com/"
)

m.save()

#-----------------------------------------------------------------------------------------------------
# HUDSON PUBLIC MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="1701 Douglas Street", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8W 0C1", # Postal Code
	latitude=48.429456,
	longitude=-123.36448,

)

# Save it
a.save()

# Create hours for the address
h1 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=2, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 9, 30, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 18, 30, 0), # (year, month, day, hour, minute, second)
)

# Save it
h1.save()


# Create hours for the address
h2 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=3, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 9, 30, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 18, 30, 0), # (year, month, day, hour, minute, second)
)

# Save it
h2.save()

# Create hours for the address
h3 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=4, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 9, 30, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 18, 30, 0), # (year, month, day, hour, minute, second)
)

# Save it
h3.save()

# Create hours for the address
h4 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=5, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 9, 30, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 18, 30, 0), # (year, month, day, hour, minute, second)
)

# Save it
h4.save()

# Create hours for the address
h5 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=6, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 9, 30, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 17, 0, 0), # (year, month, day, hour, minute, second)
)

# Save it
h5.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/VPM.jpg'))
)

mp.save()

# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Victoria Public Market", # Market name
	description="Going back to the old-world style of shopping where you know your butcher, your baker, the person who grows your vegetables and the chickens that lay your eggs is what the Victoria Public Market at the Hudson is all about. The Victoria Public Market at the Hudson also offers a year-round indoor farmers' market every Wednesday from 11am - 3pm and a seasonal outdoor farmers market from May to October.", # Market description
	photo=mp,
	webpage="http://victoriapublicmarket.com/"
)

m.save()



#-----------------------------------------------------------------------------------------------------
# HUDSON PUBLIC MARKET - INDOOR FARMERS MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="1701 Douglas Street", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8W 0C1", # Postal Code
	latitude=48.429456,
	longitude=-123.36448,

)

# Save it
a.save()

# Create hours for the address
h1 = OpeningHours(
	address=a, # Each opening hour object has to have an address associated with it
	weekday=3, # 1 = Monday, ..., 7 = Sunday
	from_hour=datetime(2014, 10, 4, 11, 00, 0), # (year, month, day, hour, minute, second)
	to_hour=datetime(2014, 10, 4, 15, 0, 0), # (year, month, day, hour, minute, second)
)

# Save it
h1.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/VPMI.jpg'))
)

mp.save()

# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Victoria Public Market - Indoor Farmers' Market", # Market name
	description="As a subset of the Victoria Public Market at the Hudson, the year-round weekly indoor farmers' market shows off some of the best local farmers and foodmakers that Victoria has to offer.", # Market description
	photo=mp,
	webpage="http://victoriapublicmarket.com/"
)

m.save()


#-----------------------------------------------------------------------------------------------------
# HUDSON PUBLIC MARKET - OUTDOOR FARMERS MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="1701 Douglas Street", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8W 0C1", # Postal Code
	latitude=48.429456,
	longitude=-123.36448,

)

# Save it
a.save()

# # Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=3, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 11, 00, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 15, 0, 0), # (year, month, day, hour, minute, second)
# )

# # Save it
# h1.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/VPMO.jpg'))
)

mp.save()

# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Victoria Public Market - Outdoor Farmers' Market", # Market name
	description="As a subset of the Victoria Public Market at The Hudson, the seasonal outdoor farmers' market shows off some of the best local farmers and foodmakers that Victoria has to offer.  The outdoor farmers market runs weekly from May - October, and is held in the back carriageway of The Hudson.", # Market description
	photo=mp,
	webpage="http://victoriapublicmarket.com/"
)

m.save()

#-----------------------------------------------------------------------------------------------------
# BASTION SQUARE MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="Bastion Square", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V5H1G9", # Postal Code
	latitude=48.4257621,
	longitude=-123.3684807,
)

# Save it
a.save()

# Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=1, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 8, 0, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 16, 0, 0), # (year, month, day, hour, minute, second)
# )

# Save it
h1.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/BSM.jpg'))
)

mp.save()

# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Bastion Square Market", # Market name
	description="The Bastion Square Market brings liveliness to Victoria's historic Bastion Square. Every Sunday from May - September, the market includes farmers selling their locally-grown produce and fruits, homemade breads, pastries, honey, preserves, chutneys, and relishes, free range eggs, and much more.  The market also features an eclectic mix of arts, crafts, imports, and entertainment", # Market description
	photo=mp,
	webpage="http://bastionsquare.ca/"
)

m.save()


#-----------------------------------------------------------------------------------------------------
# JAMES BAY MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="494 Superior St Victoria", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8V 2G9", # Postal Code
	latitude=48.418221,
	longitude=-123.372516,
)

# Save it
a.save()

# Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=6, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 9, 0, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 15, 0, 0), # (year, month, day, hour, minute, second)
# )

# Save it
# h1.save()


mp = MarketPhoto(
		image=File(open('../client/app/images/markets/JBM.jpg'))
)

mp.save()


# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="James Bay Market", # Market name
	description="The James Bay Market features produce, arts, food and live music with an emphasis on products that are homemade, handmade and homegrown.  The market provides an amazing variety of locally grown or made products and runs seasonally from May - October.", # Market description
	photo=mp,
	webpage="http://jamesbaymarket.com/"
)

m.save()


#-----------------------------------------------------------------------------------------------------
# OAKLANDS SUNSET MARKET
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="Oaklands Community Center, 1-2827 Belmont Ave", # Street number and street name
	city="Victoria", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8R 4B2", # Postal Code
	latitude=48.440987,
	longitude=-123.338325,
)

# Save it
a.save()

# Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=6, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 16, 30, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 10, 30, 0), # (year, month, day, hour, minute, second)
# )

# Save it
# h1.save()

mp = MarketPhoto(
		image=File(open('../client/app/images/markets/OCM.jpg'))
)

mp.save()


# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="Oaklands Sunset Market", # Market name
	description="Every Wednesday from June - September, the Oaklands Sunset Market is in full swing! The market features vendor tables for your weekly veggies, breads, granola, teas, canned and baked goods or browse the many homemade crafts. The market also attracts local food trucks and delicious hot food from around the city.", # Market description
	photo=mp,
	webpage="http://www.oaklandscommunitycentre.com/markets"
)

m.save()


#-----------------------------------------------------------------------------------------------------
# North Saanich Farm Market
#-----------------------------------------------------------------------------------------------------

# Create an address
a = Address(
	addr_line1="St John's Unitied Church, 10990 W Saanich Rd", # Street number and street name
	city="North Saanich", # City
	state="BC", # Province
	country="Canada", # Country
	zipcode="V8R 4B2", # Postal Code
	latitude=48.679651,
	longitude=-123.457711,
)

# Save it
a.save()

# Create hours for the address
# h1 = OpeningHours(
# 	address=a, # Each opening hour object has to have an address associated with it
# 	weekday=6, # 1 = Monday, ..., 7 = Sunday
# 	from_hour=datetime(2014, 10, 4, 16, 30, 0), # (year, month, day, hour, minute, second)
# 	to_hour=datetime(2014, 10, 4, 10, 30, 0), # (year, month, day, hour, minute, second)
# )

# Save it
# h1.save()


mp = MarketPhoto(
		image=File(open('../client/app/images/markets/NSFM.jpg'))
)

mp.save()


# Create a market
m = Market(
	address=a, # Each Market object needs an address associated with it (this also associates hours)
	name="North Saanich Farm Market", # Market name
	description="Featuring food grown in the Saanich peninsula, the North Saanich Farm Market runs seasonally from May - September. The non-profit market aims to support local growers and farmers by providing them with a venue to sell their produce and products, while giving the community access to locally grown fruits, vegetables and products.  All the producers, at the North Saanich Farm Market, must show their commitment to organic and sustainable practices.", # Market description
	photo=mp,
	webpage="http://www.northsaanichfarmmarket.ca/"
)

m.save()



