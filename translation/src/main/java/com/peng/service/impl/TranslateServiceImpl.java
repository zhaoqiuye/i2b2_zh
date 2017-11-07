package com.peng.service.impl;


import com.peng.model.Translation;
import com.peng.service.TranslateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * @author caicai
 * @date 2017/10/25
 */
@Service
public class TranslateServiceImpl implements TranslateService {
    @Autowired
    @Qualifier("postgresJdbcTemplate")
    private JdbcTemplate postgresTemplate;

    @Override
    public List<String> getZn(String[] en) {
        String sql = "select zn from checklist where en=?;";
        Translation translation = null;
        List<String> zns = new ArrayList<>();
        try {
            for (String s : en) {
                /**
                 * 去掉空格
                 */
                String ss = s.replace(" ", "");
                translation = postgresTemplate.query(sql, new Object[]{ss}, resultSet -> {
                    Translation translation1 = new Translation();
                    while (resultSet.next()) {
                        String s1 = resultSet.getString("zn");
                        translation1.setZn(s1);
                    }
                    return translation1;
                });
                if (translation.getZn() == null) {
                    zns.add("待翻译");
                } else {
                    zns.add(translation.getZn());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return zns;
    }

}
