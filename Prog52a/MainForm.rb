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
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(39, 34)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(429, 45)
		@label1.TabIndex = 0
		@label1.Text = "Length:"
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(39, 76)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(429, 43)
		@label2.TabIndex = 1
		@label2.Text = "Width:"
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Lime
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(39, 151)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(856, 54)
		@label3.TabIndex = 2
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Lime
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(39, 224)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(856, 65)
		@label4.TabIndex = 3
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(154, 392)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(143, 53)
		@button1.TabIndex = 4
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(384, 388)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(143, 57)
		@button2.TabIndex = 5
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(602, 388)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(151, 57)
		@button3.TabIndex = 6
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(135, 31)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(500, 35)
		@textBox1.TabIndex = 7
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(135, 73)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(502, 35)
		@textBox2.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Green
		self.ClientSize = System::Drawing::Size.new(930, 457)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def TextBox1TextChanged(sender, e)
		
	end

	def Button1Click(sender, e)
		length = int(@textBox1.Text)
		width = int(@textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		@label3.Text = "Area: " + str(area)
		@label4.Text = "Perimeter: " + str(perim)
	end



	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

end

