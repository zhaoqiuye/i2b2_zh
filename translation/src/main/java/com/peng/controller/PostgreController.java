package com.peng.controller;

import com.alibaba.fastjson.JSON;
import com.peng.service.TranslateService;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.impl.SLF4JLogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.text.html.HTML;
import java.util.List;
/**
 * @author caicai
 * @date 2017/10/24
 */
@Controller
public class PostgreController {
    private static final Log logger = SLF4JLogFactory.getLog(PostgreController.class);
    @Autowired
    private TranslateService translateService;

    @GetMapping(value = "/")
    public String index() {
        return "/login";
    }

    @GetMapping(value = "/test")
    public String test() {
        return "/test";
    }

    @PostMapping(value = "/translate")
    @ResponseBody
    public String getZn(String s, HttpServletResponse response, HttpServletRequest request) {
        response.setHeader("Access-Control-Allow-Origin", "*");
        String[] ss = s.split(",");
        List<String> zn = translateService.getZn(ss);
        return JSON.toJSONString(zn);
    }
}
