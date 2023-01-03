from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cash = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)


class Stock(models.Model):
    symbol = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)

class StockPriceMinute(models.Model):
    open = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    high = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    low = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    close = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    volume = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    datetime = models.DateTimeField(auto_now_add=True)

class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="watchlist")


class StockHistory(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="history") 



class StockInfo(models.Model):
    zip = models.CharField(max_length=10)
    sector = models.CharField(max_length=50)
    full_time_employees = models.PositiveIntegerField()
    long_business_summary = models.TextField()
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50)
    company_officers = models.TextField()
    website = models.URLField()
    max_age = models.PositiveIntegerField()
    address1 = models.CharField(max_length=100)
    fax = models.CharField(max_length=20)
    industry = models.CharField(max_length=50)
    ebitda_margins = models.DecimalField(max_digits=5, decimal_places=4)
    profit_margins = models.DecimalField(max_digits=5, decimal_places=4)
    gross_margins = models.DecimalField(max_digits=5, decimal_places=4)
    operating_cashflow = models.BigIntegerField()
    revenue_growth = models.DecimalField(max_digits=5, decimal_places=4)
    operating_margins = models.DecimalField(max_digits=7, decimal_places=6)
    ebitda = models.BigIntegerField()
    target_low_price = models.DecimalField(max_digits=6, decimal_places=2)
    recommendation_key = models.CharField(max_length=10)
    gross_profits = models.BigIntegerField()
    free_cashflow = models.BigIntegerField()
    target_median_price = models.DecimalField(max_digits=6, decimal_places=2)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    earnings_growth = models.DecimalField(max_digits=5, decimal_places=4)
    current_ratio = models.DecimalField(max_digits=5, decimal_places=4)
    return_on_assets = models.DecimalField(max_digits=5, decimal_places=4)
    number_of_analyst_opinions = models.PositiveIntegerField()
    target_mean_price = models.DecimalField(max_digits=6, decimal_places=2)
    debt_to_equity = models.DecimalField(max_digits=6, decimal_places=4)
    return_on_equity = models.DecimalField(max_digits=5, decimal_places=4)
    target_high_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_cash = models.BigIntegerField()
    total_debt = models.BigIntegerField()
    total_revenue = models.BigIntegerField()

    total_cash_per_share = models.DecimalField(max_digits=6, decimal_places=3)
    financial_currency = models.CharField(max_length=3)
    revenue_per_share = models.DecimalField(max_digits=6, decimal_places=3)
    quick_ratio = models.DecimalField(max_digits=4, decimal_places=3)
    recommendation_mean = models.DecimalField(max_digits=4, decimal_places=1)
    exchange = models.CharField(max_length=3)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=50)
    exchange_timezone_name = models.CharField(max_length=50)
    exchange_timezone_short_name = models.CharField(max_length=5)
    is_esg_populated = models.BooleanField()
    gmt_offset_milliseconds = models.CharField(max_length=10)
    quote_type = models.CharField(max_length=6)
    symbol = models.CharField(max_length=10)
    message_board_id = models.CharField(max_length=20)
    market = models.CharField(max_length=20)
    annual_holdings_turnover = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    enterprise_to_revenue = models.DecimalField(max_digits=6, decimal_places=3)
    beta_3_year = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    enterprise_to_ebitda = models.DecimalField(max_digits=6, decimal_places=3)
    _52_week_change = models.DecimalField(max_digits=8, decimal_places=7)
    morning_star_risk_rating = models.PositiveSmallIntegerField(null=True)
    forward_eps = models.DecimalField(max_digits=6, decimal_places=2)
    revenue_quarterly_growth = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    shares_outstanding = models.BigIntegerField()
    fund_inception_date = models.DateField(null=True)
    annual_report_expense_ratio = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    total_assets = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    book_value = models.DecimalField(max_digits=7, decimal_places=3)
    shares_short = models.BigIntegerField()
    shares_percent_shares_out = models.DecimalField(max_digits=6, decimal_places=4)
    fund_family = models.CharField(max_length=50, null=True)
    
    last_fiscal_year_end = models.PositiveIntegerField()
    held_percent_institutions = models.DecimalField(max_digits=6, decimal_places=5)
    net_income_to_common = models.BigIntegerField()
    trailing_eps = models.DecimalField(max_digits=6, decimal_places=2)
    last_dividend_value = models.DecimalField(max_digits=4, decimal_places=2)
    sandp_52_week_change = models.DecimalField(max_digits=8, decimal_places=7)
    price_to_book = models.DecimalField(max_digits=8, decimal_places=5)
    held_percent_insiders = models.DecimalField(max_digits=7, decimal_places=5)
    next_fiscal_year_end = models.PositiveIntegerField()
    yield_ = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    most_recent_quarter = models.PositiveIntegerField()
    short_ratio = models.DecimalField(max_digits=4, decimal_places=1)
    shares_short_previous_month_date = models.PositiveIntegerField()
    float_shares = models.BigIntegerField()
    beta = models.DecimalField(max_digits=6, decimal_places=5)

    enterprise_value = models.BigIntegerField()
    price_hint = models.SmallIntegerField()
    three_year_average_return = models.FloatField(blank=True, null=True)
    last_split_date = models.DateField()
    last_split_factor = models.CharField(max_length=10)
    legal_type = models.CharField(max_length=50, blank=True, null=True)
    last_dividend_date = models.DateField()
    morning_star_overall_rating = models.FloatField(blank=True, null=True)
    earnings_quarterly_growth = models.FloatField()
    price_to_sales_trailing_12_months = models.FloatField()
    date_short_interest = models.DateField()
    peg_ratio = models.FloatField()
    ytd_return = models.FloatField(blank=True, null=True)
    forward_pe = models.FloatField()
    last_cap_gain = models.FloatField(blank=True, null=True)
    short_percent_of_float = models.FloatField()
    shares_short_prior_month = models.BigIntegerField()
    implied_shares_outstanding = models.BigIntegerField()
    category = models.CharField(max_length=50, blank=True, null=True)
    five_year_average_return = models.FloatField(blank=True, null=True)
    previous_close = models.FloatField()
    regular_market_open = models.FloatField()
    two_hundred_day_average = models.FloatField()
    trailing_annual_dividend_yield = models.FloatField()
    payout_ratio = models.FloatField()

    volume24Hr = models.CharField(max_length=50, null=True)
    regularMarketDayHigh = models.CharField(max_length=50, null=True)
    navPrice = models.CharField(max_length=50, null=True)
    averageDailyVolume10Day = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)
    fiftyDayAverage = models.CharField(max_length=50, null=True)
    trailingAnnualDividendRate = models.CharField(max_length=50, null=True)
    open = models.CharField(max_length=50, null=True)
    toCurrency = models.CharField(max_length=50, null=True)
    averageVolume10days = models.CharField(max_length=50, null=True)
    expireDate = models.CharField(max_length=50, null=True)
    algorithm = models.CharField(max_length=50, null=True)
    dividendRate = models.CharField(max_length=50, null=True)
    exDividendDate = models.CharField(max_length=50, null=True)
    circulatingSupply = models.CharField(max_length=50, null=True)
    startDate = models.CharField(max_length=50, null=True)
    regularMarketDayLow = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=50, null=True)
    trailingPE = models.CharField(max_length=50, null=True)
    regularMarketVolume = models.CharField(max_length=50, null=True)
    lastMarket = models.CharField(max_length=50, null=True)
    maxSupply = models.CharField(max_length=50, null=True)
    openInterest = models.CharField(max_length=50, null=True)
    marketCap = models.CharField(max_length=50, null=True)
    volumeAllCurrencies = models.CharField(max_length=50, null=True)
    strikePrice = models.CharField(max_length=50, null=True)
    averageVolume = models.CharField(max_length=50, null=True)
    dayLow = models.CharField(max_length=50, null=True)
    ask = models.CharField(max_length=50, null=True)
    askSize = models.CharField(max_length=50, null=True)
    volume = models.CharField(max_length=50, null=True)
    fiftyTwoWeekHigh = models.CharField(max_length=50, null=True)
    fromCurrency = models.CharField(max_length=50, null=True)
    fiveYearAvgDividendYield = models.CharField(max_length=50, null=True)
    fiftyTwoWeekLow = models.CharField(max_length=50, null=True)

    bid = models.FloatField()
    tradeable = models.BooleanField()
    dividend_yield = models.FloatField()
    bid_size = models.IntegerField()
    day_high = models.FloatField()
    coin_market_cap_link = models.URLField(null=True)
    regular_market_price = models.FloatField()
    pre_market_price = models.FloatField(null=True)
    logo_url = models.URLField()
    trailing_peg_ratio = models.FloatField()