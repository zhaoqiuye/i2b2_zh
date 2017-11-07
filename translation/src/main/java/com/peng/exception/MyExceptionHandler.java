package com.peng.exception;

import org.springframework.web.servlet.HandlerExceptionResolver;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

/**
 * @author caicai
 * @date 2017/10/25
 */
public class MyExceptionHandler implements HandlerExceptionResolver {

    @Override
    public ModelAndView resolveException(HttpServletRequest request, HttpServletResponse response, Object handler,
                                         Exception ex) {
        Map<String, Object> model = new HashMap<String, Object>();
        model.put("ex", ex.getMessage());

        // 根据不同错误转向不同页面
        if (ex instanceof BusinessException) {
            return new ModelAndView("/error/error-business", model);
        } else {
            return new ModelAndView("/error/error", model);
        }
    }
}