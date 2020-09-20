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
        
        for(int n = 0; n <= rowIndex; n++){
            for(int k = n-1; k > 0; k--){
                row.set(k, row.get(k-1) + row.get(k));
            }
            row.add(1);
        }
        
        return row;
    }
}
