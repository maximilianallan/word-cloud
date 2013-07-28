word-cloud
==========

About
-----

Create pretty visual word clouds using
[PyTagCloud](https://github.com/atizo/PyTagCloud) from a Facebook message history.

Installation
------------


1. Install [PyTagCloud](https://github.com/maximilianallan/PyTagCloud).

2. Install the [Python SDK for Facebook.](https://github.com/maximilianallan/facebook-sdk).
          
3. Get a Facebook access token with permission to read the user's inbox from [here](https://developers.facebook.com/tools/explorer/?method=GET&path=223001829%3Ffields%3Did%2Cname). Eventually I will sort of Facebook permissions properly. Save this in the root project directory as access_token.txt.

4. Run as:

         $ python word-cloud "John Smith"

5. Admire the word cloud generated at cloud.png.         
 
       
