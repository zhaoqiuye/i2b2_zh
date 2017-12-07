package com.echatrs.demo.domain;

import java.util.List;

/**
 * @author caicai
 */
public class MetaDomain {
    private String name;
    private List<List<Erchat>>children;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<List<Erchat>> getChildren() {
        return children;
    }

    public void setChildren(List<List<Erchat>> children) {
        this.children = children;
    }

    public MetaDomain(String name) {
        this.name = name;
    }
}
