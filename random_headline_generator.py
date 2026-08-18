import random
# Random news headline generating function
def random_headline():
	# Lists of all options
	persons=["Madhuri Dixit","Sharukh Khan","Barak Obama","Donuld Trump","Salman Khan","Kriti Sanon","Ranbir Singh","Ranbir Kapoor","Vikey Kousal","Rahul Gandhi"]
	works=["driving","riding","eating"]
	objects_driving=["bus","tractor","auto","ambulence","jeep"]
	objects_riding=["bufflow","cycle","cow","dog","frog","ant","cat","Jebra","tiger"]
	objects_eating=["kaju katli","dog","frog","jelly fish","octopus","sheep"]
	locations=["Delhi Gate","Red ford","Howrah Bridge","Imambara","Dal lake","Sea link","Hawa Mahal","Trident Hotel","Taj Hotel","Taj Mahal"]

	again=True
	
	while again :
		
  		person=random.choice(persons)
  		work=random.choice(works)
	
		# Choosing the right list according to the work type
  		if work == "driving":
  			object=random.choice(objects_driving)
  		elif work == "riding":
    		object=random.choice(objects_riding)
  		else:
    		object=random.choice(objects_eating)
  			location=random.choice(locations)

		# Checking for Vowel or Consonant
  		if object[0] in ('a','e','i','o','u'):
    		a="an"
  		else:
    		a="a"

  		# Printing the Headline
  		print(person,"is",work,a,object,"at",location)

		# Checking if user wants to generate again
  		remark=input("Generate again (Y/N): ")
  		if remark=="N" or remark=="n":
			print("Ok Goodbye! hope you enjoyed it")
    		again=False
  		elif remark=="Y" or remark=="y":
    		print("New Headline is....")
  		else:
    		print("Wrong entry.....!")
      		break

random_headline()
