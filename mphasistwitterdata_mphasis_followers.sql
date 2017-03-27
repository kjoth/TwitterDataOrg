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
-- Table structure for table `mphasis_followers`
--

DROP TABLE IF EXISTS `mphasis_followers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mphasis_followers` (
  `ID_mphasis_followers` int(11) DEFAULT NULL,
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
  `Count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mphasis_followers`
--

LOCK TABLES `mphasis_followers` WRITE;
/*!40000 ALTER TABLE `mphasis_followers` DISABLE KEYS */;
INSERT INTO `mphasis_followers` VALUES (1,'744173769330024448','Nagendra Giriraju','','2016-06-18 14:23:47',18,19,42,19,'India','False','nagendra378','None',1),(2,'21408644','Jack Hemple','','2009-02-20 16:10:24',8,43,621,35,'','False','jhemple','None',2),(3,'2869445281','Shreya Garg','','2014-10-21 20:29:04',2,4,15,6,'Ujjain, Madhya Pradesh','False','shreyagarg64','None',3),(4,'773740365165785088','Omni Integration','Innovative Mobile Apps Development Company.','2016-09-08 04:30:53',13,14,331,1,'Mountain View, CA','False','omniintegration','None',4),(5,'3094163996','sharada hibare','','2015-03-17 15:52:09',0,2,25,3,'','False','hibare_sharada','None',5),(6,'4563065953','Akshayghogare','','2015-12-15 05:22:41',13,14,327,9,'','False','ghogareakshay33','None',6),(7,'3069795344','chetana manvi','','2015-03-09 13:13:50',2,7,103,0,'','False','ManviChetana','None',7),(8,'462787150','Sriman','','2012-01-13 10:49:36',2,15,87,4,'Mangalore, India','False','srimannarayana6','Greenland',8),(9,'2466018090','Manjunath hebbar','','2014-04-27 11:59:56',1,3,5,0,'','False','manjuchebbar','None',9),(10,'715875305450147840','Datainox','Datainox is one of the leading company which provides different types of data entry services.','2016-04-01 12:15:47',25,141,374,5,'Austin, TX','False','DatainoxService','None',10),(11,'842956188509790209','Norta','Norta is an innovative Norwegian company, providing consulting, technology services, digital marketing, and training.','2017-03-18 04:29:51',1,4,15,0,'Oslo, Norge','False','norta_no','None',11),(12,'842852597719482368','Stringart.Lk','','2017-03-17 21:38:13',1,4,456,0,'','False','StringartLk','None',12),(13,'840182397840871424','raviekiran','','2017-03-10 12:47:48',2,8,198,2,'','False','iameravikiran','None',13),(14,'759264636604645377','HD Workstations','','2016-07-30 05:49:30',145,41,124,1,'','False','hdthinpc','Pacific Time (US & Canada)',14),(15,'387883925','Abhishek Kumar','Student, SPJIMR, TCS Employee, Blogger, Dreamer','2011-10-09 20:31:51',1823,75,152,14,'Mumbai ','False','abhishek4308','None',15),(16,'103280490','UNICOM Learning','Developing Professionals Creating Global Executives Enriching Organisations','2010-01-09 14:18:50',1127,286,198,52,'Bangalore, India','False','UNICOMLearning','New Delhi',16),(17,'781929786776047616','Shiv Kadam','','2016-09-30 18:52:43',1,10,30,72,'Pune, India','False','ShivKadam00','None',17),(18,'70311832','OzAbhee','','2009-08-31 04:51:57',2,4,18,0,'Sydney, Australia','False','ozabhee','Sydney',18),(19,'40679509','Ranjeet kumar','Strategic HR Professional(Independent)  Politics & Celebs\' drama ---Not Allowed','2009-05-17 15:45:14',4897,432,2100,1132,'Corporate Business News-Global','False','StrategicB2H','Midway Island',19),(20,'839603577584660480','Gopi Adhiseshan','','2017-03-08 22:27:46',2,0,154,1,'Bengaluru, India','False','AdhiseshanGopi','Pacific Time (US & Canada)',20),(21,'1374057266','Sambhaji B Chawale','Director - Technology and Innovation at PRIMUS Techsystems Private Limited. #Enterprise Solutions and management professional with 18 years of experience.','2013-04-23 07:24:28',7,38,37,2,'Pune','False','sambhajichawale','None',21),(22,'840506762759405568','Batsan Munkhbayar','KHUYAG','2017-03-11 10:16:42',19,62,982,1,'Stockholm, Sweden','False','BatsanMunkhbay1','None',22),(23,'65004476','jayK','In Konstant pursuit of new things~ Love the simple & subtle shades ~ Believer & Jesus Lover ~Part time Film Maker~ Techkey ~Makes use of every opportunity to :)','2009-08-12 10:56:40',22855,1161,2368,4830,'Bangalore/Chennai','False','mjaikanth','Hawaii',23),(24,'214048171','lalitha ramu','','2010-11-10 12:48:01',0,10,48,1,'','False','larakwt','None',24),(25,'332896715','AKASH DHANUKA','','2011-07-10 16:30:37',3,25,327,0,'','False','AkashDhanuka','Pacific Time (US & Canada)',25),(26,'1858554084','Arjun Bhandari','','2013-09-12 21:16:02',8,175,730,6,'Hyderabad','False','bhandari1478','None',26),(27,'23058765','Giacomo Squintani','My take on how Health Insurance software can help reduce costs and deliver a better customer experience to boost profits. Opinions mine,if not always original.','2009-03-06 12:43:30',898,314,560,91,'Bristol, UK','False','giactivus','London',27);
/*!40000 ALTER TABLE `mphasis_followers` ENABLE KEYS */;
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
