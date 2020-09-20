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
import java.util.LinkedList;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder.length == 0 || postorder.length == 0){
            return null;
        }
        
        int rootVal = postorder[postorder.length-1];
        TreeNode root = new TreeNode(rootVal);
        if(postorder.length == 1){
            return root;
        }
        
        int i = 0;
        for(; i < inorder.length; i++){
            if(inorder[i] == rootVal){
                break;
            }
        }
        if(i != 0){
            int[] in1 = Arrays.copyOfRange(inorder, 0, i);
            int[] out1 = Arrays.copyOfRange(postorder, 0, i);
            root.left = buildTree(in1, out1);
        }
        
        if(i != inorder.length-1){
            int[] in2 = Arrays.copyOfRange(inorder, i+1, inorder.length);
            int[] out2 = Arrays.copyOfRange(postorder, i, postorder.length-1);
            root.right = buildTree(in2, out2);
        }
        
        return root;
    }
}
