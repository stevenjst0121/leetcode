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
    public ListNode partition(ListNode head, int x) {
        if(head == null){
            return null;
        }
        
        ListNode newHead1 = new ListNode(0);
        ListNode newHead2 = new ListNode(0);
        ListNode p1 = newHead1;
        ListNode p2 = newHead2;
        ListNode p = head;
        while(p != null){
            if(p.val < x){
                p1.next = p;
                p1 = p1.next;
            } else if (p.val >= x) {
                p2.next = p;
                p2 = p2.next;
            }
            p = p.next;
        }
        
        p2.next = null;
        p1.next = newHead2.next;
        return newHead1.next;
    }
}