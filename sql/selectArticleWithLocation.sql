select
    title,
    keywords.keyword,
    ASTEXT(locations.geometry)
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
    keywords.type = 'LOCATION'
    AND GLENGTH(GEOMFROMTEXT(CONCAT(
      'LineString(',
        X( locations.geometry ),' ',Y( locations.geometry ), ",",
        32.80589,' ',130.69181,
      ')'
  ))) < 0.489831601679492
;
