-- MySQL dump 10.13  Distrib 8.4.10, for Linux (x86_64)
--
-- Host: localhost    Database: device_project
-- ------------------------------------------------------
-- Server version	8.4.10-0ubuntu0.26.04.1

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
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `categoryID` int NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(100) NOT NULL,
  `Description` text,
  `avgPriceRange` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,'Smartphone','Handheld cellular computing devices','$400 - $1200'),(2,'Laptop','Portable personal computers','$800 - $2500');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Device`
--

DROP TABLE IF EXISTS `Device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Device` (
  `deviceID` int NOT NULL AUTO_INCREMENT,
  `modelName` varchar(100) NOT NULL,
  `releaseYear` year DEFAULT NULL,
  `basePrice` decimal(7,2) DEFAULT NULL,
  `manufacturerID` int DEFAULT NULL,
  `categoryID` int DEFAULT NULL,
  PRIMARY KEY (`deviceID`),
  KEY `manufacturerID` (`manufacturerID`),
  KEY `categoryID` (`categoryID`),
  CONSTRAINT `Device_ibfk_1` FOREIGN KEY (`manufacturerID`) REFERENCES `Manufacturer` (`manufacturerID`),
  CONSTRAINT `Device_ibfk_2` FOREIGN KEY (`categoryID`) REFERENCES `Category` (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device`
--

LOCK TABLES `Device` WRITE;
/*!40000 ALTER TABLE `Device` DISABLE KEYS */;
INSERT INTO `Device` VALUES (1,'iPhone 17',2025,799.00,1,1),(2,'Galaxy S24',2024,799.99,2,1);
/*!40000 ALTER TABLE `Device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Device_OS`
--

DROP TABLE IF EXISTS `Device_OS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Device_OS` (
  `deviceID` int NOT NULL,
  `osID` int NOT NULL,
  PRIMARY KEY (`deviceID`,`osID`),
  KEY `osID` (`osID`),
  CONSTRAINT `Device_OS_ibfk_1` FOREIGN KEY (`deviceID`) REFERENCES `Device` (`deviceID`),
  CONSTRAINT `Device_OS_ibfk_2` FOREIGN KEY (`osID`) REFERENCES `Operating_System` (`osID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device_OS`
--

LOCK TABLES `Device_OS` WRITE;
/*!40000 ALTER TABLE `Device_OS` DISABLE KEYS */;
INSERT INTO `Device_OS` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `Device_OS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Device_Variant`
--

DROP TABLE IF EXISTS `Device_Variant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Device_Variant` (
  `deviceID` int NOT NULL,
  `variantNumber` int NOT NULL,
  `Color` varchar(50) DEFAULT NULL,
  `storageCapacity` varchar(50) DEFAULT NULL,
  `variantPrice` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`deviceID`,`variantNumber`),
  CONSTRAINT `Device_Variant_ibfk_1` FOREIGN KEY (`deviceID`) REFERENCES `Device` (`deviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device_Variant`
--

LOCK TABLES `Device_Variant` WRITE;
/*!40000 ALTER TABLE `Device_Variant` DISABLE KEYS */;
INSERT INTO `Device_Variant` VALUES (1,1,'Black Titanium','256GB',799.00),(1,2,'White Titanium','512GB',899.00),(2,1,'Phantom Black','256GB',799.99),(2,2,'Marble Gray','512GB',919.99);
/*!40000 ALTER TABLE `Device_Variant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manufacturer`
--

DROP TABLE IF EXISTS `Manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Manufacturer` (
  `manufacturerID` int NOT NULL AUTO_INCREMENT,
  `companyName` varchar(100) NOT NULL,
  `Country` varchar(100) DEFAULT NULL,
  `yearFounded` year DEFAULT NULL,
  PRIMARY KEY (`manufacturerID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manufacturer`
--

LOCK TABLES `Manufacturer` WRITE;
/*!40000 ALTER TABLE `Manufacturer` DISABLE KEYS */;
INSERT INTO `Manufacturer` VALUES (1,'Apple','USA',1976),(2,'Samsung','South Korea',1938);
/*!40000 ALTER TABLE `Manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Operating_System`
--

DROP TABLE IF EXISTS `Operating_System`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Operating_System` (
  `osID` int NOT NULL AUTO_INCREMENT,
  `osName` varchar(100) NOT NULL,
  `versionNumber` varchar(50) DEFAULT NULL,
  `Developer` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`osID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Operating_System`
--

LOCK TABLES `Operating_System` WRITE;
/*!40000 ALTER TABLE `Operating_System` DISABLE KEYS */;
INSERT INTO `Operating_System` VALUES (1,'iOS','18','Apple'),(2,'Android','14','Google');
/*!40000 ALTER TABLE `Operating_System` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-23 19:30:58
