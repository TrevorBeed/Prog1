import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._listBox2 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(335, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(195, 75)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter your test value"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(413, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(117, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(88, 93)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(186, 40)
		self._label2.TabIndex = 2
		self._label2.Text = "Even Integers"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(655, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(186, 40)
		self._label3.TabIndex = 3
		self._label3.Text = "Sum"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(403, 151)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 43)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(403, 264)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 43)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(403, 369)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 43)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(594, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(296, 75)
		self._label4.TabIndex = 12
		self._label4.Text = "The sum of the even integers is: "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(28, 148)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(348, 264)
		self._listBox1.TabIndex = 13
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# listBox2
		# 
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(570, 151)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(348, 264)
		self._listBox2.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Honeydew
		self.ClientSize = System.Drawing.Size(930, 434)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		n = int(self._textBox1.Text)
		r = 0
		n2 = 2
		while n2 <= n:
			self._listBox1.Items.Add(str(n2))
			r += n2
			n2 += 2
			self._listBox2.Items.Add(str(r))
			
		self._label4.Text = "The sum of the even integers is: " + str(r)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label4.Text = "The sum of the even integers is: "
		self._listBox1.Items.Clear()
		self._listBox2.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label4Click(self, sender, e):
		pass

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass