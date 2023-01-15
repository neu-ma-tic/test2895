package me.yamashitq;

import me.yamashitq.listener.DiscordListener;
import me.yamashitq.task.Task;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import twitter4j.Twitter;
import twitter4j.TwitterFactory;

import javax.security.auth.login.LoginException;

public class Main {
    private static boolean started = true;
    private static JDA jda;
    private static Twitter twitter;
    private static String consumerKey = "";
    private static String secretKey = "";

    public static void main(String[] args) {
        try {
            Twitter twitter = TwitterFactory.getSingleton();
            twitter.setOAuthConsumer(consumerKey, secretKey);
            setTwitter(twitter);
            jda = JDABuilder.createDefault("").build();
            jda.addEventListener(new DiscordListener());
            jda.getPresence().setPresence(OnlineStatus.ONLINE, Activity.playing("/auth で使用可能"));
            new Task().start();
        } catch (LoginException e) {
            e.printStackTrace();
        }
    }

    public static JDA getJDA() {
        return jda;
    }

    public static boolean isStarted() {
        return started;
    }

    public static void setStarted(boolean started) {
        Main.started = started;
    }

    public static Twitter getTwitter() {
        return twitter;
    }

    public static void setTwitter(Twitter twitter) {
        Main.twitter = twitter;
    }

    public static String getConsumerKey() {
        return consumerKey;
    }

    public static String getSecretKey() {
        return secretKey;
    }
}
