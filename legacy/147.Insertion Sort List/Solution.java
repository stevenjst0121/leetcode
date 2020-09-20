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
    public ListNode insertionSortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode newHead = new ListNode(0);
        ListNode cur = head;
        ListNode p = newHead;
        ListNode cur_next = null;
        while(cur != null){
            cur_next = cur.next;
            
            while(p.next != null && p.next.val < cur.val){
                p = p.next;
            }
            
            cur.next = p.next;
            p.next = cur;
            cur = cur_next;
            p = newHead;
        }
        return newHead.next;
    }
}
