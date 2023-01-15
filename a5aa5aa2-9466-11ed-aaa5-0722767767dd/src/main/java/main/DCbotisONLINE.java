package main;

import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class DCbotisONLINE extends ListenerAdapter {

    public void onMessageReceived (MessageReceivedEvent ereignis) {

        if (ereignis.isFromGuild()) {

            if (ereignis.getMessage().getContentStripped().equals("!clydia")) {

                ereignis.getChannel().sendTyping().queue();
                ereignis.getChannel().sendMessage("This is Clydia!  A personal Project from @Trixi199#0001  |  Clydia is here to help you..  <3").queue();
            }
        }
    }
}
