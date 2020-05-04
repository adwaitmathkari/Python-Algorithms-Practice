var unirest = require("unirest");

// var req = unirest("GET", "https://covid-19-data.p.rapidapi.com/help/countries");

// req.query({
// 	"format": "json"
// });

// req.headers({
// 	"x-rapidapi-host": "covid-19-data.p.rapidapi.com",
// 	"x-rapidapi-key": "64ea9a4eddmsh9d3ca69386d0bb7p1c51b8jsnf91aa4855f96"
// });

// console.log('alsduflsadfhasdlkfh')

// req.end(function (res) {
// 	if (res.error) throw new Error(res.error);

// 	console.log(res.body);
// });

let response;
unirest
    .get("https://covid-19-data.p.rapidapi.com/help/countries")
    .headers({
        "x-rapidapi-host": "covid-19-data.p.rapidapi.com",
        "x-rapidapi-key": "64ea9a4eddmsh9d3ca69386d0bb7p1c51b8jsnf91aa4855f96"
    })
    .send()
    .then((res) => response = res );
