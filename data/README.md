# Science Saturday Data Notes

## Science Saturday 1: Can you tell the difference between Red vs. White Wine at room temperature?

* SS1_redvsWhiteGroupA.csv
* SS1_redvsWhiteGroupB.csv

#### Column names:

**case, guesser, wine1, wine1\_number, wine1\_color, wine1\_guess, wine1\_rating, wine1\_correct, wine2, wine2\_number, wine2\_color, wine2\_guess, wine2\_rating, wine2\_correct**

where:

* case - number between 1-11 which indicates the set of two wines that were tested
* guesser - person's first name and sometimes last initial in the case of the 3 Matts
* wine{1/2} - Style of wine of glass 1/2
* wine{1/2}_number - blind random number assigned to the wine bottle
* wine{1/2}_color - known color of the wine
* wine{1/2}_guess - color of the wine the blindfolded guesser believes the wine they are drinking is
* wine{1/2}_rating - Rating on a scale of 1-5 how much the guesser liked the wine. 1 is a low rating, 5 is a high rating
* wine{1/2}\_correct - Boolean of if wine\_color = wine\_guess

#### Notes
* People were only given 2 glasses of wine at one time
* Everyone was blindfolded
* All bottles of wine were left out at room temperature except for the Riesling 2016, which is marked with an asterisk (\*) in the wine{1/2} column of Group A.
* For Group B, the randomization code had a bug in it that didn't allow for higher number bottles to be selected, so at some point the group in charge randomized the bottles themselves.
* Also in Group B, there were two Cabernet Sauvignons, both at room temperature. These were the exact same bottles except that one was put in the fridge for a day before being brought up to room temperature. This was a mini Dave experiment inside the larger experiment to see if the two tasted differently (under the hypothesis that fridges ruin red wines).
* The Malbec and Sauvignon Blanc were from the same vineyard
* We only had 1 bottle of Rose, which became obvious was in Group A, so that could have biased some people in Group B who didn't guess Rose as much.
* Originally, the goal was to try every combination of wine, but we had way too many bottles of wine for that, so some combinations weren't done.

## Science Saturday 2: What is the least awful of shit beers?

* SS2_beerScores.csv
* SS2_beerOrder.csv
* SS2_beerNotes.csv

#### Column names:

**Beer, Beer\_Letter, name1, name2, etc.**

where:

* Beer - The name of the shitty beer
* Beer_Letter - The randomly assigned letter
* name1, name2 - The ratings (1 low 5 high), order of beer drinking, or notes for each person

#### Notes
* No one was blindfolded in this experiment
* All beers were poured into clear pitchers with sticky-note letters on them to denote which one they were.
* These letters were randomly assigned by Maria who did not participate in drinking
* Everyone had a different random order of letters on their sheet which indicated in which order they should be drinking
* We had one more beer type than anticipated, so there was one beer that suffered in non-randomization in the order of drinking.
* The darker colored beers likely did better because of the clear pitchers with no blindfolds -- people were more inclined to rate them higher (possibly)
* It was self-poured, so it wasn't a consistent volume per beer.

## Science Saturday 3: Do more expensive wines taste better?

* SS3_winePriceGuesses.csv
* SS3_winePriceRankings.csv
* SS3_winePriceRatings.csv
* SS3_winePriceNotes.csv

#### Column names:

**Wine, wine\_name, wine\_price, Color, name1, namen**

where:

* Wine - The letter indicating the wine, which was randomly assigned to a bottle after being wrapped. Reds and Whites were not given unique letters as they were tested in separate groups.
* wine_name - the name of the wine bottle
* wine_price - the price of the bottle of wine. All were bought at the same liquor store.
* color - red or white (no roses)
* name1, namen - For all of the participants, their ranking for the quality in the title of the csv (1 low, 5 high).

#### Notes
* All of the wines were bought by Jo and Roberto, so no one else knew the prices of the wine
* The bottles were wrapped by Rachel and then a random letter written on them by Jo, so no one had any idea what bottles were being poured.
* The same amount of wine was poured for each tasting.
* No blindfolds for this test


## Science Saturday 4: Which pizza chain should you order from?

* SS4_pizzaChainGuess.csv
* SS4_pizzaCheese.csv
* SS4_pizzaCrust.csv
* SS4_pizzaGreassiness.csv
* SS4_pizzaOverall.csv
* SS4_pizzaToppingQuality.csv
* SS4_pizzaSauce.csv

#### Column names:

**pizza\_chain, pizza\_letter, Temp, Type, Averages, name1, namen**

where:

* pizza_chain - is the name of the pizza chain
* pizza_letter - letter of the pizza. This is different for cheese and pepperoni
* temp - temperature of the pizza when it was served to us in degrees F
* type - cheese or pepperoni
* averages - average of everyone's score
* name1, namen - For all of the participants, their ranking for the quality in the title of the csv (1 low, 5 high). For greasiness, 5 is most greasy.

#### Notes
* The pizzas were timed to arrive at the same time, but that didn't happen exactly, so they all had to go in the oven.
* This was all blindfolded, and people were asked which chain they thought it was by raising their hand as all possibilities were called out.
* Cheese was served first, and then pepperoni.
* The oven door broke in between serving some of the pizzas
* Each slice of pizza was about an 1/8 of a pizza
* Particpants were encouraged to not eat the entire slice.

## Science Saturday 5: Red vs. White wine repeat with both cooled

* SS5_redvsWhiteGroup1.csv
* SS5_redvsWhiteGroup2.csv

#### Column names:

**case, guesser, wine1, wine1\_number, wine1\_color, wine1\_guess, wine1\_rating, wine1\_correct, wine2, wine2\_number, wine2\_color, wine2\_guess, wine2\_rating, wine2\_correct**

* case - number between 1-11 which indicates the set of two wines that were tested
* guesser - person's first name and sometimes last initial in the case of the 3 Matts
* wine{1/2} - Style of wine of glass 1/2
* wine{1/2}_number - blind random number assigned to the wine bottle
* wine{1/2}_color - known color of the wine
* wine{1/2}_guess - color of the wine the blindfolded guesser believes the wine they are drinking is
* wine{1/2}_rating - Rating on a scale of 1-5 how much the guesser liked the wine. 1 is a low rating, 5 is a high rating
* wine{1/2}\_correct - Boolean of if wine\_color = wine\_guess

#### Notes
* This was a bit more organized, but had fewer people than the first. All combinations of the wines were tried
* All of the wines were in the fridge until they were poured, and then put back in the fridge after being poured.
* Everyone was blindfolded when drinking
* Attempts to get the same types of wine as SS1 where possible.
* This was done in groups of 5 cases and then switching between the two groups

## Science Saturday 6: What makes a good cookie?

* SS6_cookieAppearance.csv
* SS6_cookieBite.csv
* SS6_cookieChocolateFlavor.csv
* SS6_cookieMoistness.csv
* SS6_cookieNotes.csv
* SS6_cookieOrder.csv
* SS6_cookiePersonalPreference.csv
* SS6_cookieSweetness.csv

#### Column names:

**Cookie, cookie\_descrip, name1, namen**

where:

* cookie - the letter of the cookie being eaten
* cookie_descrip - description of what was changed from the cookie/what was different
* name1, namen - For all of the participants, their ranking for the quality in the title of the csv.
  * Bite Key
    * 1	Very Crunchy
    * 2	Crunchy
    * 3	Chewy
    * 4	Cakey
  * Chococlate Key
    * 1	Not Choc.
    * 2	Choc.
    * 3	Too (Very) Choc.
  * Moist Key
    * 1	Dry
    * 2	Neutral
    * 3	Moist
  * Sweet Key
    * 1	Not Sweet
    * 2	Sweet
    * 3	Super Sweet
  * Personal Key
    * 0 coffin emoji
    * 1 throwing up emoji
    * 2 Sweat sad face emoji
    * 3 Shrug emoji
    * 4 drool emoji
    * 5 head exploding emoji
  * Appearance key
    * 1	Probably not
    * 2	would eat
    * 3	martha stewart level

#### Notes
* The cookies were baked in separate ovens.
* We tried to control by size, but people didn't always follow that guideline, so the cookies that were bigger were liked more because they were overall softer cookies (generally speaking).
* Blindfolds were used when eating cookies
* The chocolatey was very much biased by the bite of cookie that you took, and a lot of people only took 1 bite


## Science Saturday 8: What is the best Octoberfest beer?

* SS8_octoberfest.csv

#### Columns

  * Beer - Brand of beer
  * Drinker - Person rating the beer.
  * Round - When was this beer drunk.
  * Cup - Within the round, which cup was assiged to the beer.
  * Rating - On a scale on 1 to 5 (5 being highest), what score does this beer get. Zeros not allowed.

#### Notes

Each person was served ~2 ounces of each beer. There were 18 beers in total, served in 9 rounds. Within each round, the drinker was given two samples to taste. Drinkers took breaks afters rounds 3 and 6. The order of the samples was randomized by the servers, with the exception of the Sam Adams, which were always served together to try to ascertain whether keg or bottle tasted better.

## Science Saturday 9: Alcoholic vs. Non-alcoholic Beer

* SS9_BeerCatalog.csv  

### Columns
  * Beer - Brand of Beer
  * Alcoholic - Truth of alcoholic or Non-Alcoholic
  * Style - Truth of style
  * ABV - From cans

* SS9_Results.csv

### Columns
  * Beer - Brand of Beer
  * Info
    * Info contains: Number (order this was served), Alcoholic (True/False Guess), Style (Guess), Rating (1-5), Comment
  * Names - One column for each person that participated

### Notes

Each person was served a shot of each beer (or NA beer). Each one was given one at a time and told to rate on a scale of 1 to 5, with 5 being the best and 1 being the worst. Because there were so many beers/NA beers, several rounds were used. All beers were kept in the fridge, and only taken out to pour. What was served was randomly selected by the person serving the beverage.

## Science Saturday 10: Generic Brand vs. Name-Brand Products

  * SS10_capncrunch.csv
  * SS10_capncrunchberries.csv           
  * SS10_chip.csv               
  * SS10_cookie.csv             
  * SS10_cola.csv               
  * SS10_drpepper.csv           
  * SS10_icecream.csv           
  * SS10_life.csv               
  * SS10_rumncoke.csv
  * SS10_sourcream.csv

### Columns

  * person - Name of guesser
  * round	- Number of guess
  * capncrunch / capncrunchberries / chip / cola / cookie / drpepper / icecream / life  / rumncoke / sourcream (Truth column)
  * score	- Rating 1 to 5
  * guess/comment (Some people guessed if it was generic or not)

### Notes

Not everyone participated in all of the rounds, and their columns are left blank if that's the case. In each scenario people were blindfolded and told to rate the item based purely on taste. For the Oreos, some people held the cookies by the edges or were fed the cookies. For the chips, nothing was done to mask the Utz ridges. The sour cream was served on a plain potato chip. The ice cream was very freezer burned, and should be redone. People were told to rate on a scale of 1 to 5, with 1 being awful and 5 being fantastic.
