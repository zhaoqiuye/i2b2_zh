package com.peng;

import com.peng.exception.MyExceptionHandler;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.PropertySources;

/**
 * @author caicai
 */
@SpringBootApplication
@PropertySources(value = { @PropertySource("classpath:messages.properties") })
public class PostgreApplication {

	public static void main(String[] args) {
		SpringApplication.run(PostgreApplication.class, args);
	}
	@Bean
	public MyExceptionHandler myExceptionHandler(){
		return new MyExceptionHandler();
	}
}
