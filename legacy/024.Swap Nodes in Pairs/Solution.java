/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import data.ListNode;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null){
            return null;
        }
        
        ListNode newHead = new ListNode(0);
        ListNode p = newHead;
        newHead.next = head;
        while(p != null && p.next != null && p.next.next != null){
            ListNode p1 = p.next;            
            ListNode p2 = p1.next;
            ListNode p3 = p2.next;
            p1.next = p3;
            p2.next = p1;
            p.next = p2; 
            p = p.next.next;
        }
        return newHead.next;
    }
}