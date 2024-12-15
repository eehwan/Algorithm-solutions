SELECT P.PRODUCT_CODE, T.AMOUNT*P.PRICE AS SALES FROM (SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AMOUNT FROM OFFLINE_SALE GROUP BY PRODUCT_ID) T LEFT JOIN PRODUCT P ON P.PRODUCT_ID = T.PRODUCT_ID ORDER BY T.AMOUNT*P.PRICE DESC, P.PRODUCT_CODE ASC;