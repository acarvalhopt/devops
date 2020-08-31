db.createUser(
    {
      user  : "hello_user",
      pwd   : "hello_pass",
      roles : [ 
        { 
          role  : "readWrite", 
          db    : "hello_db" 
        } 
      ]
    }
)

db.new_collection.insert({ first: "fist_row" })