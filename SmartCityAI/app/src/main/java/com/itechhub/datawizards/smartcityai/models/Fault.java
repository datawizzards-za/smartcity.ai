package com.itechhub.datawizards.smartcityai.models;

import java.io.Serializable;

public class Fault implements Serializable {
    private String name;
    private String description;
    private User user;
    private Address_ address;

    public Fault(String name, String description, User user, Address_ address) {
        this.name = name;
        this.description = description;
        this.user = user;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Address_ getAddress() {
        return address;
    }

    public void setAddress(Address_ address) {
        this.address = address;
    }
}
