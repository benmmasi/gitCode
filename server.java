package threadedServer;

import java.net.*;
import java.util.Scanner;
import java.io.*;

public class server {
	
	public static void main() throws IOException {
		final ServerSocket servSock;
		final Scanner scan = new Scanner(System.in);
		
		try {
			servSock = new ServerSocket(5000);
			Socket sock = servSock.accept();
			
			InputStreamReader input = new InputStreamReader(sock.getInputStream());
			BufferedReader reader = new BufferedReader(input);
			PrintStream printer = new PrintStream(sock.getOutputStream());
	
			Thread sender = new Thread(new Runnable() {
				String message;
				public void run(){
					while (true) {
						message = scan.next();
						printer.println(message);
						printer.flush();
					}
				} 
			});
		
			sender.start();
		
			Thread receiver = new Thread(new Runnable() {
				String message;
				public void run(){
					while (true) {
						try {
							message = reader.readLine();
						} catch (IOException e) {
							e.printStackTrace();
						}
						System.out.println(message);
					}
				} 
			});
		
			receiver.start();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
			
	