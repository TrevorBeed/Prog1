import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(80, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(135, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(71, 18)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(153, 36)
		self._label1.TabIndex = 2
		self._label1.Text = "Guest"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(411, 18)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(153, 36)
		self._label2.TabIndex = 3
		self._label2.Text = "Chairs"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(420, 57)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(135, 20)
		self._textBox2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(80, 91)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(475, 167)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(71, 261)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 43)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(420, 261)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(135, 43)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(637, 364)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()
		
	def fac(self, n):
		Sum = 1
		for num in range(1, n+1):
			Sum *= num 
			
		return Sum
	
	def Button1Click(self, sender, e):
		#n = nog r = noc
		n = int(self._textBox1.Text)
		r = int(self._textBox2.Text)
		n1 = self.fac(n)
		nrf = self.fac((n-r))
		p = n1 / nrf
		
		stand = n - r
		if n - r < 0:
			stand = 0
		
		#PlaceHolder = self.fac(PH)
		#self._labelnumberhere.Text = str(PH)
		self._label3.Text = "Permutations: " + str(p) + " Guests standing: " + str(stand)

	def Button2Click(self, sender, e):
		Application.Exit()