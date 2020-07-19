CREATE TABLE users
(
   user_id INT,
   affiliate_code INT,
   created TIMESTAMP
);

INSERT INTO users
   (
   user_id,
   affiliate_code,
   created
   )
SELECT
   s as user_id,
   s + 1000 as affiliate_code,
   NOW() as created
FROM
   GENERATE_SERIES(1,1000) as s(a);