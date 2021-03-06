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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }
        
        int n = lists.length;
        while(n > 1){
            if(n%2 == 0){
                int k = n/2;
                for(int i = 0; i < k; i++){
                    lists[i] = mergeTwoLists(lists[i], lists[i+k]);
                }
                n = k;
            } else {
                int k = (n+1)/2;
                for(int i = 0; i < k-1; i++){
                    lists[i] = mergeTwoLists(lists[i], lists[i+k]);
                }
                n = k;
            }
        }
        return lists[0];
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        } else if (l2 == null){
            return l1;
        }
        
        ListNode head = new ListNode(0);
        ListNode p = head;
        ListNode p1 = l1;
        ListNode p2 = l2;
        while(p1 != null || p2 != null){
            if(p1 == null){
                p.next = p2;
                p = p.next;
                p2 = p2.next;
                continue;
            } else if (p2 == null){
                p.next = p1;
                p = p.next;
                p1 = p1.next;
                continue;
            }
            
            if(p1.val <= p2.val){
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        return head.next;
    }
}
