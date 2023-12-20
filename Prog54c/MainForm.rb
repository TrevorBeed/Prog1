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
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.DarkSeaGreen
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(166, 107)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(566, 143)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DarkSeaGreen
		@button1.Location = System::Drawing::Point.new(234, 272)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(140, 39)
		@button1.TabIndex = 1
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkSeaGreen
		@button2.Location = System::Drawing::Point.new(380, 273)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(140, 37)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.DarkSeaGreen
		@button3.Location = System::Drawing::Point.new(526, 273)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(140, 37)
		@button3.TabIndex = 3
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(380, 59)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(122, 20)
		@textBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Green
		self.ClientSize = System::Drawing::Size.new(894, 473)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
	
	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@textBox1.Text = ""
	end
	
	def Button1Click(sender, e)
		rad = float(@textBox1.Text)
		pi = 3.14159
		ar = pi * rad**2
		area = round(ar, 3)
		cir = 2 * pi * rad
		circ = round(cir, 3) 
		@label1.Text = "Area is: " + str(area) + "\n Circumference is: " + str(circ)
	end
end 