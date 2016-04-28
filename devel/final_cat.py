print ('Hello friends')
nickname = input('How can I call your nickname?')
print ('Welcome' + nickname + ', please answer all these questions below by yes or no to see if you are good to have a cat')

first = input ('Do you like cat?')
second = input ('Do you looking for a cat?')
third = input ('Are you looking for a small cat?')
fourth = input (' Are you looking for a big cat?')
fifth = input ('Do you know how to take care of a cat?')
sixth = input ('Do you know how to train a cat?')
seventh = input ('Do you know how to play with a cat?')
eighth = input ('Do you take your cat to everywhere with you?')
ninth = input ('Do you enough age to own a cat?')

if first and second and third and fifth and sixth and seventh and eighth and ninth == 'yes':
   print ('The best choice for you is a small cat')
   print ('Check the nearest center in your location for your small cat.')
elif first and second and fourth and fifth and sixth and seventh and eighth and ninth == 'yes':
   print ('The best choice for you is a big cat')
   print ('Check the nearest center in your location for your big cat.')
elif first and sencond and fifth and ninth == 'no':
   print ('Sorry, you are not ready to adopt a cat.') 
