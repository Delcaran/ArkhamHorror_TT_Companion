"northside": {
	"places": [
		"train station",
		"newspaper",
		"curiositie shoppe"
	],
	"links": {
		"downtown": "white",
		"merchant district": "black"
	}
},
"downtown": {
	"places": [
		"bank of arkham",
		"arkham asylum",
		"independence square"
	],
	"links": {
		"northside": "black",
		"merchant district": "none",
		"easttown": "white"
	}
},
"easttown": {
	"places": [
		"hibb's roadhouse",
		"velma's diner",
		"police station"
	],
	"links": {
		"downtown": "black",
		"rivertown": "white"
	}
},
"rivertown": {
	"places": [
		"graveyard",
		"black cave",
		"general store"
	],
	"links": {
		"easttown": "black",
		"french hill": "white",
		"merchant district": "none"
	}
},
"merchant district": {
	"places": [
		"unvisited isle",
		"river docks",
		"the unnamable"
	],
	"links": {
		"northside": "white",
		"downtown": "none",
		"rivertown": "none",
		"miskatonic university": "black"
	}
},
"miskatonic university": {
	"places": [
		"science building",
		"administration",
		"library"
	],
	"links": {
		"merchant district": "white",
		"french hill": "none",
		"uptown": "black"
	}
},
"french hill": {
	"places": [
		"the witch house",
		"silver twilight lodge"
	],
	"links": {
		"miskatonic university": "none",
		"southside": "white",
		"rivertown": "black"
	}
},
"uptown": {
	"places": [
		"st. mary's hospital",
		"ye olde magick shoppe",
		"woods"
	],
	"links": {
		"miskatonic university": "white",
		"southside": "black"
	}
},
"southside": {
	"places": [
		"ma's boarding house",
		"south church",
		"historical society"
	],
	"links": {
		"uptown": "white",
		"french hill": "black"
	}
}