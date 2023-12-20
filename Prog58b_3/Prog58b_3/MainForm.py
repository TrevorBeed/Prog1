import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
import math
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(147, 79)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(593, 228)
		self._label1.TabIndex = 13
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(546, 38)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(194, 38)
		self._textBox3.TabIndex = 12
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(346, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(195, 38)
		self._textBox2.TabIndex = 11
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(147, 38)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(195, 38)
		self._textBox1.TabIndex = 10
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(547, 321)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(194, 76)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(346, 321)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(195, 76)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(145, 321)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(195, 76)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(887, 444)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog58b_3"
		self.ResumeLayout(False)
		self.PerformLayout()
		

	def Button1Click(self, sender, e):
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		pos = (-b + math.sqrt (b**2 - 4*a*c)) / 2*a
		neg = (-b - math.sqrt (b**2 - 4*a*c)) / 2*a
		self._label1.Text = "Answer: " + str(pos) + " " + str(neg)

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()