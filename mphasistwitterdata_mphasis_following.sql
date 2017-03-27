-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mphasistwitterdata
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mphasis_following`
--

DROP TABLE IF EXISTS `mphasis_following`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mphasis_following` (
  `ID_mphasis_following` int(11) NOT NULL,
  `Twitter_ID` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Twitter_Name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Twitter_Description` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Created_At` datetime DEFAULT NULL,
  `Tweets_Count` int(11) DEFAULT NULL,
  `Followers_Count` int(11) DEFAULT NULL,
  `Following_Count` int(11) DEFAULT NULL,
  `Favourites_Count` int(11) DEFAULT NULL,
  `Location` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Verified_User` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Screen_Name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Time_Zone` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Count` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_mphasis_following`),
  UNIQUE KEY `id_mphasis_UNIQUE` (`ID_mphasis_following`),
  UNIQUE KEY `Twitter_following_id_UNIQUE` (`Twitter_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Table for Mphasis Twitter Account of People who are followed by Mphasis';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mphasis_following`
--

LOCK TABLES `mphasis_following` WRITE;
/*!40000 ALTER TABLE `mphasis_following` DISABLE KEYS */;
/*!40000 ALTER TABLE `mphasis_following` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-27 19:29:18
