package com.example.demo;


 


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;
 
@SpringBootApplication
public class Demo2Application implements CommandLineRunner {
     
    @Autowired
    private JdbcTemplate jdbcTemplate;
     
    public static void main(String[] args) {
        SpringApplication.run(Demo2Application.class, args);
    }
 
    @Override
    public void run(String... args) throws Exception {
        String sql = "INSERT INTO users (id,name, email,country, password) VALUES (?, ?, ?,?,?)";
         
        int result = jdbcTemplate.update(sql,7, "Ravi Kiran", "ravi.kumar@gmail.com","India", "ravi2011");
         
        if (result > 0) {
            System.out.println("A new row has been inserted.");
        }
         
    }
 
}
