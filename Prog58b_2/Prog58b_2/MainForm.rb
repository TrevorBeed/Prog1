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
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DarkOliveGreen
		@button1.ForeColor = System::Drawing::Color.White
		@button1.Location = System::Drawing::Point.new(140, 311)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(195, 76)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkOliveGreen
		@button2.ForeColor = System::Drawing::Color.White
		@button2.Location = System::Drawing::Point.new(341, 311)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(195, 76)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.DarkOliveGreen
		@button3.ForeColor = System::Drawing::Color.White
		@button3.Location = System::Drawing::Point.new(542, 311)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(194, 76)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::Color.DarkOliveGreen
		@textBox1.ForeColor = System::Drawing::Color.White
		@textBox1.Location = System::Drawing::Point.new(140, 37)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(195, 20)
		@textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		@textBox2.BackColor = System::Drawing::Color.DarkOliveGreen
		@textBox2.ForeColor = System::Drawing::Color.White
		@textBox2.Location = System::Drawing::Point.new(341, 37)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(195, 20)
		@textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		@textBox3.BackColor = System::Drawing::Color.DarkOliveGreen
		@textBox3.ForeColor = System::Drawing::Color.White
		@textBox3.Location = System::Drawing::Point.new(542, 37)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(194, 20)
		@textBox3.TabIndex = 5
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.DarkOliveGreen
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(142, 69)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(593, 228)
		@label1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(912, 429)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog58b_2"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
	
	def Button2Click(sender, e)
		@label1.Text = ""
		@textBox1.Text = ""
	end

	def Button1Click(sender, e)
#		a = float(@textBox1.Text)
#		b = float(@textBox2.Text)
#		c = float(@textBox3.Text)
#		pos = (-b + $math.sqrt (b**2 - 4*a*c)) / 2*a
#		neg = (-b - $math.sqrt (b**2 - 4*a*c)) / 2*a
#		@textBox1.Text = "Answer: " + str(pos) + str(neg)
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

end

