package com.echatrs.demo.domain;

import java.util.List;

/**
 * @author caicai
 */
public class Erchat {


    private String name;
    private List<Erchat> children;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Erchat> getChildren() {
        return children;
    }

    public void setChildren(List<Erchat> children) {
        this.children = children;
    }

    public Erchat(String name) {
        this.name = name;
    }
}
