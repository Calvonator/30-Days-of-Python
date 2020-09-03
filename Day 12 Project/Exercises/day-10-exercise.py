tup = (
 	"The Dark Side of the Moon",
 	"Pink Floyd",
 	1973,
 	(
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 )

dict1 = {}

dict1["Album"] = tup[0]
dict1["Artist"] = tup[1]
dict1["Year"] = tup[2]
dict1["Tracks"] = tup[3]


for key, value in dict1.items():
    print(f"{key}: {value}")
