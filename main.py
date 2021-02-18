# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer0 = 'Ruud Gullit'
scorer1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer0+' '+str(goal_0)+', ' + scorer1+' '+(str(goal_1))
report = scorer0+' scored in the '+str(goal_0)+'nd minute\n'+scorer1+ ' scored in the '+str(goal_1)+'th minute'
player = 'Ronald Koeman'
first_name = player[0:player.find(' ')]
last_name_len = len(player[(player.find(' ')+1):len(player)])
name_short = player[0]+'. '+player[-last_name_len:len(player)]
chant = str(first_name+'! ') * (len(first_name)-1) + str(first_name+'!')
good_chant = chant[-1] != ' '
print(good_chant)