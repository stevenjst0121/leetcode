/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>();
        if(rowIndex == 0){
            row.add(1);
            return row;
        }
        
        for(int k = 0; k <= rowIndex; k++){
            if(k == 0 || k == rowIndex){
                row.add(1);
            } else {
                row.add(getRow(rowIndex-1).get(k-1) + getRow(rowIndex-1).get(k));
            }
        }
        return row;
    }
}
