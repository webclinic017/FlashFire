# Generated by Django 4.1.5 on 2023-01-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_ebitda_margins_stockinfo_ebitdamargins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockinfo',
            old_name='annual_holdings_turnover',
            new_name='annualHoldingsTurnover',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='annual_report_expense_ratio',
            new_name='annualReportExpenseRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='beta_3_year',
            new_name='beta3Year',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='bid_size',
            new_name='bidSize',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='book_value',
            new_name='bookValue',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='coin_market_cap_link',
            new_name='coinMarketCapLink',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='current_price',
            new_name='currentPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='current_ratio',
            new_name='currentRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='date_short_interest',
            new_name='dateShortInterest',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='day_high',
            new_name='dayHigh',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='debt_to_equity',
            new_name='debtToEquity',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='dividend_yield',
            new_name='dividendYield',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='earnings_growth',
            new_name='earningsGrowth',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='earnings_quarterly_growth',
            new_name='earningsQuarterlyGrowth',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='enterprise_to_ebitda',
            new_name='enterpriseToEbitda',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='enterprise_to_revenue',
            new_name='enterpriseToRevenue',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='enterprise_value',
            new_name='enterpriseValue',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='exchange_timezone_name',
            new_name='exchangeTimezoneName',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='exchange_timezone_short_name',
            new_name='exchangeTimezoneShortName',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='_52_week_change',
            new_name='fiftyTwoWeekChange',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='financial_currency',
            new_name='financialCurrency',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='five_year_average_return',
            new_name='fiveYearAverageReturn',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='float_shares',
            new_name='floatShares',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='forward_eps',
            new_name='forwardEps',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='forward_pe',
            new_name='forwardPe',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='free_cashflow',
            new_name='freeCashflow',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='full_time_employees',
            new_name='fullTimeEmployees',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='fund_family',
            new_name='fundFamily',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='fund_inception_date',
            new_name='fundInceptionDate',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='gmt_offset_milliseconds',
            new_name='gmtOffsetMilliseconds',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='gross_margins',
            new_name='grossMargins',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='gross_profits',
            new_name='grossProfits',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='held_percent_insiders',
            new_name='heldPercentInsiders',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='held_percent_institutions',
            new_name='heldPercentInstitutions',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='implied_shares_outstanding',
            new_name='impliedSharesOutstanding',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='is_esg_populated',
            new_name='isEsgPopulated',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_cap_gain',
            new_name='lastCapGain',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_dividend_date',
            new_name='lastDividendDate',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_dividend_value',
            new_name='lastDividendValue',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_fiscal_year_end',
            new_name='lastFiscalYearEnd',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_split_date',
            new_name='lastSplitDate',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='last_split_factor',
            new_name='lastSplitFactor',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='legal_type',
            new_name='legalType',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='logo_url',
            new_name='logoUrl',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='long_name',
            new_name='longName',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='message_board_id',
            new_name='messageBoardId',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='morning_star_overall_rating',
            new_name='morningStarOverallRating',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='morning_star_risk_rating',
            new_name='morningStarRiskRating',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='most_recent_quarter',
            new_name='mostRecentQuarter',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='net_income_to_common',
            new_name='netIncomeToCommon',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='next_fiscal_year_end',
            new_name='nextFiscalYearEnd',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='number_of_analyst_opinions',
            new_name='numberOfAnalystOpinions',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='open_price',
            new_name='openPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='operating_cashflow',
            new_name='operatingCashflow',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='operating_margins',
            new_name='operatingMargins',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='payout_ratio',
            new_name='payoutRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='peg_ratio',
            new_name='pegRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='pre_market_price',
            new_name='preMarketPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='previous_close',
            new_name='previousClose',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='price_hint',
            new_name='priceHint',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='price_to_book',
            new_name='priceToBook',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='price_to_sales_trailing_12_months',
            new_name='priceToSalesTrailing12Months',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='profit_margins',
            new_name='profitMargins',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='quick_ratio',
            new_name='quickRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='quote_type',
            new_name='quoteType',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='recommendation_key',
            new_name='recommendationKey',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='recommendation_mean',
            new_name='recommendationMean',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='regular_market_open',
            new_name='regularMarketOpen',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='regular_market_price',
            new_name='regularMarketPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='return_on_assets',
            new_name='returnOnAssets',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='return_on_equity',
            new_name='returnOnEquity',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='revenue_growth',
            new_name='revenueGrowth',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='revenue_per_share',
            new_name='revenuePerShare',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='revenue_quarterly_growth',
            new_name='revenueQuarterlyGrowth',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='sandp_52_week_change',
            new_name='sandp52WeekChange',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='shares_outstanding',
            new_name='sharesOutstanding',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='shares_percent_shares_out',
            new_name='sharesPercentSharesOut',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='shares_short',
            new_name='sharesShort',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='shares_short_previous_month_date',
            new_name='sharesShortPreviousMonthDate',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='shares_short_prior_month',
            new_name='sharesShortPriorMonth',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='short_name',
            new_name='shortName',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='short_percent_of_float',
            new_name='shortPercentOfFloat',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='short_ratio',
            new_name='shortRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='target_high_price',
            new_name='targetHighPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='target_low_price',
            new_name='targetLowPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='target_mean_price',
            new_name='targetMeanPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='target_median_price',
            new_name='targetMedianPrice',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='three_year_average_return',
            new_name='threeYearAverageReturn',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_assets',
            new_name='totalAssets',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_cash',
            new_name='totalCash',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_cash_per_share',
            new_name='totalCashPerShare',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_debt',
            new_name='totalDebt',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_revenue',
            new_name='totalRevenue',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='total_yield',
            new_name='totalYield',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='trailing_annual_dividend_yield',
            new_name='trailingAnnualDividendYield',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='trailing_eps',
            new_name='trailingEps',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='trailing_peg_ratio',
            new_name='trailingPegRatio',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='two_hundred_day_average',
            new_name='twoHundredDayAverage',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='ytd_return',
            new_name='ytdReturn',
        ),
        migrations.RenameField(
            model_name='stockinfo',
            old_name='zip_code',
            new_name='zipCode',
        ),
    ]
