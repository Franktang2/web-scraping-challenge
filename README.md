# web-scraping-challenge

A web application that scrapes various websites for data related to Mars and displays the information in a single HTML page.

The websites were:

- NASA Mars News Site (https://mars.nasa.gov/news/), in which I collected the latest News Title and Paragraph
 
- JPL Mars Space Images - Featured Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars),  in which I collected the Scraped the full-size image URL for the current featured Mars image.
 
- Mars Weather Twitter Account (https://twitter.com/marswxreport?lang=en), in which I collected the latest Mars weather tweet from the page.

- Mars Facts Website (https://space-facts.com/mars/), in which I collected the table containing facts about the planet

- USGS Astrogeology Website (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars), in which I collected high-resolution images for each of Mar's hemispheres.


## Technologies Used

- Splinter/Requests
- Pandas
- Jupyter Notebook
- Python
- Beautiful Soup
- MongoDB
- Flask
