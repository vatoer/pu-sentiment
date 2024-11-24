# scrapper 

scrapper untuk tugas pu 

## pre

- isi variabel di `.env`
- search_keyword lihat cheatsheet

## limitation
- unverified hanya bisa 600 post/hari
- verified bisa 6000 post//hari


## command 

```sh
scrapper.py
```

menggunakan scrapper dari <https://github.com/helmisatria/tweet-harvest>


Here's a **tabular cheatsheet** for Twitter's advanced search operators to filter and search tweets effectively:

| **Operator**                  | **Description**                                                                                      | **Example**                         |
|-------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------|
| **Keyword**                   | Search for tweets containing a specific keyword.                                                   | `cats`                              |
| `"Exact Phrase"`              | Search for tweets with the exact phrase.                                                           | `"happy birthday"`                  |
| **#Hashtag**                  | Search for tweets with a specific hashtag.                                                         | `#coding`                           |
| **from:**                     | Search tweets from a specific user.                                                                | `from:elonmusk`                     |
| **to:**                       | Search tweets sent to a specific user.                                                             | `to:jack`                           |
| **@Username**                 | Search tweets that mention a specific user.                                                        | `@nasa`                             |
| **since:**                    | Search tweets sent after a specific date (YYYY-MM-DD).                                             | `since:2023-01-01`                  |
| **until:**                    | Search tweets sent before a specific date (YYYY-MM-DD).                                            | `until:2023-12-31`                  |
| **min_faves:**                | Search tweets with a minimum number of likes.                                                     | `min_faves:100`                     |
| **min_retweets:**             | Search tweets with a minimum number of retweets.                                                  | `min_retweets:50`                   |
| **min_replies:**              | Search tweets with a minimum number of replies.                                                   | `min_replies:20`                    |
| **filter:links**              | Search tweets containing links.                                                                   | `filter:links`                      |
| **-filter:links**             | Exclude tweets containing links.                                                                  | `-filter:links`                     |
| **filter:images**             | Search tweets containing images.                                                                  | `filter:images`                     |
| **filter:videos**             | Search tweets containing videos.                                                                  | `filter:videos`                     |
| **filter:media**              | Search tweets containing any type of media (images, videos, or links).                            | `filter:media`                      |
| **lang:**                     | Search tweets in a specific language using language codes (e.g., `en` for English).               | `lang:en`                           |
| **place:**                    | Search tweets from a specific location (requires place name or ID).                               | `place:"New York City"`             |
| **url:**                      | Search tweets containing a specific URL.                                                          | `url:example.com`                   |
| **"Keyword" OR "Keyword"**    | Search for tweets containing either of the keywords.                                              | `"apple" OR "banana"`               |
| **"Keyword" AND "Keyword"**   | Search for tweets containing both keywords.                                                       | `"java" AND "python"`               |
| **"Keyword" -Exclusion**      | Search for tweets with a keyword but exclude another keyword.                                      | `"car" -electric`                   |
| **near:**                     | Search tweets near a specific location (requires geolocation enabled).                            | `near:"San Francisco"`              |
| **within:**                   | Search tweets within a radius of a location (use with `near:`).                                   | `near:"San Francisco" within:15mi`  |
| **is:retweet**                | Search only retweets.                                                                              | `is:retweet`                        |
| **-is:retweet**               | Exclude retweets.                                                                                 | `-is:retweet`                       |
| **is:reply**                  | Search only replies.                                                                               | `is:reply`                          |
| **-is:reply**                 | Exclude replies.                                                                                  | `-is:reply`                         |
| **is:quote**                  | Search only quote tweets.                                                                          | `is:quote`                          |
| **has:hashtags**              | Search tweets containing hashtags.                                                                | `has:hashtags`                      |
| **has:links**                 | Search tweets containing links.                                                                   | `has:links`                         |
| **has:media**                 | Search tweets containing media (images, videos, or links).                                        | `has:media`                         |
| **has:mentions**              | Search tweets mentioning other users.                                                             | `has:mentions`                      |
| **"Keyword" until:YYYY-MM-DD since:YYYY-MM-DD** | Combine multiple filters for specific date ranges.                                     | `"election" since:2023-01-01 until:2023-06-30` |

---

### Example Searches:
1. **Find tweets about Python tutorials in English with at least 50 likes**:  
   `python tutorial lang:en min_faves:50`

2. **Find tweets mentioning Elon Musk with a hashtag and containing media**:  
   `@elonmusk has:hashtags has:media`

3. **Search for tweets about vacations excluding retweets and links**:  
   `vacation -filter:links -is:retweet`

