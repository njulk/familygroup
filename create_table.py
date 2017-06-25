from sql import *

db=mysql()
if __name__=="__main__":

    sql='''create table IF NOT EXISTS link_user(
        userid varchar(200) NOT NULL PRIMARY KEY,
        groupid bigint(12),
        name varchar(100) ,
        nickname varchar(100) ,
        portrait varchar(100),
        age int,
        gender bit,
        birthday date,
        charactersignature varchar(100),
        registertime datetime NOT NULL
	    )DEFAULT CHARSET=utf8
    '''
    db.create_table(sql)



    sql='''create table IF NOT EXISTS familygroup(
        groupid bigint(12) NOT NULL PRIMARY KEY,
        createuserid varchar(200) NOT NULL,
        groupname varchar(100) ,
        groupportrait varchar(100),
        groupdescription varchar(100),
        setgrouptime datetime                                         
    )
    '''
    db.create_table(sql)

    sql='''create table IF NOT EXISTS event(
        eventid bigint(12) auto_increment NOT NULL PRIMARY KEY,
        createuserid varchar(200) NOT NULL,
        groupid bigint(12) NOT NULL,
        eventname varchar(100) NOT NULL,
        eventdescription varchar(200),
        eventpicture varchar(50),
        createtime datetime NOT NULL
    )
    '''
    db.create_table(sql)

    sql='''create table IF NOT EXISTS talk(
        talkid bigint auto_increment NOT NULL PRIMARY KEY,
        eventid bigint(12) NOT NULL,
        userid varchar(200) NOT NULL,
        talkcontent varchar(100),
        pictureurl varchar(100),
        time datetime   #time=2017-06-22 17:15:54
    )
    '''
    db.create_table(sql)


    sql='''create table IF NOT EXISTS comment(
        commentid bigint(12) auto_increment NOT NULL PRIMARY KEY,
        talkid bigint(12) NOT NULL,
        userid varchar(200) NOT NULL,
        commentcontent varchar(200) NOT NULL,
        time datetime
    )
    '''
    db.create_table(sql)

    sql='''create table IF NOT EXISTS reminder(
        reminderid bigint(12) auto_increment NOT NULL PRIMARY KEY,
        title varchar(50) NOT NULL,
        content varchar(100),
        remindtime datetime NOT NULL,
        createuserid bigint(12), NOT NULL
    )'''
    db.create_table


