name = "riza marcos"
print(name.title())


print(name.lower())
print(name.upper())



first_name ="ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

with_format = f"{first_name} {last_name}"
print(f"hello, {full_name.title()}!")


#spacing
print("Hello \t Wrold")
print("Hello \n World")


favorite_language = ' pyton '
print(favorite_language)

# To ensure that no whitespace exists at the right side of a string, use the rstrip()
print(favorite_language.rstrip())

#remove permanently
favorite_language.rstrip()

#remove left side white space
favorite_language.lstrip()
#both side
favorite_language.strip()
# We want to remove this prefix, so we can focus on
#just the part of the URL that users need to enter into an address bar.
fb_site = 'https://facebook.com'
fb_site = fb_site.removeprefix('https://')
print(fb_site)
