package com.echatrs.demo.controller;

import com.echatrs.demo.service.ErchatService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * @author caicai
 */
@Controller
public class ErController {
    @Autowired
    private ErchatService erchatService;

    @GetMapping(value = "/echars")
    @ResponseBody
    public String get() {
        return erchatService.json();
    }

    @GetMapping(value = "/index")
    public String index() {
        return "/index";
    }
}
