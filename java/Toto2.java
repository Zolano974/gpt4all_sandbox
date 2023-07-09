package com.test;

public class Toto2 {
    private int num;

    private String msg;

    private Titi titi;

    public Toto(final int n, final String s, final Titi titi){
        this.num = n;
        this.msg = s;
        this.titi = titi;
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

    public boolean isEveryThingOkay(){
        try{
            final var isOkay = titi.isMessageOkay(this.msg)
            return isOkay;
        }catch(Exception e){
            return null;
        }
    }
}