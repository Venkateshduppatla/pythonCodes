-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 165.22.14.77    Database: dbVenkatesh
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `dbVenkatesh`
--

-- CREATE DATABASE /*!32312 IF NOT EXISTS*/ `dbVenkatesh` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- USE `dbVenkatesh`;

--
-- Table structure for table `bankcustomers`
--

DROP TABLE IF EXISTS `bankcustomers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bankcustomers` (
  `accountNumber` varchar(16) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `balance` varchar(10) DEFAULT NULL,
  `status` varchar(1) DEFAULT NULL
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bankcustomers`
--

-- LOCK TABLES `bankcustomers` WRITE;
/*!40000 ALTER TABLE `bankcustomers` DISABLE KEYS */;
INSERT INTO `bankcustomers` VALUES ('1111','D Venkatesh','54345','C'),('222','venki','24456','O');
/*!40000 ALTER TABLE `bankcustomers` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
-- DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`venkatesh`@`%`*/ /*!50003 TRIGGER `beforeDelete` BEFORE DELETE ON `bankcustomers` FOR EACH ROW BEGIN
IF old.balance > 100
THEN
SIGNAL SQLSTATE '45000';
END IF;
END */;;
-- DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `billDetails`
--

DROP TABLE IF EXISTS `billDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billDetails` (
  `billNumber` int NOT NULL,
  `itemId` varchar(10) NOT NULL,
  `soldQuantity` int DEFAULT '1',
  PRIMARY KEY (`billNumber`,`itemId`),
  -- KEY `itemId` (`itemId`),
  CONSTRAINT `billDetails_ibfk_1` FOREIGN KEY (`billNumber`) REFERENCES `billHeader` (`billNumber`),
  CONSTRAINT `billDetails_ibfk_2` FOREIGN KEY (`itemId`) REFERENCES `item` (`itemId`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billDetails`
--

-- LOCK TABLES `billDetails` WRITE;
/*!40000 ALTER TABLE `billDetails` DISABLE KEYS */;
INSERT INTO `billDetails` VALUES (70001,'RYDS002',3),(70002,'BRU22',1),(70002,'RYDS001',2),(70003,'RYDS001',2),(70003,'RYDS002',1),(110001,'888',5),(110001,'Cont22',1),(110001,'VEGO2',1),(110002,'VEGO23',1),(110003,'RYDS001',2),(130002,'RYDS003',1),(130003,'Cont22',1);
/*!40000 ALTER TABLE `billDetails` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
-- DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`venkatesh`@`%`*/ /*!50003 TRIGGER `afterInsertDetails` AFTER INSERT ON `billDetails` FOR EACH ROW BEGIN
UPDATE item SET stockQuantity = (stockQuantity - new.soldQuantity) WHERE new.itemId = itemId;
END */;;
-- DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `billHeader`
--

DROP TABLE IF EXISTS `billHeader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billHeader` (
  `billNumber` int NOT NULL,
  `cashierId` varchar(10) DEFAULT NULL,
  `customerId` varchar(10) DEFAULT NULL,
  `billDate` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`billNumber`),
  -- KEY `cashierId` (`cashierId`),
--   KEY `customerId` (`customerId`),
  CONSTRAINT `billHeader_ibfk_1` FOREIGN KEY (`cashierId`) REFERENCES `cashier` (`cashierId`),
  CONSTRAINT `billHeader_ibfk_2` FOREIGN KEY (`customerId`) REFERENCES `customer` (`customerID`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billHeader`
--

-- LOCK TABLES `billHeader` WRITE;
/*!40000 ALTER TABLE `billHeader` DISABLE KEYS */;
INSERT INTO `billHeader` VALUES (70001,'DMGV022','DM752201','2022-05-12'),(70002,'DMGV022','DM752202','2022-05-12'),(70003,'DMGV022','DM752203','2022-05-12'),(110001,'DMGV020','DM1152201','2022-05-11'),(110002,'DMGV020','DM1152202','2022-05-11'),(110003,'DMGV020','DM1152205','2022-05-11'),(130002,'DMGV020','DM1352205','2022-05-13'),(130003,'DMGV021','DM1552205','2022-05-15');
/*!40000 ALTER TABLE `billHeader` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Temporary view structure for view `billReport`
--

DROP TABLE IF EXISTS `billReport`;
/*!50001 DROP VIEW IF EXISTS `billReport`*/;
-- SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `billReport` AS SELECT 
 1 AS `billNumber`,
 1 AS `billDate`,
 1 AS `itemId`,
 1 AS `Description`,
 1 AS `soldQuantity`,
 1 AS `Unit Price`,
 1 AS `totalPrice`*/;
-- SET character_set_client = @saved_cs_client;

--
-- Table structure for table `cashier`
--

DROP TABLE IF EXISTS `cashier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cashier` (
  `cashierId` varchar(10) NOT NULL,
  `cashierName` varchar(25) NOT NULL,
  PRIMARY KEY (`cashierId`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cashier`
--

-- LOCK TABLES `cashier` WRITE;
/*!40000 ALTER TABLE `cashier` DISABLE KEYS */;
INSERT INTO `cashier` VALUES ('DMGV020','Jagannadha Rao'),('DMGV021','Durga Girish'),('DMGV022','A B Gowtham'),('DMGV023','B Satish'),('DMGV024','N Hareesh');
/*!40000 ALTER TABLE `cashier` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customerID` varchar(10) NOT NULL,
  `customerName` varchar(20) NOT NULL,
  PRIMARY KEY (`customerID`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

-- LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('DM1152201','K Raju'),('DM1152202','M Kumar'),('DM1152205','M Poornima'),('DM1352205','A Hari'),('DM1552205','A Hari'),('DM752201','D Venkatesh'),('DM752202','Krishna Nag'),('DM752203','S Ramesh');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `error`
--

DROP TABLE IF EXISTS `error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `error` (
  `errorNumber` int NOT NULL,
  `errorDescription` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`errorNumber`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `error`
--

-- LOCK TABLES `error` WRITE;
/*!40000 ALTER TABLE `error` DISABLE KEYS */;
INSERT INTO `error` VALUES (45000,'Account cant be deleted');
/*!40000 ALTER TABLE `error` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `itemId` varchar(10) NOT NULL,
  `description` varchar(30) NOT NULL,
  `unitPrice` int NOT NULL,
  `stockQuantity` int NOT NULL,
  `supplierId` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`itemId`),
  -- KEY `supplierId` (`supplierId`),
  CONSTRAINT `item_ibfk_1` FOREIGN KEY (`supplierId`) REFERENCES `supplier` (`supplierId`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

-- LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES ('888','Biryani Rice',50,995,'R2010'),('BELL200','Bell Rice',50,998,'R2010'),('BRU22','Bru Coffee',60,198,'KCP2001'),('Cont22','Continental',80,298,'KCP2001'),('RYDS001','Shirt',499,94,'RYD22'),('RYDS002','Jean Shirt',599,95,'RYD22'),('RYDS003','Trouser',799,99,'RYD22'),('VEGO1','Onion',20,998,'VV3240'),('VEGO2','Potato',20,999,'VV3240'),('VEGO23','Tomato',60,999,'VV3240');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplierId` varchar(10) NOT NULL,
  `supplierName` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`supplierId`)
) -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

-- LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES ('KCP2001','Kumar Caffine Products'),('R2010','Ramu Rice Suppliers'),('RYD22','Raj Reymond Textiles'),('VV3240','Venkatesh Vegetables');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Current Database: `dbVenkatesh`
--

-- USE `dbVenkatesh`;

--
-- Final view structure for view `billReport`
--

/*!50001 DROP VIEW IF EXISTS `billReport`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`venkatesh`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `billReport` AS select `billDetails`.`billNumber` AS `billNumber`,`getDate`(`billDetails`.`billNumber`) AS `billDate`,`billDetails`.`itemId` AS `itemId`,`getDescription`(`billDetails`.`itemId`) AS `Description`,`billDetails`.`soldQuantity` AS `soldQuantity`,`getUnitPrice`(`billDetails`.`itemId`) AS `Unit Price`,(`billDetails`.`soldQuantity` * `getUnitPrice`(`billDetails`.`itemId`)) AS `totalPrice` from `billDetails` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-14 11:16:35
