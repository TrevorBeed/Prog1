import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(8, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(118, 26)
		self._label1.TabIndex = 0
		self._label1.Text = "Class A: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(8, 67)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(118, 26)
		self._label2.TabIndex = 1
		self._label2.Text = "Class B: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(8, 117)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(118, 26)
		self._label3.TabIndex = 2
		self._label3.Text = "Class C: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(99, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(121, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(99, 73)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(121, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(99, 123)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(121, 20)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(315, 121)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(118, 26)
		self._label4.TabIndex = 8
		self._label4.Text = "Class C: "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(315, 71)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(118, 26)
		self._label5.TabIndex = 7
		self._label5.Text = "Class B: "
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(315, 25)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(118, 26)
		self._label6.TabIndex = 6
		self._label6.Text = "Class A: "
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(412, 25)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(219, 26)
		self._label7.TabIndex = 9
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(412, 71)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(219, 26)
		self._label8.TabIndex = 10
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(412, 117)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(219, 26)
		self._label9.TabIndex = 11
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(166, 236)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(298, 65)
		self._label10.TabIndex = 12
		self._label10.Text = "Total Revenu: "
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label10.Click += self.Label10Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(152, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(68, 61)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(282, 172)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(68, 61)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(412, 172)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(68, 61)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(661, 310)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgStadiumSeating"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label10Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		CA = int(self._textBox1.Text)
		CB = int(self._textBox2.Text)
		CC = int(self._textBox3.Text)
		a = CA * 15
		self._label7.Text = "$" + str(a)
		b = CB * 12
		self._label8.Text = "$" + str(b)
		c = CC * 9
		self._label9.Text = "$" + str(c)
		abc = a + b + c
		self._label10.Text = " Total Revenue: $" + str(abc)
		

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = "Total Revenue: "
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()