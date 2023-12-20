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
		@label1 = System::Windows::Forms::Label.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Red
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.White
		@button1.Location = System::Drawing::Point.new(186, 322)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(181, 78)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Red
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.White
		@button2.Location = System::Drawing::Point.new(390, 322)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(181, 78)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Red
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.White
		@button3.Location = System::Drawing::Point.new(587, 322)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(181, 77)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Red
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.White
		@label1.Location = System::Drawing::Point.new(186, 94)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(582, 183)
		@label1.TabIndex = 4
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		@textBox2.BackColor = System::Drawing::Color.Red
		@textBox2.Location = System::Drawing::Point.new(390, 41)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(134, 20)
		@textBox2.TabIndex = 5
		@textBox2.TextChanged { |sender, e| self.TextBox2TextChanged(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.BackColor = System::Drawing::Color.Red
		@textBox3.Location = System::Drawing::Point.new(555, 41)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(134, 20)
		@textBox3.TabIndex = 6
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::Color.Red
		@textBox1.Location = System::Drawing::Point.new(233, 41)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(134, 20)
		@textBox1.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(64, 0, 0)
		self.ClientSize = System::Drawing::Size.new(912, 479)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button3Click(sender, e)
		application.Exit()
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@textBox1.Text = ""
	end

	def Button1Click(sender, e)
		a = float(@textBox1.Text)
		b = float(@textBox2.Text)
		c = float(@textBox3.Text)
		pos = (-b + $math.sqrt (b**2 - 4*a*c)) / 2*a
		neg = (-b - $math.sqrt (b**2 - 4*a*c)) / 2*a  
	end

end