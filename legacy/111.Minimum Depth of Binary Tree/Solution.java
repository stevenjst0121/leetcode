/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package run;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Arrays;

/**
 *
 * @author Siteng Jin
 */
public class Solution {    
    public int minDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        
        if(left == 0 || right == 0){
            return left + right + 1;
        } else {
            return Math.min(left, right) + 1;
        }
    }
}
