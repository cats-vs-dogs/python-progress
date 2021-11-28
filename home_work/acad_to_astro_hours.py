# INPUTS:

# number of acedmic hours in the program:
acad_hours = 64

# academis hour duration in minutes:
acad_hour_dur = 40

# break frequency, number of academic hours before each break:
break_freq = 3

# break duration in minutes:
break_dur = 15


# CALCULATION:

# number of breaks:
num_breaks = acad_hours // break_freq

# astronomical hours in the program:
astro_hours = (acad_hours*acad_hour_dur + num_breaks*break_dur) / 60

print(round(astro_hours,2))