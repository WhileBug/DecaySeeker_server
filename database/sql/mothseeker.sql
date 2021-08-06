/*
 Navicat Premium Data Transfer

 Source Server         : MothSeeker
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : mothseeker

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 06/08/2021 10:45:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for check_record
-- ----------------------------
DROP TABLE IF EXISTS `check_record`;
CREATE TABLE `check_record`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NULL DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of check_record
-- ----------------------------
INSERT INTO `check_record` VALUES (1, 0, '2021-08-05 18:08:14', 1);
INSERT INTO `check_record` VALUES (2, 0, '2021-08-05 20:28:34', 2);
INSERT INTO `check_record` VALUES (3, 0, '2021-08-05 20:30:33', 1);
INSERT INTO `check_record` VALUES (4, 0, '2021-08-05 21:01:01', 1);
INSERT INTO `check_record` VALUES (5, 0, '2021-08-05 21:15:53', 1);
INSERT INTO `check_record` VALUES (6, 0, '2021-08-06 10:40:15', 1);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wechat_username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone_number` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'WhileBug', '17883693551');

SET FOREIGN_KEY_CHECKS = 1;
