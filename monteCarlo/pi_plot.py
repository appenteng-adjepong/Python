import montecarlo as mc

circle_radius = 300 # circle radius in pixels
window = (1920, 1200) # window resolutionclear

points = 10000 # number of total points

simulation = mc.MonteCarlo(window, circle_radius, points)
simulation.loop()