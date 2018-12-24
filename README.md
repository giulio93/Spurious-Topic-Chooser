# Levenshtein-String-Region

Using LVD a random string is compared with a dataset scraped from the web.
BeautifulSoap4 is used to scrape the webpage, and downloads the data from a <HTML> </HTML> table.

From the table, a dictionary <Key,Array[]> is created.
Containing region as a Key and  Capital, Population, Towns and Provinces as Array.
The LVD is calculated between the random string variable stupidi and all the regions that occour in the dictionary.

Once the LVD is calculated, the best five region are taken.

For each region an index is calculated: as the stupidi_age divided by the number of provinces in the region.
This index is used to get a letter of the region and substitute it in the stupidi string.

In this way the region is going to affect the random string and contribute to modify it.
The substitution can happen in three different way:

1) ===BEST SUB===: The index point to a letter of the region, and the letter can be directly substituted in stupidi string.
2) ===MEDIUM SUB===: The index point to a letter of the region, but it exceed the length of the stupidi string. Than the letter is going to be suistituted in a random position of the stupdi string.
3) ===WORST SUB===: The index is nor pointing to a letter in the region , neither in the stupidi string.
Than a random letter of the region is goin to be substituted in a random place of the stupidi string.

This process is goin to be repeated untill the LVD store in region[1] of the data is grather than a certain fixed value.
N.B. => If the fixed value is too high the algoritm will be trapped in a local maximum, substituiting always the same chars in the same positions, please be aware to choose the right value.
