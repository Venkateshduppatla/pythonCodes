#CREATE DATABASE /*!32312 IF NOT EXISTS*/ `dbVenkatesh` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

#USE `dbVenkatesh`;

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
 # `status` varchar(1) DEFAULT NULL
) #ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */

--
-- Dumping data for table `bankcustomers`
--

#LOCK TABLES `bankcustomers` WRITE;
/*!40000 ALTER TABLE `bankcustomers` DISABLE KEYS */;
INSERT INTO `bankcustomers` VALUES ('1111','D Venkatesh','54345','C'),('222','venki','24456','O');
/*!40000 ALTER TABLE `bankcustomers` ENABLE KEYS */;
#UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
#DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`venkatesh`@`%`*/ /*!50003 TRIGGER `beforeDelete` BEFORE DELETE ON `bankcustomers` FOR EACH ROW BEGIN
IF old.balance > 100
THEN
SIGNAL SQLSTATE '45000';
END IF;
END */;;
#DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
