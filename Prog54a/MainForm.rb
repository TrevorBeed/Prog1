require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.OldLace
		@button1.Location = System::Drawing::Point.new(138, 310)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(174, 51)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(334, 310)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(172, 51)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(525, 307)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(149, 54)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(235, 32)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(77, 20)
		@textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(334, 32)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(77, 20)
		@textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(429, 32)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(77, 20)
		@textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(525, 32)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(78, 20)
		@textBox4.TabIndex = 6
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Beige
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(235, 82)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(368, 188)
		@label1.TabIndex = 7
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Green
		self.ClientSize = System::Drawing::Size.new(886, 449)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54a"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		p1 = int(@textBox1.Text)
		p2 = int(@textBox2.Text)
		p3 = int(@textBox3.Text)
		p4 = int(@textBox4.Text)
		S = p1 + p2 + p3 + p4
		avg = S / 4.0
		@label1.Text = "Sum is: " + str(S) + "\n Avarage is: " + str(avg)
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

