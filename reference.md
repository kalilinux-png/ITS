
CREATE TABLE `order_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  `exchange` varchar(45) DEFAULT NULL,
  `stock_name` varchar(45) DEFAULT NULL,
  `order_price` float,
  `order_status` varchar(455) DEFAULT NULL,
  `order_id` BIGINT,
  `quantity` BIGINT,
  `order_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ; 

error handeling , live testing , 

insert into order_table (exchange,stock_name,order_price,,quantity,order_type) values "NSE","VEDL",0.0,73,"BUY"