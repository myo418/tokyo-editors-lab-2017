select
    title,
    keywords.keyword,
    X(locations.geometry),
    Y(locations.geometry)
from
    keywords
inner join
    articles
on
    articles.id = keywords.article_id
inner join
    locations
on
    keywords.keyword = locations.keyword
where
    GLENGTH(GEOMFROMTEXT(CONCAT(
      'LineString(',
        X( locations.geometry ),' ',Y( locations.geometry ), ",",
        %s,' ',%s,
      ')'
  ))) < 0.0489831601679492
;
