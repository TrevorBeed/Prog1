import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
import math

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Black
		self._label8.Location = System.Drawing.Point(287, 296)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(114, 31)
		self._label8.TabIndex = 37
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Black
		self._label9.Location = System.Drawing.Point(287, 258)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(114, 28)
		self._label9.TabIndex = 36
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Black
		self._label10.Location = System.Drawing.Point(287, 220)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(114, 30)
		self._label10.TabIndex = 35
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(287, 180)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(114, 26)
		self._label11.TabIndex = 34
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.Black
		self._label12.Location = System.Drawing.Point(287, 134)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(114, 30)
		self._label12.TabIndex = 33
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.Black
		self._label13.Location = System.Drawing.Point(287, 93)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(114, 32)
		self._label13.TabIndex = 32
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.Black
		self._label14.Location = System.Drawing.Point(287, 44)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(114, 38)
		self._label14.TabIndex = 31
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Black
		self._label7.Location = System.Drawing.Point(15, 296)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(114, 31)
		self._label7.TabIndex = 30
		self._label7.Text = "Min"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(15, 258)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(114, 28)
		self._label6.TabIndex = 29
		self._label6.Text = "Max"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(15, 220)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(114, 30)
		self._label5.TabIndex = 28
		self._label5.Text = "Abs. Distance"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(15, 180)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(114, 26)
		self._label4.TabIndex = 27
		self._label4.Text = "Average"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(15, 134)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(114, 30)
		self._label3.TabIndex = 26
		self._label3.Text = "Product"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(15, 93)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(114, 32)
		self._label2.TabIndex = 25
		self._label2.Text = "Diffrence"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(15, 44)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(114, 38)
		self._label1.TabIndex = 24
		self._label1.Text = "Sum"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ButtonFace
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(265, 374)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 43)
		self._button3.TabIndex = 23
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(152, 374)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 43)
		self._button2.TabIndex = 22
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(21, 374)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 43)
		self._button1.TabIndex = 21
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ButtonFace
		self._textBox2.Location = System.Drawing.Point(287, 12)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(115, 20)
		self._textBox2.TabIndex = 20
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ButtonFace
		self._textBox1.Location = System.Drawing.Point(14, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(115, 20)
		self._textBox1.TabIndex = 19
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SteelBlue
		self.ClientSize = System.Drawing.Size(417, 428)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()
		
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		self._label13.Text = str(Diff)
		self._label14.Text = str(Sum)
		AbsDiff = abs(Diff)
		self._label10.Text = str(AbsDiff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		
		if Max == num1:
			Min = num2
		else: 
			Min = num1
			
			self._label9.Text = str(Max)
			self._label8.Text = str(Min)
			
		Prod = num1 * num2
		self._label12.Text = str(Prod)
		
		Avg = num1 + num2 / 2
		self._label11.Text = str(Avg)

	def TextBox1TextChanged(self, sender, e):
		pass