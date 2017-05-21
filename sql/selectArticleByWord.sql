select
    title
from
    keywords
inner join
    articles
on
    articles.id = keywords.article_id
where
    keywords.keyword = '%s'
;
