create database play_music_db;

use play_music_db;
-- 这是一个用户信息表
create table t_user(
id int primary key auto_increment,
uname varchar(20),
password varchar(20)
);
-- 音乐表
create table t_music(
id int primary key auto_increment,
music_name varchar(255),
path varchar(255)

);
--关系表
/*
 * 这是本次项目的关键 有这个表我们才知道哪个用户有哪些歌曲
 * 不至于混乱
 * 所以这张表不但需要独立的ID，
 * 还需要两个外键和用户表，音乐表建立连接
 */
create table t_list(
id int primary key auto_increment,
mid int,
uid int,
constraint foreign key (mid) references t_music(id),
constraint foreign key (uid) references t_user(id)

);

show databases;
use play_music_db;
show tables;
desc t_list ;
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!这里和菜鸟教程上面的语法稍有不同，但是添加数据更加快速！！！！！！！！
-- 开始插入数据
insert t_user(uname,password) values('zs',123),('lisi',123);
-- 查询
select * from t_user tu;
