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
        TreeLinkNode first = null;
        
        while(node != null){
            if(first == null){
                first = node.left;
            }
            
            if(node.left != null){
                node.left.next = node.right;
            } else {
                break;
            }
            
            if(node.next != null){
                node.right.next = node.next.left;
                node = node.next;
            } else {
                node = first;
                first = null;
            }
        }
    }
}
