CREATE TABLE IF NOT EXISTS bookmars
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	url TEXT NOT NULL,
	notes TEXT,
	date_added TEXT NOT NULL
)
