select
    locations.keyword,
    X(locations.geometry),
    Y(locations.geometry)
from
    locations
where
    GLENGTH(GEOMFROMTEXT(CONCAT(
      'LineString(',
        X( locations.geometry ),' ',Y( locations.geometry ), ",",
        %s,' ',%s,
      ')'
  ))) < 0.089831601679492
