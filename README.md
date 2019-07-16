# Levenshtein-String-Region

This code help me to choose a theme dinner topic, using friend's age and 20 Italian regions.
YES, That's a [sporious correlation](https://www.tylervigen.com/spurious-correlations)

## INPUT:
Every friend suggest me a letter of the alphabet and i store it in the stupidi string variable. 
Then i create a vector ,stupidi_age, where i collect the age of my friends.
I scraped a dataset which contains the name of the  20 Italian regions.
The stupidi string is manipulated by letters of the  best 5 nearest (in terms of Levenstein distance a.k.a [LVD] ) regions.

## OUTPUT:
The name of the nearest (in terms of LVD)  region to the stupidi string.

## Parameters
The minimum distance value is fixed by the user.

## How it works ? 
### Buold the regions dataset
Using LVD a random string is compared with the dataset scraped from the web.
BeautifulSoap4 is used to scrape the webpage, and downloads the data from a <HTML> </HTML> table.

From the table, a dictionary <Key,Array[]> is created.
Containing region as a Key and  Capital, Population, Towns and Provinces as Array.
The LVD is calculated between the random string variable stupidi and all the regions that occour in the dictionary.

Once the LVD is calculated, the best five region are drawn.

For each region an index is calculated as follow:  
* drawn random an index for stupidi_age vector 
* the selected age is divided by the number of provinces in each region.
* This index is used to get a letter of the region and substitute it in the stupidi string.

Thus, the region is going to affect the random stupidi string and contribute to modify it.
The substitution can happen in three different way:

1) ===BEST SUB===: The index point to a letter of the region, and the letter can be directly substituted in stupidi string.
2) ===MEDIUM SUB===: The index point to a letter of the region, but it exceed the length of the stupidi string. Than the letter is going to be suistituted in a random position of the stupdi string.
3) ===WORST SUB===: The index is nor pointing to a letter in the region , neither in the stupidi string.
Than a random letter of the region is going to be substituted in a random place of the stupidi string.

This process is going to be repeated untill the LVD store in region[1] of the data is grather than a certain fixed value.
N.B. => If the fixed value is too high the algoritm will be trapped in a local maximum, substituiting always the same chars in the same positions, please be aware to choose the right value.
