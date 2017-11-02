class Bucket:
	name =""
	max_volume = 0
	current_volume = 0

	def __init__(self,name,max_volume,current_volume):
		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getName(self):
		return self.name

	def getMaxVolume(self):
		return self.max_volume

	def getCurrentVolume(self):
		return self.current_volume

	def setMaxVolume(self, max_volume):
		self.max_volume = max_volume

	def setCurrentVolume(self, current_volume):
		self.current_volume = current_volume

	def transfer(self, bucket):
		available_volume = self.max_volume - self.current_volume
		#Use the smaller of the available volume and the volume of the second bucket as the transfer ammount.
		amount_transfer = min( available_volume, bucket.getCurrentVolume() )
		#Increase bucket's volume by transfer ammount
		self.current_volume = self.current_volume + amount_transfer
		#decrease second bucket's volume by transfer ammount
		bucket.setCurrentVolume( bucket.getCurrentVolume() - amount_transfer )


	# Using if statements isntead of the min built in function
	# def transferVolume(self, new_bucket):
	# 	difference = self.max_volume - self.current_volume

	# 	if new_bucket.getCurrentVolume() > 0 and new_bucket.getCurrentVolume() > difference:
	# 		self.current_volume = self.current_volume + difference
	# 		new_bucket.setCurrentVolume( new_bucket.getCurrentVolume() - difference )

	# 	elif new_bucket.getCurrentVolume() > 0 and new_bucket.getCurrentVolume() <= difference:
	# 		self.current_volume = self.current_volume + new_bucket.getCurrentVolume()
	# 		new_bucket.setCurrentVolume(0)


bucket1 = Bucket("Waterbottle", 3, 1)

bucket2 = Bucket("Large Bucket", 20, 15)

print(bucket1.getCurrentVolume())

print(bucket2.getCurrentVolume())

bucket1.transfer(bucket2)

print(bucket1.getCurrentVolume())

print(bucket2.getCurrentVolume())
