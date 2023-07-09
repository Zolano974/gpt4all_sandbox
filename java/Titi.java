package com.test;

public class Titi {

    public boolean isMessageOkay(final String msg){
        return true;
    }

    public boolean isThereAnIssue() throws Exception {
        throw new Exception("zob");
    }
}