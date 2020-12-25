BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"login"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"e-mail"	TEXT,
	PRIMARY KEY("login")
);
CREATE TABLE IF NOT EXISTS "Patient" (
	"id"	INTEGER NOT NULL,
	"surname"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"patronym"	TEXT,
	"date_of_birth"	TEXT NOT NULL,
	"sex"	TEXT NOT NULL CHECK('ж' OR 'м'),
	"address"	TEXT NOT NULL,
	"phone_number"	TEXT NOT NULL,
	"next of kin"	TEXT,
	"doctor"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Analysis" (
	"id"	INTEGER NOT NULL,
	"patient"	INTEGER NOT NULL,
	"result"	TEXT NOT NULL,
	"image_dcm"	BLOB NOT NULL,
	"image_data_json"	TEXT,
	"image_jpg"	BLOB NOT NULL,
	"comment"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("patient") REFERENCES "Patient"("id")
);
COMMIT;
