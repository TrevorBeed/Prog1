require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.FromArgb(64, 64, 64)
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Lime
		@label1.Location = System::Drawing::Point.new(158, 37)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(419, 236)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.FromArgb(64, 64, 64)
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Lime
		@button1.Location = System::Drawing::Point.new(158, 330)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(149, 60)
		@button1.TabIndex = 1
		@button1.Text = "Bio"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(64, 64, 64)
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Lime
		@button2.Location = System::Drawing::Point.new(428, 330)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(149, 60)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(730, 471)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.ForeColor = System::Drawing::Color.FromArgb(64, 64, 64)
		self.Name = "MainForm"
		self.Text = "Bio"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
	end

	def TextBox1TextChanged(sender, e)
		
	end

	def Button1Click(sender, e)
		
	end

	def Button2Click(sender, e)
		
	end

	def MainFormLoad(sender, e)
		
	end
	
	def Button1Click(sender, e)
		@label1.Text = "Im, Trevor, a 17 year old kid"
	end
	
	def Button2Click(sender, e)
		@label1.Text = ""
	end

end

