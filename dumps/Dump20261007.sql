-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: ecommdb
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('898229e12c6d');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refresh_tokens`
--

DROP TABLE IF EXISTS `refresh_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refresh_tokens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `token` varchar(255) NOT NULL,
  `expires_at` datetime NOT NULL,
  `revoked` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `refresh_tokens_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refresh_tokens`
--

LOCK TABLES `refresh_tokens` WRITE;
/*!40000 ALTER TABLE `refresh_tokens` DISABLE KEYS */;
INSERT INTO `refresh_tokens` VALUES (1,1,'e08b7857-0f1f-452f-b537-e40368004865','2026-10-13 17:42:28',0,'2026-10-06 17:42:28'),(2,1,'d015b182-74a1-4371-baae-d0bc34d1bc7c','2026-10-13 18:03:40',0,'2026-10-06 18:03:40'),(3,1,'2badf68f-7b49-437f-a3f1-d3e64df7804d','2026-10-13 18:33:30',0,'2026-10-06 18:33:30'),(4,1,'0e8c4f9e-8597-49b0-b4ca-f0d9fa34563c','2026-10-13 18:33:57',0,'2026-10-06 18:33:57'),(5,1,'e43bc364-ae99-410c-81e6-7a7266978f8f','2026-10-13 18:34:55',0,'2026-10-06 18:34:55'),(6,1,'2127f01b-2db6-419e-94da-239a529da5e7','2026-10-13 18:35:55',0,'2026-10-06 18:35:55'),(7,2,'41bf217b-af18-4e04-98e3-e17ff893e0c4','2026-10-13 18:37:20',0,'2026-10-06 18:37:20'),(8,2,'527c80c9-5978-4b39-b9fd-75f26dbf5c94','2026-10-13 18:38:33',0,'2026-10-06 18:38:33'),(9,2,'1fc07ffd-d3f7-48ce-bc73-6d228033ba30','2026-10-13 18:39:28',0,'2026-10-06 18:39:28'),(10,2,'cb06c54d-b5c2-4724-84f2-1b88625e3a4c','2026-10-13 18:42:46',0,'2026-10-06 18:42:46'),(11,2,'a701f5d4-5700-4bd3-8768-e13dcb89a422','2026-10-13 18:44:13',0,'2026-10-06 18:44:13'),(12,2,'174592a1-79c2-46a9-a46f-7ed09a698e62','2026-10-13 18:44:31',0,'2026-10-06 18:44:31'),(13,2,'ec918c1a-3b7e-4aa4-9f8a-48df498b8b47','2026-10-13 18:45:23',0,'2026-10-06 18:45:23'),(14,2,'fb5f3726-db76-4295-bee6-10e4b7d292f6','2026-10-13 18:46:13',0,'2026-10-06 18:46:13'),(15,2,'2f37737f-5036-42fc-91ac-e1b8461bc0cd','2026-10-13 18:47:36',0,'2026-10-06 18:47:36'),(16,2,'33b14481-488a-4527-8105-9614bd64345f','2026-10-13 18:47:43',0,'2026-10-06 18:47:43'),(17,2,'94f615aa-23f4-4f09-b4b3-c43201ee0e2e','2026-10-13 18:50:44',0,'2026-10-06 18:50:44'),(18,2,'95c87005-eba2-44d3-a5ab-542a80b0e73d','2026-10-13 18:50:53',0,'2026-10-06 18:50:53'),(19,2,'621dd194-8b94-476b-afe1-f237e2902478','2026-10-13 18:51:14',0,'2026-10-06 18:51:14'),(20,2,'1e336103-42a3-42f9-87ef-0ee83805398b','2026-10-13 18:53:38',0,'2026-10-06 18:53:38'),(21,1,'b02520b9-b097-4a0b-b00c-d496254cee1b','2026-10-13 18:58:09',0,'2026-10-06 18:58:09'),(22,2,'23ae5da4-c5cd-4139-ab3a-fa4430229e38','2026-10-13 18:59:48',0,'2026-10-06 18:59:48'),(23,1,'a6ba3d28-e7c6-41d1-9941-2d1837563cc5','2026-10-13 19:20:46',0,'2026-10-06 19:20:46'),(24,1,'7ed93ddc-f974-4d0a-9417-8674163aac83','2026-10-13 19:20:51',0,'2026-10-06 19:20:51'),(25,1,'a39f53fd-906b-4d8e-9511-e5c1dcc28e34','2026-10-13 19:22:21',0,'2026-10-06 19:22:21'),(26,1,'22500111-fe27-4aa0-afb6-795befd83a8c','2026-10-13 19:25:10',0,'2026-10-06 19:25:10');
/*!40000 ALTER TABLE `refresh_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'akshay@example.com','$2b$12$yVxwg9MiPLakf4fnMTw4luAcY5EROHdISUPzfZaI73jEMQq/nSxNW',1,0,0,'2026-10-06 16:13:52','2026-10-06 16:13:52'),(2,'aditya@example.com','$2b$12$sxiPfaIfjFyEbdYH2yf77OE7l8nuLXCh2gXUZiPppYnmlRB6Hcfj6',1,0,0,'2026-10-06 18:36:59','2026-10-06 18:36:59');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-07  1:09:29
