# coding: utf-8
 
require 'csv'
require 'pp'
require 'sqlite3'
 
def insCSV
  db = SQLite3::Database.new("app.db")
  #sql = "DELETE FROM table1"
  #db.execute(sql)
  CSV.foreach("./test.csv") do |row|
    sql = "insert into articles
          (col1, col2, col3, col4, col5, col6)
          values
          (?, ?, ?, ?, ?, ?)"
    db.execute(sql, row[0].to_i, row[1], row[2], row[3], row[4], row[5])
    puts row[1]
  end
  db.close
end
 
insCSV