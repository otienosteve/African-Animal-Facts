# AFRICAN ANIMAL FACTS
![elephant.jpg](elephant.jpg)


[Photo by Wolfgang Hasselmann on Unsplash](https://unsplash.com/photos/yaEkTCGc6vY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)

## Api Documentation

[<img src="SW-logo-clr.png">](https://app.swaggerhub.com/apis-docs/otienosteve/AfricanAnimalFacts/1.0.0#/)


Inspired by [Daily Cat Facts](https://alexwohlbruck.github.io/cat-facts/)

## Description

You think you know about african animals- Here are some interesting facts you maybe had not known about them.

This less sophisticated API will give you information about random african Animals.


## USAGE
Make a GET request to the following endpoint and be amazed.

[https://african-animal-facts.onrender.com/rand](https://african-animal-facts.onrender.com/rand)

Data is returned from the random Endpoint in the following format
```

{ 
"animal" : "the animal name"
 "fact" : "fact about the animal"
 "source" : "the fact source" 
}
```
To get all the facts at once use the following endpoint

[https://african-animal-facts.onrender.com/all/](https://african-animal-facts.onrender.com/all/)

Data is returned from the All Endpoint in the following format
```
[...

{
"animal": "the animal name" 
"fact": "fact about the animal" 
"source": "the fact source" 
  
 }

{},{},{}

{
"animal": "the animal name" 
"fact": "fact about the animal" 
"source": "the fact source" 
  
}

]
```
You feel there's something am missing? There's where the fun starts. You can make a POST request to the following enpoint to add data.

[https://african-animal-facts.onrender.com/update/](https://africananimalfacts.herokuapp.com/update/)

When Making a POST request add data in the following format
```
{ 
"animal" : "the animal name"
"fact" : "fact about the animal"
"source" : "the fact source" 
}
```

