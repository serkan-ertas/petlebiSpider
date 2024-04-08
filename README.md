# Petlebi Products

## scrapping
run this command in CLI:

    scrapy runspider <spider_path> -o <product_name>.json

## writing the data to MySQL table
run import_products.py file

ensure you have the table named "petlebi" in your database,
and its columns:

| variable           	| type   	|
|---------------	|----------------	|
| URL      	| VARCHAR(255)    	|
| category      	| VARCHAR(50)    	|
| brand         	| VARCHAR(50)    	|
| name          	| VARCHAR(255)   	|
| price         	| DECIMAL(10, 2) 	|
| priceCurrency 	| VARCHAR(10)    	|
| images        	| TEXT           	|
| SKU           	| VARCHAR(50)    	|
