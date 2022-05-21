
CREATE TABLE `PE` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime,
  `exchange` varchar(45) DEFAULT NULL,
  `stock_name` varchar(45) DEFAULT NULL,
  `order_price` float,
  `order_status` varchar(45) DEFAULT NULL,
  `order_id` int long,
  `quantity` int long,
  `order_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ;