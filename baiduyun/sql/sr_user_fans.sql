# table user fans
drop table if exists sr_user_fans;

create table sr_user_fans(
    id              int(11) not null auto_increment,
    uid             int(11) not null default 0 comment "user id",
    fans_uk       bigint(20) not null default 0 comment "user identity",
    type            tinyint(1) not null default 0 comment "type",
    fans_uname    varchar(60) not null default "" comment "follow_uname",
    avatar_url      varchar(120) not null default "" comment "avatar_url",
    intro           varchar(255) not null default "" comment "intro",
    user_type       tinyint(1) not null default 0 comment "user_type",
    is_vip          tinyint(1) not null default 0 comment "is_vip",
    fans_count    int(11) not null default 0 comment "follow_count",
    fans_count      int(11) not null default 0 comment "fans_count",
    follow_time     int(11) not null default 0 comment "follow_time",
    pubshare_count  int(11) not null default 0 comment "pubshare_count",
    album_count     int(11) not null default 0 comment "album_count",

    added_time int(11) not null default 0,
    update_time int(11) not null default 0,
    primary key(id)
)ENGINE=InnoDB default charset=utf8 comment "user fans table";

