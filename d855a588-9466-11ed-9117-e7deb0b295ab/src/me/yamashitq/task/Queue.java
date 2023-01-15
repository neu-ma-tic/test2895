package me.yamashitq.task;

import net.dv8tion.jda.api.entities.User;
import twitter4j.auth.AccessToken;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Queue {
    private static final Map<User, AccessToken> queue = new HashMap<>();

    public static void addQueue(User member, AccessToken token) {
        queue.put(member,token);
    }

    public static void removeQueue(User member) {
        queue.remove(member);
    }

    public static User getOneQueueMember() {
        List<User> list = new ArrayList<User>(queue.keySet());
        return list.get(0);
    }

    public static AccessToken getToken(User member) {
        return queue.get(member);
    }

    public static int getQueueMembers() {
        return queue.size();
    }

    public static boolean hasQueue() {
        return queue.entrySet().size() != 0;
    }

    public static boolean hasInQueue(User member) {
        return queue.containsKey(member);
    }
}
