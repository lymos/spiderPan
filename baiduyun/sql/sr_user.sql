# user table
drop table if exists sr_user;

create table sr_user(
    id          int(11) not null auto_increment,
    uk          bigint(20) not null default 0 comment "uk user identity",

    added_time int(11) not null default 0,
    update_time int(11) not null default 0,
    primary key(id),
    unique key(uk)
)ENGINE=InnoDB default charset=utf8 comment "user table";
