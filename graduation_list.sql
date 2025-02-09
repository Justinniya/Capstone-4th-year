-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2025 at 01:39 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `monitoring_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `graduation_list`
--

CREATE TABLE `graduation_list` (
  `ui_id` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` varchar(10) NOT NULL,
  `year` varchar(10) NOT NULL,
  `section` varchar(50) NOT NULL,
  `major` varchar(100) NOT NULL,
  `units` varchar(100) NOT NULL,
  `status` varchar(222) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `graduation_list`
--

INSERT INTO `graduation_list` (`ui_id`, `name`, `age`, `year`, `section`, `major`, `units`, `status`) VALUES
('04-2122-026', 'Belleza', '22', '4th Year', 'UI-FB1-BSIT4-3', 'Information Technology', 'Complete', 'Graduating'),
('04-2122-907', 'Botea', '22', '4th Year', 'UI-FB1-BSIT4-3', 'Information Technology', 'Complete', 'Graduating'),
('11-1004-111', 'Emily Davis', '22', '4th Year', 'UI-FB4-BSCS4-2', 'Computer Science', 'Complete', 'Graduating'),
('11-1010-111', 'Olivia Harris', '22', '4th Year', 'UI-FB10-BSCS4-2', 'Computer Science', 'Complete', 'Graduating');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `graduation_list`
--
ALTER TABLE `graduation_list`
  ADD PRIMARY KEY (`ui_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
