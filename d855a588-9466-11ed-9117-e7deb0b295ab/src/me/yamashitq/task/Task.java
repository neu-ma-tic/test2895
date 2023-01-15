package me.yamashitq.task;

import me.yamashitq.Main;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.User;
import twitter4j.IDs;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.auth.AccessToken;
import twitter4j.conf.ConfigurationBuilder;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class Task extends Thread {
    private static final List<Long> followerIDS = new ArrayList<>();
    public static int removefriend = 0;
    public static boolean a = false;

    @Override
    public void run() {
        while (Main.isStarted()) {
            try {
                if (Queue.hasQueue()) {
                    User member = Queue.getOneQueueMember();
                    try {
                        followerIDS.clear();
                        removefriend = 0;
                        a = false;
                        AccessToken token = Queue.getToken(member);
                        ConfigurationBuilder cb = new ConfigurationBuilder()
                                .setOAuthConsumerKey(Main.getConsumerKey())
                                .setOAuthConsumerSecret(Main.getSecretKey())
                                .setOAuthAccessToken(token.getToken())
                                .setOAuthAccessTokenSecret(token.getTokenSecret());
                        Twitter twitter = new TwitterFactory(cb.build()).getInstance();
                        EmbedBuilder embedBuilder = new EmbedBuilder()
                                .setTitle("フォロワー解除開始します！")
                                .appendDescription("開始前人数: " + twitter.verifyCredentials().getFollowersCount() + "人")
                                .setColor(Color.ORANGE);
                        member.openPrivateChannel().complete().sendMessage(embedBuilder.build()).queue();
                        Thread.sleep(500);
                        IDs ids = twitter.getFollowersIDs(twitter.getScreenName(), -1);
                        for (long l : ids.getIDs()) {
                            followerIDS.add(l);
                        }
                        for (int a = 0; a < 10; a++) {
                            new RemoveFollowerTask(twitter, member).start();
                        }
                    } catch (TwitterException e) {
                        Queue.removeQueue(member);
                        e.printStackTrace();
                    }
                }
                Thread.sleep(1000 * 60);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
    public static List<Long> getFollowerIDS() {
        return followerIDS;
    }
}
class RemoveFollowerTask extends Thread {

    public Twitter twitter;
    public User member;
    public RemoveFollowerTask(Twitter twitter, User member) {
        this.twitter = twitter;
        this.member = member;
    }
    @Override
    public void run() {
        while (true) {
            if(Task.getFollowerIDS().size() > 0) {
                try {
                    long id = Task.getFollowerIDS().get(0);
                    Task.getFollowerIDS().remove(id);
                    twitter.createBlock(id);
                    twitter.destroyBlock(id);
                } catch (TwitterException e) {
                    e.printStackTrace();
                }
            }
            else {
                if (!Task.a) {
                    Queue.removeQueue(member);
                    Task.a = true;
                    EmbedBuilder embedBuilder = new EmbedBuilder()
                            .setTitle("フォロワー解除完了しました！")
                            .setColor(Color.GREEN);
                    member.openPrivateChannel().complete().sendMessage(embedBuilder.build()).queue();
                }
                break;
            }
        }
    }
}