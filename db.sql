/*
SQLyog Professional v12.5.1 (64 bit)
MySQL - 10.4.16-MariaDB : Database - absensipkb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`absensipkb` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `absensipkb`;

/*Table structure for table `karyawan` */

DROP TABLE IF EXISTS `karyawan`;

CREATE TABLE `karyawan` (
  `nik` varchar(20) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`nik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `karyawan` */

insert  into `karyawan`(`nik`,`nama`,`created_at`,`active`) values 
('09','Alwai','2021-01-18 22:14:39',1),
('2000','Thamrein','2021-01-18 22:27:57',1),
('2105','Erza Fahmi Fasya','2021-01-18 22:23:59',1),
('91','Gelas','2021-01-18 22:00:19',1);

/*Table structure for table `kehadiran` */

DROP TABLE IF EXISTS `kehadiran`;

CREATE TABLE `kehadiran` (
  `id` bigint(255) NOT NULL,
  `nik_karyawan` varchar(50) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nik_karyawan` (`nik_karyawan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `kehadiran` */

insert  into `kehadiran`(`id`,`nik_karyawan`,`timestamp`) values 
(1,'11181024','2021-01-16 21:09:48'),
(3,'11181028','2021-01-16 23:03:13');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
