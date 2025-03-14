import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month
my_email = "pradhyumsirupa@gmail.com"

df = pandas.read_csv("birthdays.csv")
people = df[(df["month"] == month) & (df["day"] == day)].to_dict(orient="records")

if len(people)>0:
    for i in range(len(people)):
        letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
        random_letter = random.choice(letters)

        with open(f"letter_templates/{random_letter}","r") as file:
            info_in_letter = file.read()
            wishes=info_in_letter.replace("[NAME]",(people[i]["name"]).capitalize())

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password="xfinptclbdvvmkfc")
        connection.sendmail(from_addr=my_email, to_addrs=people[i]["email"], msg=f"Subject:Happy Birthday \n\n{wishes} ")
        connection.close()

