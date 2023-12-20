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
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(24, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(72, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(24, 68)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(53, 18)
		self._label2.TabIndex = 1
		self._label2.Text = "Operator"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(24, 113)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(72, 26)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 2"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(24, 163)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(39, 18)
		self._label4.TabIndex = 3
		self._label4.Text = "Result"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(69, 163)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(125, 16)
		self._label5.TabIndex = 4
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(95, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(92, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(95, 110)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(92, 20)
		self._textBox2.TabIndex = 6
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(225, 38)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(26, 27)
		self._button1.TabIndex = 7
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(289, 38)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(26, 27)
		self._button2.TabIndex = 8
		self._button2.Text = "*"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(257, 71)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(26, 27)
		self._button3.TabIndex = 9
		self._button3.Text = "/"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(257, 38)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(26, 27)
		self._button4.TabIndex = 10
		self._button4.Text = "-"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(289, 71)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(26, 27)
		self._button5.TabIndex = 12
		self._button5.Text = "//"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(225, 71)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(26, 27)
		self._button6.TabIndex = 11
		self._button6.Text = "^"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(240, 105)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(61, 28)
		self._button7.TabIndex = 13
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(225, 139)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(88, 21)
		self._button8.TabIndex = 14
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(225, 166)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(88, 21)
		self._button9.TabIndex = 15
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(95, 68)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(28, 18)
		self._label6.TabIndex = 16
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGoldenrodYellow
		self.ClientSize = System.Drawing.Size(333, 331)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgSimpleCalc"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		"""+"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "+"
		result = int1 + int2
		self._label5.Text = str(result)
	

	def Button4Click(self, sender, e):
		"""-"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "-"
		result = int1 - int2
		self._label5.Text = str(result)
	

	def Button2Click(self, sender, e):
		"""*"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "*"
		result = int1 * int2
		self._label5.Text = str(result)

	def Button6Click(self, sender, e):
		"""^"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "^"
		result = int1 ** int2
		self._label5.Text = str(result)

	def Button3Click(self, sender, e):
		"""/"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "/"
		result = int1 / int2
		self._label5.Text = str(result)

	def Button5Click(self, sender, e):
		"""//"""
		int1 = int(self._textBox1.Text)
		int2 = int(self._textBox2.Text)
		self._label6.Text = "//"
		result = int1 // int2
		self._label5.Text = str(result)

	def Button8Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
	

	def Button9Click(self, sender, e):
		Application.Exit()

	def Label6Click(self, sender, e):
		pass