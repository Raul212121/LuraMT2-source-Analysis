/*
 Navicat Premium Data Transfer

 Source Server         : Development
 Source Server Type    : MySQL
 Source Server Version : 50644
 Source Host           : 192.168.0.16:3306
 Source Schema         : player

 Target Server Type    : MySQL
 Target Server Version : 50644
 File Encoding         : 65001

 Date: 12/01/2021 19:47:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for biolog_monsters
-- ----------------------------
DROP TABLE IF EXISTS `biolog_monsters`;
CREATE TABLE `biolog_monsters`  (
  `mission` tinyint(2) UNSIGNED NOT NULL DEFAULT 0,
  `mob_vnum` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `chance` tinyint(3) UNSIGNED NOT NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of biolog_monsters
-- ----------------------------
INSERT INTO `biolog_monsters` VALUES (0, 591, 90);
INSERT INTO `biolog_monsters` VALUES (0, 601, 90);
INSERT INTO `biolog_monsters` VALUES (0, 602, 90);
INSERT INTO `biolog_monsters` VALUES (1, 4, 2);
INSERT INTO `biolog_monsters` VALUES (1, 5, 2);

SET FOREIGN_KEY_CHECKS = 1;
