package me.yamashitq.listener;

import me.yamashitq.Main;
import me.yamashitq.task.Queue;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.*;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.events.message.priv.PrivateMessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.auth.AccessToken;
import twitter4j.auth.RequestToken;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class DiscordListener extends ListenerAdapter {
    public static Map<User, RequestToken> tokenMap = new HashMap<>();

    @Override
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        Message message = event.getMessage();
        User user = event.getAuthor();
        String content = message.getContentDisplay();

        if (content.equals("/frtmes")) {
            if (user.getId().equals("680362200694652960")) {
                EmbedBuilder embed = new EmbedBuilder()
                        .setTitle("フォロワー解除ツールの使い方")
                        .setColor(Color.MAGENTA)
                        .appendDescription("1. フォロワー解除ツールにDMで /auth と送る。\n" +
                                "        \n" +
                                "        2. 認証のURLが返ってくるので認証しPINを入力する\n" +
                                "        \n" +
                                "        3. 待機リストに追加されるので15分以内に完了します！");
                event.getTextChannel().sendMessage(embed.build()).queue();
            }
        }
    }

    @Override
    public void onPrivateMessageReceived(@NotNull PrivateMessageReceivedEvent event) {
        Message message = event.getMessage();
        User user = event.getAuthor();
        PrivateChannel channel = event.getChannel();
        String content = message.getContentDisplay();

        if (content.equals("/auth")) {
            if (Queue.hasInQueue(user)) {
                EmbedBuilder embedBuilder = new EmbedBuilder()
                        .setTitle("すでに他の解除申請をリクエスト済みです！")
                        .setColor(Color.RED);
                channel.sendMessage(embedBuilder.build()).queue();
                return;
            }
            if (tokenMap.containsKey(user)) {
                EmbedBuilder embedBuilder = new EmbedBuilder()
                        .setTitle("すでに他の認証をリクエスト済みです！")
                        .setColor(Color.RED);
                channel.sendMessage(embedBuilder.build()).queue();
                return;
            }
            if (Queue.getQueueMembers() == 15) {
                EmbedBuilder embedBuilder = new EmbedBuilder()
                        .setTitle("今リクエストを多数受け付けています！　15分ほど開けてお試しください。")
                        .setColor(Color.RED);
                channel.sendMessage(embedBuilder.build()).queue();
                return;
            }
            try {
                Main.getTwitter().setOAuthAccessToken(null);
                RequestToken token = Main.getTwitter().getOAuthRequestToken();
                tokenMap.put(user, token);
                new Thread(() -> {
                    try {
                        Thread.sleep(1000 * 60 * 5);
                        if (tokenMap.containsKey(user)) {
                            tokenMap.remove(user);
                            EmbedBuilder embedBuilder = new EmbedBuilder()
                                    .setTitle("5分経ったのでURLが無効化されました。")
                                    .setColor(Color.RED);
                            channel.sendMessage(embedBuilder.build()).queue();
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }).start();
                EmbedBuilder embedBuilder = new EmbedBuilder()
                        .setTitle("下記のリンクを開いて認証し認証番号をチャットで5分以内に送ってください！")
                        .appendDescription(token.getAuthenticationURL())
                        .setColor(Color.CYAN);
                channel.sendMessage(embedBuilder.build()).queue();
            } catch (TwitterException e) {
                e.printStackTrace();
            }
        }
        if (tokenMap.containsKey(user)) {
            if (isNumber(content)) {
                if (content.length() == 7) {
                    RequestToken token = tokenMap.get(user);
                    Twitter twitter = TwitterFactory.getSingleton();
                    EmbedBuilder embedBuilder = new EmbedBuilder();
                    try {
                        AccessToken accessToken = twitter.getOAuthAccessToken(token, content);
                        embedBuilder.setTitle("認証成功しました！待機リストに追加したので完了までお待ちください！")
                                .setColor(Color.GREEN);
                        Queue.addQueue(user, accessToken);
                    } catch (TwitterException e) {
                        embedBuilder.setTitle("認証失敗しました")
                                .setColor(Color.RED);
                    }
                    channel.sendMessage(embedBuilder.build()).queue();
                    tokenMap.remove(user);
                }
            }
        }
    }
    public static boolean isNumber(String str) {
        try {
            Integer.parseInt(str);
            return true;
        }
        catch (NumberFormatException e) {
            return false;
        }
    }
}
