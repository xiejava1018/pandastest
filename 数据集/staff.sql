/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : pandastest

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2022-01-22 16:23:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `staff_id` int(11) DEFAULT NULL,
  `staff_name` varchar(64) DEFAULT NULL,
  `staff_age` int(2) DEFAULT NULL COMMENT '年龄',
  `staff_gender` varchar(2) DEFAULT NULL COMMENT '性别',
  `staff_salary` double DEFAULT NULL COMMENT '薪水',
  `staff_depatment_id` int(2) DEFAULT NULL COMMENT '部门ID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
