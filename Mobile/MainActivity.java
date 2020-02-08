package com.example.androidpackettest;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

public class MainActivity extends AppCompatActivity {
    final String IP_ADDRESS = "10.14.202.113";
    final int PORT = 8888;

    Button toggleButton;
    Switch toggleSwitch;

    EditText messageTextBox;
    EditText ipTextBox;
    EditText portTextBox;

    Button startButton;
    Button sendButton;

    SenderThread myThread;


    static int xCoordinate = 0;
    static int yCoordinate = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        toggleButton = findViewById(R.id.toggleButton);
        toggleSwitch = findViewById(R.id.switch1);
        toggleButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toggleSwitch.toggle();
                xCoordinate++;
                yCoordinate += 3;
            }
        });

        ipTextBox = findViewById(R.id.ipText);
        portTextBox = findViewById(R.id.portText);
        messageTextBox = findViewById(R.id.messageTextView);

        startButton = findViewById(R.id.startButton);
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myThread = new SenderThread(IP_ADDRESS, PORT, "heheheheh");
                myThread.start();
            }
        });

        sendButton = findViewById(R.id.sendButton);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Thread newThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        SocketAddress sockaddr = new InetSocketAddress(ipTextBox.getText().toString(), Integer.parseInt(portTextBox.getText().toString()));

                        Socket socket = new Socket();

                        try {
                            socket.connect(sockaddr, 1000);
                            OutputStream out = socket.getOutputStream();
                            out.write(messageTextBox.getText().toString().getBytes());
                            out.flush();
                            socket.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                });
                newThread.start();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }


}
