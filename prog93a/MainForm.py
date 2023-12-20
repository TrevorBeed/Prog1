import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(264, 176)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(195, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Ammount owed"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(264, 213)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(195, 102)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(264, 73)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(195, 38)
		self._textBox1.TabIndex = 2
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(264, 33)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(195, 37)
		self._label3.TabIndex = 3
		self._label3.Text = "Killowatts Used"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 402)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 41)
		self._button1.TabIndex = 4
		self._button1.Text = "Not Late"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(453, 402)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 41)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(575, 402)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(116, 41)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(145, 402)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(116, 41)
		self._button4.TabIndex = 8
		self._button4.Text = "Late"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(703, 455)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Label1Click(self, sender, e):
		pass
	

	def Button1Click(self, sender, e):
		kw = int(self._textBox1.Text)
		br = round((0.0475 * kw), 2)
		sc = round((br * 0.1), 2)
		ct = round((br * 0.03), 2)
		fa = round((br + sc + ct), 2)
		self._label2.Text = str(fa)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button4Click(self, sender, e):
		kw = int(self._textBox1.Text)
		br = round((0.0475 * kw), 2)
		sc = round((br * 0.1), 2)
		ct = round((br * 0.03), 2)
		f = round((br + sc + ct), 2)
		lf = (0.04 * f)
		fa = round((br + sc + ct + lf), 2)
		self._label2.Text = str(fa)