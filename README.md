# Bank Statement Transaction Extractor using Google Gemini

In this project i used how to extract structured financial transaction data from **bank statement images** using **Google Gemini's API** (`gemini-2.5-flash`)`

# Prompt strategy

**Role Assignment**
    - “An expert at extracting financial transaction data from bank statements

**Task scope**
    - "Analyze the provided image of a bank statement."

**Output Format**
    - "Extract all individual transactions into a Markdown table."

**Schema Declaration**
    - "The table should have the following columns: 'Date', 'Description', 'Amount', 'Balance'.",

**Conditional Formatting**
    - "For the 'Amount' column:"

**Rules**

    - " - If the transaction is a withdrawal or a debit, precede the amount with a minus sign (e.g., -200.00)."

    - " - If the transaction is a deposit or a credit, provide the amount as a positive number (e.g., 694.81)."

    "- Do not include a currency symbol.",

    "- The 'Previous balance' entry does not have an 'Amount', so leave that cell empty.",


# Output
**img1**

--- Extracted Transactions ---
Here is the extracted transaction data in a Markdown table format:

| Date       | Description                       | Amount  | Balance |
| :--------- | :-------------------------------- | :------ | :------ |
| 2003-10-08 | Previous balance                  |         | 0.55    |
| 2003-10-14 | Payroll Deposit - HOTEL           | 694.81  | 695.36  |
| 2003-10-14 | Web Bill Payment - MASTERCARD     | -200.00 | 495.36  |
| 2003-10-16 | ATM Withdrawal - INTERAC          | -21.25  | 474.11  |
| 2003-10-16 | Fees - Interac                    | -1.50   | 472.61  |
| 2003-10-20 | Interac Purchase - ELECTRONICS    | -2.99   | 469.62  |
| 2003-10-21 | Web Bill Payment - AMEX           | -300.00 | 169.62  |
| 2003-10-22 | ATM Withdrawal - FIRST BANK       | -100.00 | 69.62   |
| 2003-10-23 | Interac Purchase - SUPERMARKET    | -29.08  | 40.54   |
| 2003-10-24 | Interac Refund - ELECTRONICS      | 2.99    | 43.53   |
| 2003-10-27 | Telephone Bill Payment - VISA     | -6.77   | 36.76   |
| 2003-10-28 | Payroll Deposit - HOTEL           | 694.81  | 731.57  |
| 2003-10-30 | Web Funds Transfer - From SAVINGS | 50.00   | 781.57  |
| 2003-11-03 | Pre-Auth. Payment - INSURANCE     | -33.55  | 748.02  |
| 2003-11-03 | Cheque No. - 409                  | -100.00 | 648.02  |
| 2003-11-06 | Mortgage Payment                  | -710.49 | -62.47  |
| 2003-11-07 | Fees - Overdraft                  | -5.00   | -67.47  |
| 2003-11-08 | Fees - Monthly                    | -5.00   | -72.47  |

------------------------------

**img2**

--- Extracted Transactions ---

| Date | Description | Amount | Balance |
| :--------- | :---------------------------------- | :---------- | :---------- |
| 2021-06-01 | Opening Balance | | 4500.25 |
| 2021-05-31 | Best Embarcadero Parking | -25.00 | 4475.25 |
| 2021-05-31 | AIG Insurance Adjustment 20-21 | -121.45 | 4353.80 |
| 2021-06-01 | Ferry Building Marketplace | -76.80 | 4277.00 |
| 2021-06-01 | 76 Fuel 1150 Embarcadero | -87.25 | 4189.75 |
| 2021-06-03 | Trello Subscription | -35.20 | 4154.55 |
| 2021-06-03 | ATM Embarcadero Center | -200.00 | 3954.55 |
| 2021-06-04 | Blue Bottle Cofee | -11.00 | 3943.55 |
| 2021-06-04 | Best Embarcadero Parking | -35.00 | 3908.55 |
| 2021-06-04 | Docmosis Subscription | -50.00 | 3858.55 |
| 2021-06-04 | Embarcadero Centre Postage | -22.50 | 3836.05 |
| 2021-06-04 | Bill Payment - Silicon Valley Graphic | -450.00 | 3386.05 |
| 2021-06-04 | Blue Bottle Cofee | -11.00 | 3375.05 |
| 2021-06-07 | Ferry Building Marketplace | -85.50 | 3289.55 |
| 2021-06-07 | Dividend Share - Berkeley Group | 1500.60 | 4790.15 |
| 2021-06-07 | Canva Subscription | -125.00 | 4665.15 |
| 2021-06-07 | 76 Fuel 1150 Embarcadero | -95.00 | 4570.15 |
| 2021-06-08 | Embarcadero Centre Postage | -24.50 | 4545.65 |
| 2021-06-08 | ATM Embarcadero Center | -300.00 | 4245.65 |
| 2021-06-09 | Best Embarcadero Parking | -7.50 | 4238.15 |
| 2021-06-09 | Internet Transfer | 1000.00 | 5238.15 |
| 2021-06-09 | Dividend Share - McDonalds Corp | 2500.00 | 7738.15 |
| 2021-06-09 | Bill Payment - Silicon Valley Graphic | -4500.00 | 3238.15 |
| 2021-06-11 | Ferry Building Marketplace | -150.65 | 3087.50 |
| 2021-06-11 | Bill Payment - Electricity | -900.65 | 2186.85 |
| 2021-06-11 | Best Embarcadero Parking | -121.00 | 2065.85 |
| 2021-06-11 | Embarcadero Centre Postage | -54.75 | 2011.10 |


------------------------------

**img3**

--- Extracted Transactions ---
Here are the individual transactions extracted from the provided bank statement:

| Date       | Description       | Amount  | Balance  |
| :--------- | :---------------- | :------ | :------- |
| 2010-04-08 | Opening Balance   |         | 5234.09  |
| 2010-04-08 | Insurance         | 272.45  | 5506.54  |
| 2010-04-10 | ATM               | -200.00 | 5306.54  |
| 2010-04-12 | Internet Transfer | 250.00  | 5556.54  |
| 2010-04-12 | Payroll           | 2100.00 | 7656.54  |
| 2010-04-13 | Bill payment      | -135.07 | 7521.47  |
| 2010-04-14 | Direct debit      | -200.00 | 7321.47  |
| 2010-04-14 | Deposit           | 250.00  | 7567.87  |
| 2010-04-15 | Bill payment      | -525.72 | 7042.15  |
| 2010-04-17 | Bill payment      | -327.63 | 6714.52  |
| 2010-04-17 | Bill payment      | -729.96 | 5984.56  |
| 2010-04-18 | Bill payment      | -223.69 | 5710.87  |

------------------------------

# Challenges faced

* Learned how to get API_KEY from AI Studio
* Used .env file for API_KEY