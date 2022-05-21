
CREATE TABLE `order_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  `exchange` varchar(45) DEFAULT NULL,
  `stock_name` varchar(45) DEFAULT NULL,
  `order_price` float,
  `order_status` varchar(45) DEFAULT NULL,
  `order_id` BIGINT,
  `quantity` BIGINT,
  `order_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ; 