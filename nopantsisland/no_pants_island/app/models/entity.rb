class Entity
  include MongoMapper::Document

  key :author, String
  key :tag, String
  key :data, Array

end
