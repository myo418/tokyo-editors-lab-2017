CREATE TABLE locations (
  id int(11) NOT NULL AUTO_INCREMENT,
  keyword char(255) NOT NULL,
  geometry geometry NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY keyword (keyword),
  SPATIAL KEY sp_index (geometry),
  KEY index_keyword (keyword)
);
