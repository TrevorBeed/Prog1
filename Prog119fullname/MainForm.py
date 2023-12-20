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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(22, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(62, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "First Name"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(20, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(64, 46)
		self._label2.TabIndex = 1
		self._label2.Text = "Last Name"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(90, 14)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(114, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(90, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(114, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(90, 131)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(83, 30)
		self._label3.TabIndex = 4
		self._label3.Text = "Your Name is..."
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 161)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(229, 84)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(22, 248)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(207, 49)
		self._button1.TabIndex = 6
		self._button1.Text = "Combine Name!"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self.ClientSize = System.Drawing.Size(253, 331)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog119fullname"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		strFullName = ""
		strFullName = self._textBox1.Text + " " + self._textBox2.Text
		self._label4.Text = strFullName