package com.peng.config;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.autoconfigure.jdbc.DataSourceBuilder;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

/**
 * @author caicai
 * @date 2017/10/24
 */
@Configuration
public class PostgreConfig {
    @Bean(name = "postgresDb")
    @ConfigurationProperties(prefix = "spring.ds_post")
    public DataSource postgresDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "postgresJdbcTemplate")
    public JdbcTemplate postgresJdbcTemplate(@Qualifier("postgresDb")
                                                     DataSource dsPostgres) {
        return new JdbcTemplate(dsPostgres);
    }
}
