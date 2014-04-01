/**
 * 
 */
package javaUI;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

/**
 * @author zsc347
 *
 */
public class UserLogin extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JLabel lblUsername;
	private JTextField tfUsername;
	private JLabel lblPassword;
	private JPasswordField ptfPassword;
	private JButton btnOK;
	private JButton btnExit;
	
	public UserLogin(){
		JPanel p1 = new JPanel();
		p1.setLayout(new BorderLayout());
		lblUsername = new JLabel("name:");
		tfUsername=new JTextField(12);
		p1.add(lblUsername,BorderLayout.WEST);
		p1.add(tfUsername,BorderLayout.EAST);
		p1.setSize(300,100);
		
		JPanel p2 = new JPanel();
		p2.setLayout(new BorderLayout());
		lblPassword=new JLabel("password");
		ptfPassword=new JPasswordField(12);
		p2.add(lblPassword,BorderLayout.WEST);
		p2.add(ptfPassword,BorderLayout.EAST);
		p2.setSize(300, 100);
		
		JPanel p3 = new JPanel();
		btnOK = new JButton("loadin");
		btnOK.addActionListener(this);
		btnExit=new JButton("exit");
		btnExit.addActionListener(this);
		p3.add(btnOK,BorderLayout.WEST);
		p3.add(btnExit,BorderLayout.EAST);
		p3.setSize(300, 300);
		
		this.add(p1,BorderLayout.NORTH);
		this.add(p2,BorderLayout.CENTER);
		this.add(p3,BorderLayout.SOUTH);
		
		this.setLocation(400, 300);
		this.setSize(300, 300);
		this.setTitle("password verify");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getActionCommand().equals("loadin")){
			JOptionPane.showMessageDialog(this, ("your name:"+tfUsername.getText()+"\n"+"your password:"+String.valueOf(ptfPassword.getPassword())));
		}else if(e.getActionCommand().equals("exit")){
			System.exit(0);
		}
	}
}
