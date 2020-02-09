package com.example.androidpackettest;

import android.content.Intent;
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
    final String IP_ADDRESS = "10.14.181.227";
    final int PORT = 8888;

    Button toggleButton,btn;
    Switch toggleSwitch;

    EditText messageTextBox;
    EditText ipTextBox;
    EditText portTextBox;

    Button startButton;
    Button sendButton;

    SenderThread myThread;


    static int xCoordinate = 0;
    static int yCoordinate = 0;

    String targetIp;
    String targetPort;

    int w = 4;
    int h = 3;
//    int[] wh = new int[2];


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        btn = findViewById(R.id.start);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openActivity2();
            }
        });

        ipTextBox = findViewById(R.id.ipText);
        portTextBox = findViewById(R.id.portText);

        targetIp = ipTextBox.getText().toString();
        targetPort = portTextBox.getText().toString();

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

    //opens second activity/screen
    public void openActivity2() {


        String[] wh = new String[4];
        wh[0] = w+""; wh[1] = h+""; wh[2] = targetIp; wh[3] = targetPort;
        Intent intent = new Intent(this, Activity2.class);
        intent.putExtra("pixelR", wh);
        startActivity(intent);
    }

}
