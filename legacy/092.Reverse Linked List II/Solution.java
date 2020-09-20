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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null){
            return null;
        }
        
        ListNode newHead = new ListNode(0);
        newHead.next = head;
        ListNode p = newHead;
        
        for(int i = 1; i < m; i++){
            p = p.next;
        }
        
        ListNode pm = p.next;
        for(int j = 0; j < n-m; j++){
            ListNode pm1 = pm.next;
            pm.next = pm1.next;
            pm1.next = p.next;
            p.next = pm1;
        }
        return newHead.next;
    }
}