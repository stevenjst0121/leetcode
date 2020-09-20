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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Queue<TreeNode> que = new LinkedList<TreeNode>();
        if(root == null){
            return  res;
        }
        
        que.offer(root);
        while(!que.isEmpty()){
            int queSize = que.size();
            List<Integer> lvl = new ArrayList<Integer>();
            while(queSize > 0){
                if(que.peek().left != null){
                    que.offer(que.peek().left);
                }
                if(que.peek().right != null){
                    que.offer(que.peek().right);
                }
                lvl.add(que.poll().val);
                queSize--;
            }
            res.add(lvl);
        }
        return res;
    }
}
