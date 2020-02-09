package com.example.androidpackettest;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;


public class Activity2 extends AppCompatActivity  {

    final String IP_ADDRESS = "10.14.184.18";
    final int PORT = 8888;

    static int xCoordinate = 0;
    static int yCoordinate = 0;

    Button buttonRight,buttonLeft,buttonScrollU,buttonScrollD,buttonExit;
    ImageView canvasImg;
    LinearLayout layer;
    float downx = 0, downy = 0, upx = 0, upy = 0;
    Canvas canvas;
    Paint p;

    Communications comms;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        String[] wh = (String[]) getIntent().getExtras().get("pixelR");
        int w = Integer.parseInt(wh[0]);
        int h = Integer.parseInt(wh[1]);
        String ip = wh[2];
        int port = Integer.parseInt(wh[3]);

        comms= new Communications(ip,port);
        try {
            Thread.sleep(500);
        }catch(Exception e){
            System.err.println("ise garos");
        }

        comms.connect();

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_2);

        buttonExit = findViewById(R.id.buttonExit);
        buttonExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                comms.send("bye:bye");
                try{
                    comms.close();
                } catch(Exception e){

                }
                finish();
                System.exit(0);
            }});
        buttonRight = findViewById(R.id.buttonRight);
        buttonRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                comms.send("Cursor_Right:Click");
            }});
        buttonLeft = findViewById(R.id.buttonLeft);
        buttonLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                comms.send("Cursor_Left:Click");
            }});
        buttonScrollU = findViewById(R.id.buttonScrollU);
        buttonScrollU.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                comms.send("Cursor_Scroll:Up");
            }});
        buttonScrollD = findViewById(R.id.buttonScrollD);
        buttonScrollD.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                comms.send("Cursor_Scroll:Down");
            }});

        canvasImg = findViewById(R.id.canvasImg);
        layer = findViewById(R.id.layout);


        ViewGroup.LayoutParams canvasLayout = (FrameLayout.LayoutParams) canvasImg.getLayoutParams();

        Point size = new Point();
        getWindowManager().getDefaultDisplay().getSize(size);

        int w2 = Math.round(size.y * w / h);
        canvasImg.setLayoutParams(new FrameLayout.LayoutParams(w2, canvasLayout.height, Gravity.RIGHT | Gravity.BOTTOM));


        canvasImg.setOnTouchListener(new View.OnTouchListener() {
            int i = 0;

            public boolean onTouch(View v, MotionEvent event) {
                Log.d("aa", " " + event.getAction());
                Log.d("aaa", "i");
                Bitmap imageBitmap = Bitmap.createBitmap(canvasImg.getWidth(), canvasImg.getHeight(), Bitmap.Config.ARGB_8888);
                canvas = new Canvas(imageBitmap);
                float scale = getResources().getDisplayMetrics().density;
                p = new Paint();
                Paint p2 = new Paint();
                Paint p3 = new Paint();
                p3.setColor(Color.RED);
                p2.setColor(Color.rgb(150, 150, 150));
                p.setColor(Color.BLUE);
                p.setStrokeWidth(p.getStrokeWidth() + 6);

                canvas.drawRect(0, 0, canvasImg.getWidth(), canvasImg.getHeight(), p2);
                canvas.drawLine(canvasImg.getWidth() / 3, 0, canvasImg.getWidth() / 3, canvasImg.getHeight(), p);
                canvas.drawLine(2 * canvasImg.getWidth() / 3, 0, 2 * canvasImg.getWidth() / 3, canvasImg.getHeight(), p);

                canvas.drawLine(0, canvasImg.getHeight() / 3, canvasImg.getWidth(), canvasImg.getHeight() / 3, p);
                canvas.drawLine(0, 2 * canvasImg.getHeight() / 3, 2 * canvasImg.getWidth(), 2 * canvasImg.getHeight() / 3, p);

                canvas.drawCircle(event.getX(), event.getY(), 20, p3);
                Log.d("aaa", event.getX() + " " + event.getY());
                canvasImg.setImageBitmap(imageBitmap);


                float rX = event.getX() / canvasImg.getWidth();
                float rY = event.getY() / canvasImg.getHeight();

                comms.send("Cursor_Move:"+rX+","+rY);

                return false;
            }
        });
    }

    class Communications{


        SenderThread myThread;
        String targetIp;
        Integer targetPort;

        public Communications(String ip, Integer port) {
            this.targetIp = ip;
            this.targetPort = port;
        };

        public boolean connect() {
            try{
                myThread = new SenderThread(IP_ADDRESS, PORT, "heheheheh");
                myThread.start();
                return true;
            } catch (Exception e){
                System.exit(0);
            }
            return false;
        }

        public void send(final String message1){

                    Thread newThread = new Thread(new Runnable() {
                @Override
                public void run() {
                    SocketAddress sockaddr = new InetSocketAddress(targetIp, targetPort);

                    Socket socket = new Socket();

                    try {
                        socket.connect(sockaddr, 1000);
                        if (!socket.isConnected()){
                            System.exit(0);
                        }
                        OutputStream out = socket.getOutputStream();
                        out.write(message1.getBytes());
                        out.flush();
                        socket.close();
                    } catch (IOException e) {
                        System.exit(0);
                    }
                }
            });
            newThread.start();
        }

        public void close(){
            myThread.stopSocket();
            myThread.destroy();
        }
    }
}





