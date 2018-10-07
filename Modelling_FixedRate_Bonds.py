
#Problem Statement:
"""Let's consider a hypothetical bond with a par value of 100, that pays 6% coupon semi-annually issued on January 15th, 2015 and set to mature on January 15th, 2016. 
The bond will pay a coupon on July 15th, 2015 and January 15th, 2016.
 The par amount of 100 will also be paid on the January 15th, 2016."""

 #SolutioN:
"""lets assume that we know the spot rates of the treasury as of January 15th,
 2015. The annualized spot rates are 0.5% for 6 months 
                                 and 0.7% for 1 year point. 
 Lets calculate the fair value of this bond."""

 # simple answer by discounting the CFS;
print(3/pow(1+0.005, 0.5) + (100+3)/(1+0.007))

# STEP:1  Settings

"""
set params:
#1. Today's date| set evaluation date = Today's date

#2 Spot Dates

#3 Spot rates

#4 Day count

#5 Calendar

#6 Interpolation

#7 Compounding

#8 Compounded freq

"""
import QuantLib as ql

#1. Today's date| set evaluation date = Today's date
todays_date = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = todays_date

#2 Spot Dates
spot_dates = [todays_date, ql.Date(15, 7, 2015), ql.Date(15, 1,2016)]

#3 Spot rates
spot_rates = [0.0, 0.005, 0.007]

#4 Day count
day_count = ql.Thirty360()

#5 Calendar
calendar = ql.UnitedStates()

#6 Interpolation
interpolation = ql.Linear()

#7 Compounding
compounding = ql.Compounded

#8 Compounded freq
compounding_freq = ql.Annual


# STEP: 2 Get Spot Curve
"""

get spotcurve:= ql.ZeroCurve
    params:
        spotDates,
        spotRates,
        dayCount,
        Calendar,
        interpolation,
        ..
        .
        CompoundingFrequency


"""

spot_curve = ql.ZeroCurve(spot_dates, spot_rates, day_count, calendar, interpolation,
                             compounding, compounding_freq)

# STEP:3 Create term Structure
"""

get Term Structure:= ql.YieldTermStructureHandle
    params:
        spotCurve
"""
spot_curve_Handle = ql.YieldTermStructureHandle(spot_curve)


# STEP:4 Setting up Bond Properties
"""

get Schedule:= ql.Schedule
    params:
        (issue_date, 
         maturity_date,
         tenor,
         calendar, 
         bussiness_convention,
         bussiness_convention, 
         date_generation, 
         month_end)
"""


issue_date = ql.Date(15, 1, 2015)
maturity_date = ql.Date(15, 1, 2016)
tenor = ql.Period(ql.Semiannual)
#calendar = ql.UnitedStates()
bussiness_convention = ql.Unadjusted
date_generation = ql.DateGeneration.Backward
month_end = False
schedule = ql.Schedule (issue_date, maturity_date, tenor, calendar, bussiness_convention,
                            bussiness_convention , date_generation, month_end)
print(list(schedule))


# Now lets build the coupon
day_count = ql.Thirty360()
coupon_rate = .06
coupons = [coupon_rate]

# Now lets construct the FixedRateBond
settlement_days = 0
face_value = 100
fixedrate_bond = ql.FixedRateBond(settlement_days, face_value, schedule, coupons, day_count)

# STEP:5 Setting up Bond Engine
# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bond_engine = ql.DiscountingBondEngine(spot_curve_Handle)
fixedrate_bond.setPricingEngine(bond_engine)

# Finally the price
print(fixedrate_bond.NPV())
