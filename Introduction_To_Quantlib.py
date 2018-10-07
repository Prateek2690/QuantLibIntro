
#%%
import QuantLib as ql

date = ql.Date(31, 3, 2015) # 31 March, 2015

# WalkThrough --

#1. Get day, month, year from the date
print(date.dayOfMonth(), date.month(), date.year())

#2. comparing the dates
date.weekday() == ql.Tuesday

#3. Airthmetics
#print(date+1)

#4 Constructing a Schedule of dates b/w date1 and date2; with Tenor tenor; With Calendar US
date1 = date
date2 = ql.Date(31, 3, 2016)
tenor = ql.Period(ql.Monthly)
calendar = ql.UnitedStates()
schedule = ql.Schedule(date1,\
                       date2,\
                       tenor,\
                       calendar,\
                       ql.Following,\
                       ql.Following,\
                       ql.DateGeneration.Forward,\
                       False)

#print(list(schedule))

#5 Interest Rate Class
# The InterestRate class can be used to store the interest rate with the compounding type, day count and the frequency of compounding. Below we show how to create an interest rate of 5.0% compounded annually, using Actual/Actual day count convention.

#a get the interest rate for annualRate = 0.05; dayCOunt = Actual/Actual; Compounded; Annual
annual_rate = 0.05
compound_type = ql.Compounded
day_count = ql.ActualActual()
frequency = ql.Annual
interest_rate = ql.InterestRate(annual_rate,\
                                day_count,\
                                compound_type,\
                                frequency)

#print(interest_rate.compoundFactor(3.0), pow(1.0+annual_rate,3))

#b equivalent Interest rate: A given interest rate can be converted into other types using the equivalentRate method as :
new_freq = ql.Semiannual
effective_rate = interest_rate.equivalentRate(compound_type, new_freq,1)
print(effective_rate.rate())