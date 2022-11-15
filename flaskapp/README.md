# FlashFire

__STATUS:__ CURRENTLY IN DEVELOPMENT     <br><br>
__Application:__                         <br>
FlashFire is a trading platform / flask web application that reproduces the behaviours and features of the US stock market, while utilising Alpacas trade API to both retrieve market data and place orders. This allows users to trade commission-free with live-trading, or simply practice trading equities without financial risk with paper-trading.                <br>

The user interface prioritises user-friendliness with a simplistic design that aims to reduce klutter and support individuals that may have little to no experience trading or managing financial portfolios. Upon registering an account, each users paper-trading configuration can be tailored to suit that individuals level of trading experience.             
Users will also be able to utilise a paradigm of popular trading strategies that can be configured from the user interface to automatically place/cancel orders on the users behalf.      <br>                                                                                 

This is my first major flask capstone project, so any feedback/assistance on the app will be welcomed and highly appreciated. Feel free to contact me if you experience any issues   <br><br><br>


### Package dependencies: 
    python,              
    flask,                        
    flask-session,                
    flask-wtf,                    
    requests,                     
    python-dotenv,                
    alpaca-trade-api,          
    email_validator,              
    datetime,
    
<br>  

### .gitignore:               
    __pycache__/
    instance/
    tests/
    .env
    test.py
    logs/
    
<br>      

### Usage:                                                                  <br>
1. __Install the latest version of Python and add to your PATH.__           <br>
2. __Install package dependencies into your environment.__                  <br>
3. __Configure the Alpaca API.__                                            <br>
   -Alpacas api key and secret key are required by the app to send REST requests. Both can be obtained for free on their website.   <br>
   -Once you have obtained your keys, create a file: ".env" in the root flashfire directory.                                        <br>
   -Open .env using a text editor and paste the keys as values to their respective variables: "ALPACA_KEY=yourapikeyhere, ALPACA_SECRET=yoursecretkeyhere, PAPER_URL=yoururlhere"                                                      <br>
4. __Construct the database.__                                              <br>
   -Initialize the database by running the following cli command while in the root flashfire directory: "flask init-db"             <br>
   -Populate the database by executing "update_db.py" in the scripts/ directory: "python scripts/update_db.py"                      <br>
   -(OPTIONAL) Schedule the script to run daily if you wish to keep the database up to date automatically                           <br>
5. __Run flask from the CLI with: "flask run"__                             <br><br><br>

__------------------PACKAGE TREE--------------------------__

    FLASHFIRE
    ├───env
    ├───flashfire
    │   ├───static
    │   │   ├───css
    │   │   │   ├───bootstrap.css
    │   │   │   └───styles.css
    │   │   ├───js
    │   │   │   └───bootstrap.bundle.js
    │   │   └───images
    │   │       └───.ico and .svg files
    │   ├───templates
    │   │   ├───auth
    │   │   │   ├───change_password.html
    │   │   │   ├───login.html
    │   │   │   └───register.html
    │   │   ├───platform
    │   │   │   ├───index.html
    │   │   │   ├───portfolio.html
    │   │   │   ├───quote.html
    │   │   │   ├───settings.html
    │   │   │   ├───trading.html
    │   │   │   └───watchlist.html
    │   │   └───base.html
    │   ├───__init__.py
    │   ├───auth.py
    │   ├───db.py
    │   ├───forms.py
    │   ├───queries.py
    │   ├───platform.py
    │   └───schema.sql
    ├───scripts
    │   ├───update_db.py
    │   ├───update_latest.py
    │   ├───update_prices.py   
    │   ├───update_snaps.py
    │   └───update_stocks.py
    ├───.flaskenv
    ├───.gitignore
    ├───MANIFEST.in
    ├───README.md
    └───setup.py


--------------------------------------------------


















