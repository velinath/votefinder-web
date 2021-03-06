UPDATE migration_version SET version = 10;
CREATE TABLE `main_gamefaction` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `game_id` INT(11) NOT NULL,
    `faction_name` VARCHAR(255) NOT NULL,
    `faction_type` ENUM ('town', 'scum', 'third', 'cult'),
    PRIMARY KEY (`id`),
    KEY `main_gamefaction_gameid` (`game_id`)
    ) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `main_playerfaction` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `player_id` INT(11) NOT NULL,
    `faction_id` INT(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `main_playerfaction_playerid` (`player_id`),
    KEY `main_playerfaction_factionid` (`faction_id`)
    ) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;