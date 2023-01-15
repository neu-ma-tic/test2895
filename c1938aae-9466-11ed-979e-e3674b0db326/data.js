const Database = require("@replit/database")

const db = new Database()

function Save(key,value) {
	db.set(key, value).then(() => {})
}

function Load(key) {
	db.get(key).then(value => {return value});
}