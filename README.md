# AFRICAN ANIMAL FACTS
![elephant.jpg](elephant.jpg)


[Photo by Wolfgang Hasselmann on Unsplash](https://unsplash.com/photos/yaEkTCGc6vY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)

## Api Documentation

[<img src="SW-logo-clr.png">](https://app.swaggerhub.com/apis-docs/otienosteve/AfricanAnimalFacts/1.0.0#/)

## Description

You think you know about african animals- Here are some interesting facts you maybe had not known about them.

This less sophisticated API will give you information about random african Animals.


## USAGE
Make a GET request to the following endpoint and be amazed.

[https://africananimalfacts.herokuapp.com/rand](https://africananimalfacts.herokuapp.com/)

Data is returned from the random Endpoint in the following format
- Animal- The Animal Name
- Fact- Fact About The Animal
- Source -The fact Source

To get all the facts at once use the following endpoint

[https://africananimalfacts.herokuapp.com/all/](https://africananimalfacts.herokuapp.com/all/)

Data is returned from the All Endpoint in the following format

[...

{
- Animal- The Animal Name 
- Fact- Fact About The Animal 
- Source -The fact Source 
  
 }

{},{},{}

{
- Animal- The Animal Name 
- Fact- Fact About The Animal 
- Source -The fact Source 
  
}

]

You feel there's something am missing? There's where the fun starts. You can make a POST request to the following enpoint to add data.

[https://africananimalfacts.herokuapp.com/update/](https://africananimalfacts.herokuapp.com/update/)

When Making a POST request add data in the following format
- Animal- The Animal Name (string)
- Fact- Fact About The Animal (string)
- Source -The fact Source (string)

