# figure out how many ways there are to represent TARGET_CENTS with pennies,
# nickles, dimes and quarts.  For Matthew's assignment on 4/30/2020
TARGET_CENTS = 50
pennies = range(0, TARGET_CENTS+1)
nickles = range(0, TARGET_CENTS+1, 5)
dimes = range(0, TARGET_CENTS+1, 10)
quarters = range(0, TARGET_CENTS+1, 25)
combo = 0
print "Combination\tPennies\tNickels\tDimes\tQuarters"
print "--------------------------------------------------"
for quarter in quarters:
    for dime in dimes:
        for nickle in nickles:
            for penny in pennies:
                if (quarter + dime + nickle + penny) == TARGET_CENTS:
                    combo += 1
                    print "%s\t\t%s\t%s\t%s\t%s" % (combo,pennies.index(penny),
                            nickles.index(nickle),
                            dimes.index(dime),
                            quarters.index(quarter))
