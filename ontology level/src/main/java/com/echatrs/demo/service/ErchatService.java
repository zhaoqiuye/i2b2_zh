package com.echatrs.demo.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.echatrs.demo.dao.Birn;
import com.echatrs.demo.domain.Erchat;
import com.echatrs.demo.domain.MetaDomain;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

/**
 * @author caicai
 */
@Service
public class ErchatService {
    @Resource
    private Birn birn;

    public String json() {
        Erchat erchat = new Erchat("i2b2");//根
        List<Erchat> erchatList1 = getErchatList("BIRN", "birn");
        List<Erchat> erchatList2 = getErchatList("Custom Metadata", "custom_meta");
        List<Erchat> erchatList3 = getErchatList("i2b2", "i2b2");
        List<Erchat> erchatList4 = getErchatList("Diagnoses", "icd10_icd9");
        Erchat birner = new Erchat("birn");
        birner.setChildren(erchatList1);
        Erchat cuser = new Erchat("custom");
        cuser.setChildren(erchatList2);
        Erchat i2b2er = new Erchat("i2b2");
        i2b2er.setChildren(erchatList3);
        Erchat diagon = new Erchat("icd_icd9");
        diagon.setChildren(erchatList4);
        List<Erchat> list = new ArrayList<>();
        list.add(birner);
        list.add(cuser);
        list.add(i2b2er);
        list.add(diagon);
        erchat.setChildren(list);
        return JSON.toJSONString(erchat, SerializerFeature.DisableCircularReferenceDetect);
    }

    private List<Erchat> getErchatList(String parent, String table_name) {
        List<Erchat> erchatList = new ArrayList<Erchat>();
        String[] ss = birn.getSonName(0, parent, table_name);//得到子元素
        for (String name : ss) {
            Erchat erchat1 = new Erchat(name);
            List<Erchat> erchatList1 = new ArrayList<>();
            String english = birn.getEnglish(0, name, table_name);
            String[] sonName = birn.getSonName(1, english, table_name);
            for (String s : sonName) {
                Erchat erchat2 = new Erchat(s);
                List<Erchat> erchatList2 = new ArrayList<>();
                String english2 = birn.getEnglish(1, s, table_name);
                String[] sonName2 = birn.getSonName(2, english2, table_name);
                for (String s2 : sonName2) {
                    Erchat erchat3 = new Erchat(s2);
                    List<Erchat> erchatList3 = new ArrayList<>();
                    String english3 = birn.getEnglish(2, s2, table_name);
                    String[] sonName3 = birn.getSonName(3, english3, table_name);
                    for (String s3 : sonName3) {
                        Erchat erchat4 = new Erchat(s3);
                        erchatList3.add(erchat4);
                    }
                    erchat3.setChildren(erchatList3);
                    erchatList2.add(erchat3);
                }
                erchat2.setChildren(erchatList2);
                erchatList1.add(erchat2);
            }
            erchat1.setChildren(erchatList1);
            erchatList.add(erchat1);
        }
        return erchatList;
    }
}
