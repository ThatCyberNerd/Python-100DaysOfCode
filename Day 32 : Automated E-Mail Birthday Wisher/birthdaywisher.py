import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "[ENTER YOUR EMAIL HERE]"
MY_PASSWORD = "[ENTER PASSWORD]"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

today = dt.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
