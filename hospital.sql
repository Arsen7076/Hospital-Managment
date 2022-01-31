-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 30, 2022 at 06:04 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Department`
--

CREATE TABLE `Hospital_Department` (
  `Department_Id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Description` varchar(255) NOT NULL,
  `Level` int(11) NOT NULL,
  `Type_Number_Id` int(11) NOT NULL,
  `Parent_Department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Department`
--

INSERT INTO `Hospital_Department` (`Department_Id`, `Name`, `Description`, `Level`, `Type_Number_Id`, `Parent_Department`) VALUES
(4, 'Diagnostic', 'Bone Density Scan', 1, 1, 'Diagnostic'),
(8, 'Fluoroscopy', 'Fluoroscopy is a term invented by Thomas Edison during his early X-ray studies.', 2, 1, 'Radiology'),
(78, 'Accouting', 'Balancing patient accounts and taking payments for services rendered', 1, 2, 'Managment');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Doctor`
--

CREATE TABLE `Hospital_Doctor` (
  `Specalization` varchar(255) NOT NULL,
  `Biographical_Data` varchar(255) NOT NULL,
  `Doctor_Id` int(11) NOT NULL,
  `Staf_Id` int(11) NOT NULL,
  `Type_Room` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Doctor`
--

INSERT INTO `Hospital_Doctor` (`Specalization`, `Biographical_Data`, `Doctor_Id`, `Staf_Id`, `Type_Room`) VALUES
('Dermatologists', '31/05/1980', 14, 442, 'Medical'),
('Endocrinologist', '16/08/2000', 27, 568, 'Medical'),
('Ginekolog', '01/02/1988', 66, 487, 'Office');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Gender`
--

CREATE TABLE `Hospital_Gender` (
  `Gender_Type` int(11) NOT NULL,
  `Sex` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Gender`
--

INSERT INTO `Hospital_Gender` (`Gender_Type`, `Sex`) VALUES
(1, 'Male'),
(2, 'Female');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Patient`
--

CREATE TABLE `Hospital_Patient` (
  `Patient_ID` int(11) NOT NULL,
  `Patient_Name` varchar(255) NOT NULL,
  `Patient_Lastname` varchar(255) NOT NULL,
  `Birthdate` varchar(255) NOT NULL,
  `Patient_Gender` int(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Blood_Type` varchar(255) NOT NULL,
  `Patient_History_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Patient`
--

INSERT INTO `Hospital_Patient` (`Patient_ID`, `Patient_Name`, `Patient_Lastname`, `Birthdate`, `Patient_Gender`, `Address`, `Blood_Type`, `Patient_History_Id`) VALUES
(458, 'Agvan', 'Abgaryan', '07/24/1999', 1, 'Lennagan', '3 Rh+', 2),
(542, 'Mamikon', 'Tsarukyan', '23/08/1993', 1, 'Argavand', '1 Rh+', 1),
(658, 'Sergey', 'Vardanyan', '30/12/1993', 1, 'Avan', '4 Rh+', 3);

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Patient_History`
--

CREATE TABLE `Hospital_Patient_History` (
  `Patient_History_Id` int(11) NOT NULL,
  `Date_Of_Application` varchar(255) NOT NULL,
  `Complains` varchar(255) NOT NULL,
  `Admission_Doctor` varchar(255) NOT NULL,
  `Services_Provided` varchar(255) NOT NULL,
  `Date_Of_Discharge` varchar(255) NOT NULL,
  `Sick` varchar(255) NOT NULL,
  `Hospital_Room` varchar(255) NOT NULL,
  `Department_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Patient_History`
--

INSERT INTO `Hospital_Patient_History` (`Patient_History_Id`, `Date_Of_Application`, `Complains`, `Admission_Doctor`, `Services_Provided`, `Date_Of_Discharge`, `Sick`, `Hospital_Room`, `Department_ID`) VALUES
(1, '04/12/2018', 'Headache', 'Nazar Paroyan', 'prescribing drugs', '10/12/2018', 'prescribing drugs', 'Medical', 4),
(2, '03/07/2017', 'Breack foot', 'Harutyun Gasparyan', 'Gips', '19/07/2017', 'Breacking of bone', 'Medical', 4),
(3, '12/10/2021', 'High blood sugar', 'Sergey Vardanyan', 'Insulin', '12/10/2021', 'Diabet', 'Medical', 8);

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Room`
--

CREATE TABLE `Hospital_Room` (
  `Hospital_Room_Id` int(11) NOT NULL,
  `Room_Name` varchar(255) NOT NULL,
  `Doctor_Assistant` varchar(255) NOT NULL,
  `Department_Id` int(11) NOT NULL,
  `Description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Room`
--

INSERT INTO `Hospital_Room` (`Hospital_Room_Id`, `Room_Name`, `Doctor_Assistant`, `Department_Id`, `Description`) VALUES
(25, 'Medical', 'Babayan Karen', 4, '2 bed and TV'),
(39, 'Office', 'Garaqyan Edgar', 78, '2 table, 2 notebook'),
(56, 'Medical', 'Barsegyan Karen', 8, '2 bed and 1 TV');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Room_Type`
--

CREATE TABLE `Hospital_Room_Type` (
  `Room_Name` varchar(255) NOT NULL,
  `Type_Room` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Room_Type`
--

INSERT INTO `Hospital_Room_Type` (`Room_Name`, `Type_Room`) VALUES
('Medical', 1),
('Office', 2);

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Service`
--

CREATE TABLE `Hospital_Service` (
  `Service_Id` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Department_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Service`
--

INSERT INTO `Hospital_Service` (`Service_Id`, `Price`, `Name`, `Department_Id`) VALUES
(14, 5000, 'Chorionic gonadotropin', 8),
(23, 65000, 'Nervous system', 78),
(54, 50000, 'Breast Biopsy', 8),
(59, 20000, 'Oncology', 4),
(107, 30000, '3D breast ultrasound', 4);

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Shift`
--

CREATE TABLE `Hospital_Shift` (
  `Shift_Id` int(11) NOT NULL,
  `Department_Id` int(11) NOT NULL,
  `Staff_Id` int(11) NOT NULL,
  `Type_Of_Shift_Id` int(11) NOT NULL,
  `Schedule` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Shift`
--

INSERT INTO `Hospital_Shift` (`Shift_Id`, `Department_Id`, `Staff_Id`, `Type_Of_Shift_Id`, `Schedule`) VALUES
(15, 4, 784, 1, '2022-01-13'),
(24, 8, 658, 2, '2022-01-13'),
(36, 8, 568, 1, '2022-01-13'),
(64, 78, 487, 2, '2022-01-13'),
(74, 4, 45, 1, '2022-10-14'),
(79, 4, 442, 2, '2022-01-13');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Shift_Type`
--

CREATE TABLE `Hospital_Shift_Type` (
  `Type_Of_Shift_Id` int(11) NOT NULL,
  `Shift_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Shift_Type`
--

INSERT INTO `Hospital_Shift_Type` (`Type_Of_Shift_Id`, `Shift_name`) VALUES
(1, 'Day'),
(2, 'Night');

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Staff`
--

CREATE TABLE `Hospital_Staff` (
  `Staff_Id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Lastname` varchar(255) NOT NULL,
  `Birthdate` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Position` varchar(255) NOT NULL,
  `Department_Id` int(11) NOT NULL,
  `Gender_Type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Staff`
--

INSERT INTO `Hospital_Staff` (`Staff_Id`, `Name`, `Lastname`, `Birthdate`, `Address`, `Position`, `Department_Id`, `Gender_Type`) VALUES
(45, 'Samuel', 'Xukasyan', '12/10/1960', 'Halabyan 8/1', 'Narcoses ', 8, 1),
(442, 'Karen', 'Postolakyan', '01/02/1988', 'Komitas 33/7', 'Onkolog', 8, 1),
(487, 'Susan', 'Ghazaryan', '14/05/1990', 'Komitas 7/2', 'Family medicine', 8, 2),
(568, 'Arthur', 'Sedrakyan', '16/08/2000', 'Cheremushka 3/3', 'Ginekolog', 4, 2),
(658, 'Gyurnaz', 'Petrosyan', '19/07/1985', 'Exvard 45/4', 'Surgent', 78, 1),
(784, 'Nazar', 'Paroyan', '04/12/1984', 'Babayan 48a', 'Dermatologists', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Hospital_Type_Department`
--

CREATE TABLE `Hospital_Type_Department` (
  `Type_Number_Id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Hospital_Type_Department`
--

INSERT INTO `Hospital_Type_Department` (`Type_Number_Id`, `Name`) VALUES
(1, 'Medical'),
(2, 'Managment'),
(3, 'Technical');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Hospital_Department`
--
ALTER TABLE `Hospital_Department`
  ADD PRIMARY KEY (`Department_Id`),
  ADD KEY `Description` (`Description`),
  ADD KEY `Type_Number_Id` (`Type_Number_Id`,`Description`);

--
-- Indexes for table `Hospital_Doctor`
--
ALTER TABLE `Hospital_Doctor`
  ADD PRIMARY KEY (`Doctor_Id`),
  ADD KEY `Staf_ID` (`Staf_Id`),
  ADD KEY `Type_Room` (`Type_Room`) USING BTREE;

--
-- Indexes for table `Hospital_Gender`
--
ALTER TABLE `Hospital_Gender`
  ADD PRIMARY KEY (`Gender_Type`);

--
-- Indexes for table `Hospital_Patient`
--
ALTER TABLE `Hospital_Patient`
  ADD PRIMARY KEY (`Patient_ID`),
  ADD KEY `Patient_Gender` (`Patient_Gender`) USING BTREE,
  ADD KEY `Patient_History_Id` (`Patient_History_Id`);

--
-- Indexes for table `Hospital_Patient_History`
--
ALTER TABLE `Hospital_Patient_History`
  ADD PRIMARY KEY (`Patient_History_Id`),
  ADD KEY `Department_ID` (`Department_ID`),
  ADD KEY `Hospital_Room` (`Hospital_Room`);

--
-- Indexes for table `Hospital_Room`
--
ALTER TABLE `Hospital_Room`
  ADD PRIMARY KEY (`Hospital_Room_Id`),
  ADD KEY `Room_Name` (`Room_Name`) USING BTREE,
  ADD KEY `Department_Id` (`Department_Id`) USING BTREE;

--
-- Indexes for table `Hospital_Room_Type`
--
ALTER TABLE `Hospital_Room_Type`
  ADD PRIMARY KEY (`Room_Name`);

--
-- Indexes for table `Hospital_Service`
--
ALTER TABLE `Hospital_Service`
  ADD PRIMARY KEY (`Service_Id`),
  ADD KEY `Department_ID` (`Department_Id`);

--
-- Indexes for table `Hospital_Shift`
--
ALTER TABLE `Hospital_Shift`
  ADD PRIMARY KEY (`Shift_Id`),
  ADD KEY `Department_ID` (`Department_Id`),
  ADD KEY `Staf_ID` (`Staff_Id`),
  ADD KEY `Type_Of_Shift_Id` (`Type_Of_Shift_Id`) USING BTREE;

--
-- Indexes for table `Hospital_Shift_Type`
--
ALTER TABLE `Hospital_Shift_Type`
  ADD PRIMARY KEY (`Type_Of_Shift_Id`);

--
-- Indexes for table `Hospital_Staff`
--
ALTER TABLE `Hospital_Staff`
  ADD PRIMARY KEY (`Staff_Id`),
  ADD KEY `Department_ID` (`Department_Id`),
  ADD KEY `Gender_Type` (`Gender_Type`);

--
-- Indexes for table `Hospital_Type_Department`
--
ALTER TABLE `Hospital_Type_Department`
  ADD PRIMARY KEY (`Type_Number_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Hospital_Shift_Type`
--
ALTER TABLE `Hospital_Shift_Type`
  MODIFY `Type_Of_Shift_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Hospital_Department`
--
ALTER TABLE `Hospital_Department`
  ADD CONSTRAINT `Hospital_Department_ibfk_1` FOREIGN KEY (`Type_Number_Id`) REFERENCES `Hospital_Type_Department` (`Type_Number_Id`);

--
-- Constraints for table `Hospital_Doctor`
--
ALTER TABLE `Hospital_Doctor`
  ADD CONSTRAINT `Hospital_Doctor_ibfk_1` FOREIGN KEY (`Staf_Id`) REFERENCES `Hospital_Staff` (`Staff_Id`),
  ADD CONSTRAINT `Hospital_Doctor_ibfk_2` FOREIGN KEY (`Type_Room`) REFERENCES `Hospital_Room_Type` (`Room_Name`);

--
-- Constraints for table `Hospital_Patient`
--
ALTER TABLE `Hospital_Patient`
  ADD CONSTRAINT `Hospital_Patient_ibfk_1` FOREIGN KEY (`Patient_Gender`) REFERENCES `Hospital_Gender` (`Gender_Type`),
  ADD CONSTRAINT `Hospital_Patient_ibfk_2` FOREIGN KEY (`Patient_History_Id`) REFERENCES `Hospital_Patient_History` (`Patient_History_Id`);

--
-- Constraints for table `Hospital_Patient_History`
--
ALTER TABLE `Hospital_Patient_History`
  ADD CONSTRAINT `Hospital_Patient_History_ibfk_2` FOREIGN KEY (`Department_ID`) REFERENCES `Hospital_Department` (`Department_Id`),
  ADD CONSTRAINT `Hospital_Patient_History_ibfk_3` FOREIGN KEY (`Hospital_Room`) REFERENCES `Hospital_Room_Type` (`Room_Name`);

--
-- Constraints for table `Hospital_Room`
--
ALTER TABLE `Hospital_Room`
  ADD CONSTRAINT `Hospital_Room_ibfk_1` FOREIGN KEY (`Department_Id`) REFERENCES `Hospital_Department` (`Department_Id`),
  ADD CONSTRAINT `Hospital_Room_ibfk_2` FOREIGN KEY (`Room_Name`) REFERENCES `Hospital_Room_Type` (`Room_Name`);

--
-- Constraints for table `Hospital_Service`
--
ALTER TABLE `Hospital_Service`
  ADD CONSTRAINT `Hospital_Service_ibfk_1` FOREIGN KEY (`Department_Id`) REFERENCES `Hospital_Department` (`Department_Id`);

--
-- Constraints for table `Hospital_Shift`
--
ALTER TABLE `Hospital_Shift`
  ADD CONSTRAINT `Hospital_Shift_ibfk_1` FOREIGN KEY (`Department_Id`) REFERENCES `Hospital_Department` (`Department_Id`),
  ADD CONSTRAINT `Hospital_Shift_ibfk_2` FOREIGN KEY (`Staff_Id`) REFERENCES `Hospital_Staff` (`Staff_Id`),
  ADD CONSTRAINT `Hospital_Shift_ibfk_3` FOREIGN KEY (`Type_Of_Shift_Id`) REFERENCES `Hospital_Shift_Type` (`Type_Of_Shift_Id`);

--
-- Constraints for table `Hospital_Staff`
--
ALTER TABLE `Hospital_Staff`
  ADD CONSTRAINT `Hospital_Staff_ibfk_1` FOREIGN KEY (`Department_Id`) REFERENCES `Hospital_Department` (`Department_Id`),
  ADD CONSTRAINT `Hospital_Staff_ibfk_2` FOREIGN KEY (`Gender_Type`) REFERENCES `Hospital_Gender` (`Gender_Type`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
