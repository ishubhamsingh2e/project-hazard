# Project-Hazard⚠
It a API for game **joking hazard** it will generate fun story picking random cards, you just have to read them in sequence.

API is LIVE!!🔴 here 👉 https://sb2001nov.pythonanywhere.com

On a get request it will git you 3 links of images for each card have a equal probability of occurance except the 3rd card, there is a 10% chance of getting a red card by default.

<p float="left">
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/60.jpg" width="200" />
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/65.jpg" width="200" /> 
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/225.jpg" width="200" />
</p>

<p float="left">
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/239.jpg" width="200" />
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/68.jpg" width="200" /> 
  <img src="https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/red/10.jpg" width="200" />
</p>


## API
API have 2 variables
- Red
- chance

### Red
Red is a bool value by default set to 0, if you chage it to 1 it will always return a red card.
0 is 10% chance by default

### Chance
- Chance by default is set to 10, it specifies the probability of getting a red
- Here value of chance is the size of the sample and we are using probability of 0 in 1 - n
- Probability = Condition / Sample space

To call the API use thins url

```sh
curl https://sb2001nov.pythonanywhere.com
```

To call the API with parameters

```sh
curl https://sb2001nov.pythonanywhere.com?red=1
```

```sh
curl https://sb2001nov.pythonanywhere.com?chance=20
```

Sample Response :

```json
{
"1": "https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/298.jpg",
"2": "https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/169.jpg",
"3": "https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/109.jpg",
"red": 0
}
```
