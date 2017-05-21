CREATE TABLE keywords (
  id int(11) NOT NULL AUTO_INCREMENT,
  article_id int(11) NOT NULL,
  keyword char(255) NOT NULL,
  type char(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY article_id (article_id,keyword),
  KEY index_keyword (keyword),
  KEY index_article_id (article_id)
);
