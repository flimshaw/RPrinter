# Master Entity class, gets extended by other datatypes
class Entity

	include MongoMapper::Document


	key :author, String
	key :type, String
	key :data, Array
	timestamps!


end

