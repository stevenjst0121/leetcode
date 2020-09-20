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
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
        if(root == null){
            return res;
        }
        levelOrderHelper(res, root, 0);
        return res;
    }
    
    public void levelOrderHelper(LinkedList<List<Integer>> res, 
            TreeNode root, int height){
        if(root == null){
            return;
        }
        
        if(res.size() <= height){
            res.addFirst(new ArrayList<Integer>());
        }
        res.get(res.size()-height-1).add(root.val);
        levelOrderHelper(res, root.left, height+1);
        levelOrderHelper(res, root.right, height+1);
    }
}
