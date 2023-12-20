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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(417, 69)
		self._label1.TabIndex = 0
		self._label1.Text = "What is the sum of the multiples of 3 from 3 to 9669?"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(38, 154)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(374, 64)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.ForeColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(12, 342)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 75)
		self._button1.TabIndex = 2
		self._button1.Text = "Find Out"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(237, 342)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(192, 75)
		self._button2.TabIndex = 3
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(441, 429)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.ForeColor = System.Drawing.Color.White
		self.Name = "MainForm"
		self.Text = "prog152a"
		self.ResumeLayout(False)

#The sum of the multiples of 3, from 3 to 9669 is 15586428


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		s = sum(range(3,9670, 3))
		self._label2.Text = "It is " + str(s) + "!"

	def Button2Click(self, sender, e):
		Application.Exit()