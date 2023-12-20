import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(101, 143)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(151, 57)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(111, 29)
		self._label1.TabIndex = 1
		self._label1.Text = "Annual Salary"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(105, 29)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay Periods per Year"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(120, 218)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(105, 29)
		self._label3.TabIndex = 3
		self._label3.Text = "Salary per Pay Period"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(120, 260)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(105, 29)
		self._label4.TabIndex = 4
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(120, 34)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(112, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(120, 93)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(112, 20)
		self._textBox2.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGreen
		self.ClientSize = System.Drawing.Size(324, 318)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "ProgSalaryCalc"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		AS = int(self._textBox1.Text)
		PPY = int(self._textBox2.Text)
		SPP = AS / PPY
		self._label4.Text = str(SPP)