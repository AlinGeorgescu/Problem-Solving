package com.main;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import javax.swing.*;

class PushCounterPanel extends JPanel {
    private Random gen;
    private int randomNum;
    private JLabel label;

    //-----------------------------------------------------------------
    //  Constructor: Sets up the GUI.
    //-----------------------------------------------------------------
    PushCounterPanel() {
        gen = new Random();
        randomNum = gen.nextInt(1000);

        JButton push = new JButton("Random Gen");
        push.addActionListener(new ButtonListener());

        label = new JLabel("Random: " + randomNum, SwingConstants.CENTER);

        setLayout(new BorderLayout());
        setBorder(BorderFactory.createEmptyBorder());
        add(push, BorderLayout.SOUTH);
        add(label, BorderLayout.CENTER);

        setPreferredSize(new Dimension(500, 400));
    }

    private class ButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            randomNum = gen.nextInt(1000);
            label.setText("Random: " + randomNum);
            setBackground(Color.getHSBColor(randomNum, randomNum, randomNum));
        }
    }
}
