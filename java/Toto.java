package com.test;

public class Toto {
    private int num;

    private String msg;

    public Toto(final int n, final String s){
        this.num = n;
        this.msg = s;
    }

    public int getNum(){
        return num;
    }

    public String getMessage(){
        return msg;
    }

    public String getInfos(){
        return this.msg + " " + String.valueOf(this.num); 
    }
}