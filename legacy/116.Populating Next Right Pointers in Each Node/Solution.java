/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package run;

import data.*;
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
    public void connect(TreeLinkNode root) {        
        TreeLinkNode node = root;
        int height = 0;
        while(node != null){
            node = node.left;
            height++;
        }
        
        if(height != 0){
            TreeLinkNode[] store = new TreeLinkNode[height];
            connectHelper(root, store, 0);
        } else {
            return;
        }
        
    }
    
    public void connectHelper(TreeLinkNode root, TreeLinkNode[] store, int height){
        if(root == null){
            return;
        }
        
        TreeLinkNode node = store[height];
        if(node != null){
            node.next = root;
        }
        store[height] = root;
        connectHelper(root.left, store, height+1);
        connectHelper(root.right, store, height+1);
    }
}
