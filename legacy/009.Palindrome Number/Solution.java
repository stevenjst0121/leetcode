/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        
        int reversed_x = 0;
        int res = x;
        while(res > 0){
            reversed_x = reversed_x*10 + res%10;
            res = res/10;
        }
        if(reversed_x == x){
            return true;
        } else {
            return false;
        }
    }
}