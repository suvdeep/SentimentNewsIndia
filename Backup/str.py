a,b="asd", "asdd"

sql= "UPDATE `links` SET `text` = CONCAT(`text`, \'%s\') WHERE id =%s", %(a,b)
print sql