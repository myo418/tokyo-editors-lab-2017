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
;
