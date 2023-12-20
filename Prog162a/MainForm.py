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
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._textBox1.Location = System.Drawing.Point(97, 122)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(92, 29)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.PeachPuff
		self._label1.Location = System.Drawing.Point(1, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(281, 98)
		self._label1.TabIndex = 1
		self._label1.Text = "Please enter a number"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.PeachPuff
		self._label2.Location = System.Drawing.Point(1, 227)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(281, 98)
		self._label2.TabIndex = 2
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Teal
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.PeachPuff
		self._button1.Location = System.Drawing.Point(77, 175)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(139, 40)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(287, 334)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass
	def fac(self, n):
		Sum = 1
		for num in range(1, n+1):
			Sum *= num 
		return Sum
	def Button1Click(self, sender, e):
		n = int(self._textBox1.Text)
		n2 = self.fac(n)
		self._label2.Text = str(n2)