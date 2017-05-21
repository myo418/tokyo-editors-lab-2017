SELECT
    articles.title,
    articles.media_name,
    articles.published_at,
    keywords.keyword,
    keywords.type
FROM
    keywords
INNER JOIN
    articles
ON
    articles.id = keywords.article_id
WHERE keywords.article_id in (
    select
        keywords.article_id
    from
        keywords
    where
        keywords.keyword = '%s'
    group by
        article_id
);
