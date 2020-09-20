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
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for(int n = 0; n < numRows; n++){
            List<Integer> row = new ArrayList<Integer>();
            for(int k = 0; k < n+1; k++){
                if(k == 0 || k == n){
                    row.add(1);
                } else {
                    row.add(res.get(n-1).get(k-1) + res.get(n-1).get(k));
                }
            }
            res.add(row);
        }
        return res;
    }
}
