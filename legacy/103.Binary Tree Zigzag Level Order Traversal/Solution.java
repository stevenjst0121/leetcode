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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null){
            return res;
        }
        levelOrderHelper(res, root, 0);
        return res;
    }
    
    public void levelOrderHelper(List<List<Integer>> res, 
            TreeNode root, int height){
        if(root == null){
            return;
        }
        
        if(res.size() <= height){
            res.add(new LinkedList<Integer>());
        }
        if(height%2 != 0){
            ((LinkedList) res.get(height)).addFirst(root.val);
        } else {
            ((LinkedList) res.get(height)).addLast(root.val);
        }
        levelOrderHelper(res, root.left, height+1);
        levelOrderHelper(res, root.right, height+1);
    }
}
