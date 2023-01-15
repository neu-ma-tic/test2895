package main;

import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class kleinerals3 extends ListenerAdapter{



        public void onMessageReceived (MessageReceivedEvent ereignis) {

            if (ereignis.isFromGuild()) {

                if (ereignis.getMessage().getContentStripped().equals("!uwu")) {

                    ereignis.getChannel().sendTyping().queue();
                    ereignis.getChannel().sendMessage("https://tenor.com/view/chicken-tease-funny-angry-bird-gif-5402157").queue();
                }
            }
        }



}
