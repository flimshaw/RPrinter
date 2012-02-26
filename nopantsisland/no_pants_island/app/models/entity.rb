class Entity
    include MongoMapper::Document 
    
    key :author, String
    key :type, String
    key :data, Array #Object?
  
end