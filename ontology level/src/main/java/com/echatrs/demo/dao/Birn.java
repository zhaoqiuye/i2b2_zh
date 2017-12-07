package com.echatrs.demo.dao;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Options;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import static org.apache.ibatis.mapping.StatementType.STATEMENT;

/**
 * @author caicai
 */
@Mapper
public interface Birn {

    /**
     * 返回c_hlevel
     *
     * @return
     */
    @Select({"select c_name from ${tableName} where c_hlevel=0"})
    @Options(statementType = STATEMENT)
    String getParentName(@Param(value = "tableName") String tableName);

    /**
     * 找一leve的数据
     *
     * @param level
     * @return
     */
    @Select("select c_name from ${tableName} where c_hlevel=${level} and UPPER(c_fullname) like upper(CONCAT(CONCAT('%', '${parentName}'),'%'));")
    @Options(statementType = STATEMENT)
    String[] getSonName(@Param(value = "level") Integer level, @Param(value = "parentName") String parentName,
                        @Param(value = "tableName") String tableName);

    /**
     * 根据中文找英文备份
     *
     * @param zname
     * @return
     */
    @Select("select DISTINCT(en_name) from ${tableName} where c_hlevel=${level} and c_name='${zname}'")
    @Options(statementType = STATEMENT)
    String getEnglish(@Param(value = "level") Integer level, @Param(value = "zname") String zname, @Param(value = "tableName") String tableName);
}
