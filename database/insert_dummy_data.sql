CREATE TABLE tables (
	user_id INT,
    affiliate_code CHAR(100),
    created TIMESTAMP
);

INSERT INTO tables
(
user_id,
affiliate_code,
created
)
SELECT
   s as user_id,
   CAST((1000 + s) as CHAR) as affiliate_code,
   NOW() as created
FROM
   GENERATE_SERIES(1,1000) as s(a);