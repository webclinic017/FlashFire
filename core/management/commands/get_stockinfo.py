from django.core.management.base import BaseCommand
from .progress_bar import bar
from datetime import datetime
from django.db import connection
import yfinance as yf
import pandas as pd
import numpy as np
import csv
import os



NOW = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")


def get_symbols(file_path):
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"] + ".AX"
            symbols_list.append(symbol)

    print("Done.")
    return symbols_list


def get_symbols_df(symbols):
    with open("logs/query.txt", "w") as f:
        f.truncate(0)
    with open("logs/errors.txt", "w") as f:
        f.truncate(0)

    df = pd.DataFrame()
    skipped_symbols = []
    errors = 0
    loops = 2
    # loops = len(symbols)

    for t in range(loops):
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
        except Exception as e:
            errors += 0
            with open("logs/errors.txt", "a") as f: 
                f.write(f"{NOW}: {symbols[t]} Not Found \n")

        if len(df_entry.columns) < 130:
            print(df_entry)
            print(f"Skipping {symbols[t]}")
            skipped_symbols.append(symbols[t])
            continue

        df = pd.concat([df, df_entry], axis=0)
        print(symbols[t])
        print(len(df_entry.columns))
        print("")
        # bar("Retrieving Stock Info", t + 1, loops, symbols[t])


    df = df.replace(np.nan, None)
    df = df.reset_index(drop=True)
    df = df.rename(columns={"open": "openPrice", \
        "52WeekChange": "fiftyTwoWeekChange", "logo_url": "logoUrl"})
    df.drop(["zip", "companyOfficers", "fundInceptionDate", "lastSplitDate", \
        "lastDividendDate", "dateShortInterest", "fullTimeEmployees", "fax", "targetLowPrice", \
        "targetMedianPrice", "earningsGrowth", "numberOfAnalystOpinions", "targetMeanPrice", \
        "targetHighPrice", "recommendationMean", "annualHoldingsTurnover", "beta3Year", \
        "morningStarRiskRating", "forwardEps", "revenueQuarterlyGrowth", \
        "annualReportExpenseRatio", "totalAssets", "sharesShort", "sharesPercentSharesOut", \
        "fundFamily", "yield", "shortRatio", "sharesShortPreviousMonthDate", \
        "threeYearAverageReturn", "lastSplitFactor", "legalType", "morningStarOverallRating", \
        "earningsQuarterlyGrowth", "pegRatio", "ytdReturn", "lastCapGain", "shortPercentOfFloat", \
        "sharesShortPriorMonth", "impliedSharesOutstanding", "category", "fiveYearAverageReturn", \
        "volume24Hr", "navPrice", "toCurrency", "expireDate", "algorithm", "dividendRate", \
        "exDividendDate", "circulatingSupply", "startDate", "lastMarket", "maxSupply", \
        "openInterest", "volumeAllCurrencies", "strikePrice", "fromCurrency", \
        "fiveYearAvgDividendYield", "dividendYield", "coinMarketCapLink", "preMarketPrice", \
        "trailingPegRatio", "address2", "lastDividendValue", "trailingPE", "0", "", " "], \
        axis=1, inplace=True, errors="ignore")


    with connection.cursor() as cursor:
        # creating column list for insertion
        cursor.execute("SELECT symbol from core_stockinfo;")
        db_symbols = cursor.fetchall()
        cols = "`,`".join([str(i) for i in df.columns.tolist()])

        for i,row in df.iterrows():
            sql = "INSERT INTO `core_stockinfo` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            query = f"{sql}{tuple(row)}"
            try:
                print(row["symbol"])
                print(db_symbols)
                # print(sql, tuple(row))
                # cursor.execute(sql, tuple(row))
            except Exception as e:
                with open("logs/query.txt", "a") as f:
                    f.write(query + '\n')
                with open("logs/errors.txt", "a") as f:
                    f.write(f"{NOW}: Could not insert {symbols[i]}, {e} \n")
                errors += 1
            # print(sql, tuple(row))
            # bar("Inserting into Database", i + 1, loops, symbols[i])
    print(f"Skipped Symbols: {str(skipped_symbols)}")
    return df, errors


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')

        symbols = get_symbols(csv_path)
        df, errors = get_symbols_df(symbols)
        
        print("")
        df.to_csv("logs/raw_data.csv", index=False)
        print("")
        print(f"Task completed with {errors} error/s.")