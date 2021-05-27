CREATE DATABASE atm;

USE atm;

CREATE TABLE `custs` (
  `card_no` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `acc_type` varchar(50) NOT NULL,
  `bal` int(11) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `img_path` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

