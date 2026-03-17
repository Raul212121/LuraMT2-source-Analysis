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

 Date: 12/01/2021 19:47:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for biolog_missions
-- ----------------------------
DROP TABLE IF EXISTS `biolog_missions`;
CREATE TABLE `biolog_missions`  (
  `mission` tinyint(2) UNSIGNED NOT NULL,
  `required_lvl` tinyint(3) UNSIGNED NOT NULL DEFAULT 0,
  `required_item` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `required_item_count` tinyint(4) UNSIGNED NOT NULL DEFAULT 0,
  `cooldown` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `chance` tinyint(3) UNSIGNED NOT NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of biolog_missions
-- ----------------------------
INSERT INTO `biolog_missions` VALUES (0, 30, 30006, 10, 600, 70);
INSERT INTO `biolog_missions` VALUES (1, 40, 30047, 15, 600, 65);
INSERT INTO `biolog_missions` VALUES (2, 50, 30015, 15, 900, 60);
INSERT INTO `biolog_missions` VALUES (3, 60, 30050, 20, 900, 55);
INSERT INTO `biolog_missions` VALUES (4, 70, 30165, 25, 1800, 50);
INSERT INTO `biolog_missions` VALUES (5, 80, 30166, 30, 1800, 50);
INSERT INTO `biolog_missions` VALUES (6, 85, 30167, 40, 2700, 45);
INSERT INTO `biolog_missions` VALUES (7, 90, 30168, 50, 3600, 45);
INSERT INTO `biolog_missions` VALUES (8, 92, 30251, 10, 7200, 40);
INSERT INTO `biolog_missions` VALUES (9, 94, 30252, 20, 7200, 40);

SET FOREIGN_KEY_CHECKS = 1;
