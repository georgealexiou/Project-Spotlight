package com.example.androidpackettest;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

public class SenderThread extends Thread implements Runnable{
    private String ipAddress;
    private int port;
    private String message;

    private Socket socket;
    private OutputStream out;
    private SocketAddress sockaddr;

    private int previousX = -1;
    private int previousY = -1;


    SenderThread(String ipAddress, int port, String message) {
        this.ipAddress = ipAddress;
        this.port = port;
        this.message = message;

        this.socket = new Socket();
        this.sockaddr = new InetSocketAddress(ipAddress, port);
    }

    @Override
    public void run() {
        while (true) {
            try {
                if (!socket.isConnected()) {
                    socket.connect(sockaddr, 5000);
                }

                if (socket.isConnected()) {
                    out = socket.getOutputStream();
                }

                if (MainActivity.xCoordinate != previousX) {
                    this.previousX = MainActivity.xCoordinate;
                    try {
                        if (socket.isConnected()) {
                            out.write(Integer.toString(this.previousX).getBytes());
                            out.flush();
                        }
                    } catch (Exception e) {
                        System.err.println("error" + e);
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
//    public void sendSinglePacket(String message) {
//        try {
//            if (socket.isConnected()) {
//                out.write(message.getBytes());
//                out.flush();
//            }
//        } catch (Exception e) {
//            System.err.println("error" + e);
//        }
//
//    }
}
