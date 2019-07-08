const Database = require('better-sqlite3')
const path = require('path')
const dbPath = path.join(__dirname,'../../../','/db','db.sqlite')
const db = new Database(dbPath);
const row = db.prepare('SELECT * FROM db ').all()
console.log(row);