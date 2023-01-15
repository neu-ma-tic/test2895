package main;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;

import javax.security.auth.login.LoginException;

public class Hauptklasse {

    public static void main(String[] args) throws LoginException {

        //YT.tutorial

        String prefix = "!";

        System.out.println(prefix);

        String status;
        status = "!clydia";

        //int zahl = 12;
        //double kommazahl = 1.45;

        String token = "OTcxNzkzNzM4Mjc3OTc4MTky.Gnz1Rt.6OKofiHD1xT_ITNYsuW97aRysApzvAGvwl6eXk";

        JDABuilder bauplan = JDABuilder.createDefault(token);

        bauplan.setStatus(OnlineStatus.ONLINE);
        bauplan.setActivity(Activity.listening(status));
        bauplan.addEventListeners(new DCbotisONLINE());
        bauplan.addEventListeners(new MenuCommand());
        bauplan.addEventListeners(new MenuCommandSelection());

        bauplan.addEventListeners(new Energy());

        JDA bot = bauplan.build();
        System.out.println("Der Bot ist nun Online!");

    }

}