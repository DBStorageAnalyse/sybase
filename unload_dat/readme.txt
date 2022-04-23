# -*- coding: utf-8 -*-
  SYBASE 解析工具

在sqlserver解析工具基础上改编
先解析 出几个重要系统表， 然后通过这几个系统表的数据 来解析全部。


history =============================================================================
2016-05-05   V1.0.0

sybase dump


---------------------------------------------------------------------------------------
# create table tab_info(id integer primary key,tab_obj_id,user_name,tab_name,col_sum,nullable_sum)
# create table col_info(id integer primary key,tab_obj_id,col_id,col_name,col_x_type,col_u_type,col_len,prec,scale,collationid,seed,nullable_is,var_len_is,def_data)
# col_info给解析系统表用，只存几个系统表的列信息，或给没有系统表时手工解析单表用
# insert into col_info(tab_obj_id,col_id,col_name,col_x_type,col_u_type,col_len,prec,scale,collationid,seed,nullable_is,var_len_is,def_data)
values(1,1,'a',1,1,4,0,0,null,null,1,0,0,null)

