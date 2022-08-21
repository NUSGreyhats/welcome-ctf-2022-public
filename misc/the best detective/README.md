# the best detective

### Challenge Details
This is an OSINT (Open Source Intelligence) challenge.

Find out the name of a person and what she likes.

The only information given is a username: cingelord2361

Format the flag as such: greyhats{\<name\>\_\<favouritesinger\>\_\<favouritemovie\>}

For example: greyhats{johnnybravo_michaeljackson_wargames}

### Key Concepts
Eveything you put on the internet will always be recorded somewhere

### Solution
- Use sherlock to find [Greyson Caterine's twitter account](https://twitter.com/cingelord2361)
- Use the info in her bio to find her favourite singer (Miracle Johnson)
- Use waybackmachine to see her deleted tweet about a quote from her favourite movie (The Martian).
- A clue hinting about Will Smith's older meme (youtube rewind) can be found by Googling `cingelord2361`.

### Learning Objectives
- How to use tools to help with finding somebody
- How to google for information
- How to use Wayback Machine

### Flag
greyhats{greysoncaterine_miraclejohnson_themartian}