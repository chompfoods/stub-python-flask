# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Chomp Food &amp; Recipe Database API Documentation",
    author_email="",
    url="",
    keywords=["Swagger", "Chomp Food &amp; Recipe Database API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. * Get a **Food Data API** key at **[https://chompthis.com/api](https://chompthis.com/api/)**. * Get a **Recipe Data API** key at **[https://chompthis.com/api/recipes](https://chompthis.com/api/recipes/)**.  ### Getting Started   * Subscribe to the **[Food Data API](https://chompthis.com/api/#pricing)** or the **[Recipe Data API](https://chompthis.com/api/recipes/#pricing)**.   * Scroll down and click the \&quot;**Authorize**\&quot; button.   * Enter your API key into the \&quot;**value**\&quot; input, click the \&quot;**Authorize**\&quot; button, then click the \&quot;**Close**\&quot; button.   * Scroll down to the section titled \&quot;**default**\&quot; and click on the API endpoint you wish to use.   * Click the \&quot;**Try it out**\&quot; button.   * Enter the information the endpoint requires.   * Click the \&quot;**Execute**\&quot; button.  ### Example    * Branded food response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Recipe response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/example-recipe-response.json)**   * Error response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### I&#x27;m a Premium subscriber. How do I access the API?   * All Premium subscribers must pass in a unique user ID for each user on their platform that is accessing data from the Chomp API. A user ID can be any string of letters and numbers that you assign to your user. Simply add \&quot;user_id\&quot; as a URL parameter when calling the API. *You must add a \&quot;user_id\&quot; URL parameter to every call you make to ANY endpoint.*     * **Example**        &gt; &#x60;&#x60;&#x60;ENDPOINT.php?api_key&#x3D;API_KEY&amp;code&#x3D;CODE&amp;user_id&#x3D;USER_ID&#x60;&#x60;&#x60;  ### Helpful Links   * **Help &amp; Support**     * [Knowledge Base &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &amp;raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &amp;raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Food Data API Subscription Options &amp;raquo;](https://chompthis.com/api/)     * [Recipe Data API Subscription Options &amp;raquo;](https://chompthis.com/api/recipes/)     * [Food Data API Cost Calculator &amp;raquo;](https://chompthis.com/api/cost-calculator.php)     * [Recipe Data API Cost Calculator &amp;raquo;](https://chompthis.com/api/recipes/cost-calculator.php)   * **Guidelines**     * [Terms &amp; License &amp;raquo;](https://chompthis.com/api/terms.php)     * [Attribution &amp;raquo;](https://chompthis.com/api/docs/attribution.php) 
    """
)
