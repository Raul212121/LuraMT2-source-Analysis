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

 Date: 13/01/2021 16:59:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `account_id` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `name` varchar(24) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'NONAME',
  `job` tinyint(2) UNSIGNED NOT NULL DEFAULT 0,
  `voice` tinyint(1) NOT NULL DEFAULT 0,
  `dir` tinyint(2) NOT NULL DEFAULT 0,
  `x` int(11) NOT NULL DEFAULT 0,
  `y` int(11) NOT NULL DEFAULT 0,
  `z` int(11) NOT NULL DEFAULT 0,
  `map_index` int(11) NOT NULL DEFAULT 0,
  `exit_x` int(11) NOT NULL DEFAULT 0,
  `exit_y` int(11) NOT NULL DEFAULT 0,
  `exit_map_index` int(11) NOT NULL DEFAULT 0,
  `hp` int(11) NOT NULL DEFAULT 0,
  `mp` int(11) NOT NULL DEFAULT 0,
  `stamina` smallint(6) NOT NULL DEFAULT 0,
  `random_hp` smallint(5) NOT NULL DEFAULT 0 COMMENT 'if lvl 0, it will be negative',
  `random_sp` smallint(5) NOT NULL DEFAULT 0 COMMENT 'if lvl 0, it will be negative',
  `playtime` int(11) NOT NULL DEFAULT 0,
  `level` tinyint(2) UNSIGNED NOT NULL DEFAULT 1,
  `level_step` tinyint(1) NOT NULL DEFAULT 0,
  `st` smallint(3) NOT NULL DEFAULT 0,
  `ht` smallint(3) NOT NULL DEFAULT 0,
  `dx` smallint(3) NOT NULL DEFAULT 0,
  `iq` smallint(3) NOT NULL DEFAULT 0,
  `exp` int(11) NOT NULL DEFAULT 0,
  `gold` bigint(16) NULL DEFAULT NULL,
  `stat_point` smallint(3) NOT NULL DEFAULT 0,
  `skill_point` smallint(3) NOT NULL DEFAULT 0,
  `quickslot` tinyblob NULL,
  `ip` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '0.0.0.0',
  `part_main` mediumint(6) NOT NULL DEFAULT 0,
  `part_base` tinyint(4) NOT NULL DEFAULT 0,
  `part_hair` mediumint(4) NOT NULL DEFAULT 0,
  `part_sash` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `skill_group` tinyint(4) NOT NULL DEFAULT 0,
  `skill_level` blob NULL,
  `alignment` int(11) NOT NULL DEFAULT 0,
  `last_play` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `change_name` tinyint(1) NOT NULL DEFAULT 0,
  `mobile` varchar(24) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `sub_skill_point` smallint(3) NOT NULL DEFAULT 0,
  `stat_reset_count` tinyint(4) NOT NULL DEFAULT 0,
  `horse_hp` smallint(4) NOT NULL DEFAULT 0,
  `horse_stamina` smallint(4) NOT NULL DEFAULT 0,
  `horse_level` tinyint(2) UNSIGNED NOT NULL DEFAULT 0,
  `horse_hp_droptime` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `horse_riding` tinyint(1) NOT NULL DEFAULT 0,
  `horse_skill_point` smallint(3) NOT NULL DEFAULT 0,
  `gaya_coins` int(11) NOT NULL DEFAULT 0,
  `costume_options` int(2) NOT NULL DEFAULT 0,
  `gm_invisible` int(2) NOT NULL DEFAULT 0,
  `chatban_count` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `biolog_mission` tinyint(3) NOT NULL DEFAULT 0,
  `biolog_collected` int(3) NOT NULL DEFAULT 0,
  `biolog_cooldown_reminder` tinyint(1) NOT NULL DEFAULT 0,
  `biolog_cooldown` int(11) NOT NULL DEFAULT 0,
  `marble_mission` int(6) UNSIGNED NOT NULL DEFAULT 0,
  `marble_extanded_count` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `marble_killed` int(11) UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `account_id_idx`(`account_id`) USING BTREE,
  INDEX `name_idx`(`name`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 11 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Triggers structure for table player
-- ----------------------------
DROP TRIGGER IF EXISTS `MakeCharacter`;
delimiter ;;
CREATE TRIGGER `MakeCharacter` BEFORE INSERT ON `player` FOR EACH ROW BEGIN
	IF(new.`name` REGEXP '[^A-Za-z0-9]')THEN
		SET new.`name`=NULL;
	END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
