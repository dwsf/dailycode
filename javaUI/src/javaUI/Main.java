/**
 * 
 */
package javaUI;

import javax.swing.*;
/**
 * @author zsc347
 *
 */
public class Main {
	public static void main(String args[]){
		System.out.println("hello world");
		//Main a = new Main();
		//a.showJFrame();
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InstantiationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedLookAndFeelException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		new UserLogin();
	}
	
	public void showJFrame(){
		JFrame jf = new JFrame("mainFrame");
		jf.setSize(600, 800);
		jf.setLocation(100,100);
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JButton btn=new JButton("i");
		jf.getContentPane().add(btn,"West");
		jf.setVisible(true);
	}
}
