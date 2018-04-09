# -*- coding: utf-8 -*-
print "Jedilni list"

jedilnilist = {}
main = open("main.txt", "w+")

while True:
    jed = raw_input("Vnesite jed:")
    cena = raw_input("Vnesite ceno:")
    jedilnilist[jed] = cena

    konec = raw_input("želite dodati še eno(da/ne)?")
    if konec.lower() == "ne":
        break
je
print "Jedilni list:"
main.write("Jedilni list:\n")

for jed in jedilnilist:
    print "Jed: " + jed + " Cena: " + str(jedilnilist[jed]) + "€"
    main.write("Jed: " + jed + " Cena: " + str(jedilnilist[jed]) + "€\n")
