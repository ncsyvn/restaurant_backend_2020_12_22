-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `BillId` int NOT NULL AUTO_INCREMENT,
  `Type` int DEFAULT NULL,
  `Datetime` datetime DEFAULT NULL,
  `TotalMoney` decimal(19,4) DEFAULT NULL,
  `Description` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Weather` int DEFAULT NULL,
  `Temperature` int DEFAULT NULL,
  PRIMARY KEY (`BillId`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (13,0,'2020-12-15 07:00:00',3344000.0000,'Nhập sáng sớm',8,25),(17,0,'2020-12-16 15:36:42',3433000.0000,'Nhập sáng sớm',7,25),(19,0,'2020-12-17 15:42:03',3170000.0000,'Nhập sáng sớm',6,25),(25,1,'2020-12-15 16:00:00',NULL,'Cập nhật tới đêm',8,25),(26,1,'2020-12-16 16:36:42',NULL,'Cập nhật tới đêm',7,25),(27,1,'2020-12-17 16:42:03',NULL,'Cập nhật tới đêm',6,25),(61,1,'2020-11-13 12:54:59',0.0000,NULL,8,11),(62,1,'2020-11-13 12:56:03',30000.0000,'',8,11),(63,1,'2020-11-13 12:56:11',0.0000,NULL,8,11),(68,0,'2020-11-13 13:05:17',66.0000,'',8,11),(69,0,'2020-11-13 13:35:07',108.0000,'',8,11),(70,0,'2020-11-03 17:04:00',240000.0000,'',8,1),(71,1,'2020-12-18 16:42:03',720000.0000,'',5,5),(72,1,'2020-12-19 16:42:03',660000.0000,'',3,12),(73,1,'2020-12-20 16:42:03',384000.0000,'',7,3);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-22 21:55:40
