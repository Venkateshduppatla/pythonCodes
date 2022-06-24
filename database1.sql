-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: dbSireesha
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BillDetails`
--

DROP TABLE IF EXISTS `BillDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BillDetails` (
  `BillNumber` int NOT NULL,
  `ItemID` varchar(10) NOT NULL,
  `SoldQty` int DEFAULT '1',
  PRIMARY KEY (`BillNumber`,`ItemID`),
  KEY `ItemID` (`ItemID`),
  CONSTRAINT `BillDetails_ibfk_1` FOREIGN KEY (`BillNumber`) REFERENCES `BillHeader` (`BillNumber`),
  CONSTRAINT `BillDetails_ibfk_2` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BillDetails`
--

LOCK TABLES `BillDetails` WRITE;
/*!40000 ALTER TABLE `BillDetails` DISABLE KEYS */;
INSERT INTO `BillDetails` VALUES (1,'AR801',4),(1,'AR890',2),(1,'SH900',2),(2,'AR890',2),(2,'SH900',2),(3,'AR801',50),(3,'SH900',2),(3,'T0023',2),(4,'AR890',5),(4,'T0023',3),(5,'SH900',3),(5,'T0023',3),(6,'AR801',5),(6,'SH900',3),(7,'AR801',5),(7,'T0023',5);
/*!40000 ALTER TABLE `BillDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BillHeader`
--

DROP TABLE IF EXISTS `BillHeader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BillHeader` (
  `BillNumber` int NOT NULL,
  `BillDate` date DEFAULT NULL,
  `CashierID` varchar(25) DEFAULT NULL,
  `CustomerID` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`BillNumber`),
  KEY `CashierID` (`CashierID`),
  KEY `CustomerID` (`CustomerID`),
  CONSTRAINT `BillHeader_ibfk_1` FOREIGN KEY (`CashierID`) REFERENCES `Cashier` (`CashierID`),
  CONSTRAINT `BillHeader_ibfk_2` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BillHeader`
--

LOCK TABLES `BillHeader` WRITE;
/*!40000 ALTER TABLE `BillHeader` DISABLE KEYS */;
INSERT INTO `BillHeader` VALUES (1,'2022-05-05','A11','C001'),(2,'2022-05-05','A11','C002'),(3,'2022-05-05','A12','C003'),(4,'2022-05-10','A12','C001'),(5,'2022-05-11','A11','C004'),(6,'2022-05-18','A11','C005'),(7,'2022-05-25','A13','C006');
/*!40000 ALTER TABLE `BillHeader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cashier`
--

DROP TABLE IF EXISTS `Cashier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cashier` (
  `CashierID` varchar(20) NOT NULL,
  `CashierName` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`CashierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cashier`
--

LOCK TABLES `Cashier` WRITE;
/*!40000 ALTER TABLE `Cashier` DISABLE KEYS */;
INSERT INTO `Cashier` VALUES ('A11','Raju'),('A12','Giri'),('A13','Satish');
/*!40000 ALTER TABLE `Cashier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `CustomerID` varchar(20) NOT NULL,
  `CustomerName` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('C001','Sireesha'),('C002','Sharvani'),('C003','Revathi'),('C004','Harika'),('C005','Satish'),('C006','Bhanu');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomerDetails`
--

DROP TABLE IF EXISTS `CustomerDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CustomerDetails` (
  `Account_number` int NOT NULL,
  `Customer_name` varchar(20) DEFAULT NULL,
  `Balance` int DEFAULT NULL,
  `Status` char(1) DEFAULT NULL,
  PRIMARY KEY (`Account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomerDetails`
--

LOCK TABLES `CustomerDetails` WRITE;
/*!40000 ALTER TABLE `CustomerDetails` DISABLE KEYS */;
INSERT INTO `CustomerDetails` VALUES (100,'Leela',600,'1'),(599,'Hari',200,'1'),(700,'Sirisha',900,'0'),(800,'Leela',500,'1'),(900,'Sirisha',800,'1');
/*!40000 ALTER TABLE `CustomerDetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`Sireesha`@`%`*/ /*!50003 TRIGGER `beforeDelete` BEFORE DELETE ON `CustomerDetails` FOR EACH ROW BEGIN
IF old.Balance > 100
THEN
SIGNAL SQLSTATE'45000';
END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Error`
--

DROP TABLE IF EXISTS `Error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Error` (
  `ErrorNumber` int NOT NULL,
  `ErrorMsg` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ErrorNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Error`
--

LOCK TABLES `Error` WRITE;
/*!40000 ALTER TABLE `Error` DISABLE KEYS */;
INSERT INTO `Error` VALUES (45000,'Error: Unable to Delete.');
/*!40000 ALTER TABLE `Error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Item`
--

DROP TABLE IF EXISTS `Item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Item` (
  `ItemID` varchar(10) NOT NULL,
  `Description` varchar(25) DEFAULT NULL,
  `UnitPrice` int NOT NULL,
  `SupplierID` varchar(15) DEFAULT NULL,
  `StockQty` int DEFAULT NULL,
  PRIMARY KEY (`ItemID`),
  KEY `SupplierID` (`SupplierID`),
  CONSTRAINT `Item_ibfk_1` FOREIGN KEY (`SupplierID`) REFERENCES `Supplier` (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Item`
--

LOCK TABLES `Item` WRITE;
/*!40000 ALTER TABLE `Item` DISABLE KEYS */;
INSERT INTO `Item` VALUES ('AR801','Ariel',300,'SU02',132),('AR890','Ariel Bar',50,'SU02',145),('MI670','Mixture',1000,'SU03',50),('SH900','Shampoo',100,'SU03',142),('T0023','ToothPaste',100,'SU01',39);
/*!40000 ALTER TABLE `Item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier`
--

DROP TABLE IF EXISTS `Supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier` (
  `SupplierID` varchar(20) NOT NULL,
  `SupplierName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier`
--

LOCK TABLES `Supplier` WRITE;
/*!40000 ALTER TABLE `Supplier` DISABLE KEYS */;
INSERT INTO `Supplier` VALUES ('SU01','Venkatesh'),('SU02','Nithin'),('SU03','Akhil');
/*!40000 ALTER TABLE `Supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `getDmartReport`
--

DROP TABLE IF EXISTS `getDmartReport`;
/*!50001 DROP VIEW IF EXISTS `getDmartReport`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `getDmartReport` AS SELECT 
 1 AS `BillNumber`,
 1 AS `BillDate`,
 1 AS `ItemID`,
 1 AS `Description`,
 1 AS `SoldQty`,
 1 AS `UnitPrice`,
 1 AS `TotalPrice`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `getDmartReport`
--

/*!50001 DROP VIEW IF EXISTS `getDmartReport`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`Sireesha`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `getDmartReport` AS select `BillDetails`.`BillNumber` AS `BillNumber`,(select `BillHeader`.`BillDate` from `BillHeader` where (`BillHeader`.`BillNumber` = `BillDetails`.`BillNumber`)) AS `BillDate`,`BillDetails`.`ItemID` AS `ItemID`,(select `Item`.`Description` from `Item` where (`Item`.`ItemID` = `BillDetails`.`ItemID`)) AS `Description`,`BillDetails`.`SoldQty` AS `SoldQty`,(select `Item`.`UnitPrice` from `Item` where (`Item`.`ItemID` = `BillDetails`.`ItemID`)) AS `UnitPrice`,(`BillDetails`.`SoldQty` * (select `Item`.`UnitPrice` from `Item` where (`Item`.`ItemID` = `BillDetails`.`ItemID`))) AS `TotalPrice` from `BillDetails` */;
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

-- Dump completed on 2022-05-14  6:16:09
