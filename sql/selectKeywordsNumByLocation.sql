SELECT
    keywords.keyword,
    count(keywords.keyword) as count
FROM
    keywords
INNER JOIN
    articles
ON
    articles.id = keywords.article_id
WHERE
    keywords.article_id in (
        select
            keywords.article_id
        from
            keywords
        where
            keywords.keyword = '%s'
        group by
            article_id
    ) AND keywords.type != 'LOCATION'
    AND published_at = '%s'
group by
    keywords.keyword
order by count desc
;
