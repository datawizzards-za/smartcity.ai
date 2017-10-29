package com.itechhub.datawizards.smartcityai.models;

import java.io.Serializable;

public class Address_ implements Serializable {
    private String line1;
    private String line2;
    private String city;
    private String province;
    private String postalCode;
    private String coordinates;

    public Address_(String line1, String line2, String city, String province, String postalCode, String coordinates) {
        this.line1 = line1;
        this.line2 = line2;
        this.city = city;
        this.province = province;
        this.postalCode = postalCode;
        this.coordinates = coordinates;
    }

    public String getLine1() {
        return line1;
    }

    public void setLine1(String line1) {
        this.line1 = line1;
    }

    public String getLine2() {
        return line2;
    }

    public void setLine2(String line2) {
        this.line2 = line2;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }
}
