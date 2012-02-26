class User
  include MongoMapper::Document

  key :name, String, :required => true
  key :email, String, :required => true
  key :crypted_password, String
  
  # TODO: add all kindsa validation
  

end
