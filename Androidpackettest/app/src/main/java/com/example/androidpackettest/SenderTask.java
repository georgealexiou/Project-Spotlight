package com.example.androidpackettest;

import android.os.AsyncTask;

import java.io.*;
import java.net.*;

class SenderTask extends AsyncTask <Void, byte[], Boolean> {
    private String ipAddress;
    private int port;
    private Socket socket;
    private OutputStream out;

    SenderTask(String ipAddress, int port) {
        this.ipAddress = ipAddress;
        this.port = port;
    }

    @Override
    protected Boolean doInBackground(Void... voids) {
        try {
            SocketAddress sockaddr = new InetSocketAddress(ipAddress, port);
            socket = new Socket();
            socket.connect(sockaddr, 5000);

            if (socket.isConnected()) {
                out = socket.getOutputStream();

                return true;
            }
            else {
                return false;
            }
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    public void sendSinglePacket (String message) {
        try {
            if (socket.isConnected()) {
                out.write(message.getBytes());

                out.flush();

                int i = 5;
            }
        }
        catch (Exception e) {
            System.err.println("error"+e);
        }
    }
}
