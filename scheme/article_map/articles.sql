CREATE TABLE articles (
  id int(11) NOT NULL AUTO_INCREMENT,
  title char(255) NOT NULL,
  media_name char(255) NOT NULL,
  published_at datetime NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY title (title,media_name),
  KEY index_title (title)
);
