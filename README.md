Instagram
=========

Polls Instagram for public posts, given a hashtag. The hashtag can be in either the caption or comments. Official documentation of Instagram API [here](http://instagram.com/developer/endpoints/tags/).

Properties
--------------

-   **queries**: List of hashtags to search public posts for.
-   **creds**: API credentials.
-   **polling_interval**: How often API is polled. When using more than one query. Each query will be polled at a period equal to the *polling\_interval* times the number of queries.
-   **retry_interval**: When a url request fails, how long to wait before attempting to try again.
-   **retry_limit**: When a url request fails, number of times to attempt a retry before giving up.

Python Package Dependencies
----------------

-   [requests](https://pypi.python.org/pypi/requests/)

Commands
----------------
None

Input
-------
None

Output
---------
Creates a new signal for each Instagram Post. Every field on the Post will become a signal attribute. Official documentation on the repsonse fields from Instagram [here](http://instagram.com/developer/endpoints/tags/). The following is a list of commonly include attributes, but note that not all will be included on every signal:

-   id
-   user['username']
-   caption['text']
-   link
-   images['standard_resolution']['url']
-   user['profile_picture']
-   type
-   created_time
