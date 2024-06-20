def circle(px1, py1, px2, py2, px3, py3):

	def middlepoints(px1, py1, px2, py2, px3, py3):

		middlepoints.M1x = (px1+px2)/2
		middlepoints.M1y = (py1+py2)/2
		M1 = [middlepoints.M1x, middlepoints.M1y]

		middlepoints.M2x = (px2+px3)/2
		middlepoints.M2y = (py2+py3)/2
		M2 = [middlepoints.M2x, middlepoints.M2y]

	def equationmaker(px1, py1, px2, py2, px3, py3, M1x, M2y):

		slope1 = (py2-py1)/(px2-px1)
		equationmaker.slope1pb = -1/slope1
		equationmaker.b1 = -equationmaker.slope1pb*M1x+middlepoints.M1y

		y1 = equationmaker.slope1pb-equationmaker.b1
		print("y1 =", equationmaker.slope1pb, "*x +", -equationmaker.b1)

		slope2 = (py3-py2)/(px3-px2)
		equationmaker.slope2pb = -1/slope2
		equationmaker.b2 = -equationmaker.slope2pb*middlepoints.M2x+M2y

		y2 = equationmaker.slope2pb-equationmaker.b2
		print("y2 =", equationmaker.slope2pb, "*x +", -equationmaker.b2)

	def xsolver(slope2pb, slope1pb, b1, b2):

		#print("slope1b:", slope1pb)
		#print("slope2b:", slope2pb)

		ft = slope1pb-slope2pb
		#print("feet:", ft)
		xsolver.x = (b2-b1)/ft
		print(xsolver.x)

	def ysolver(slope1pb, x, b1):

		ysolver.y = slope1pb*x+b1
		print(ysolver.y)

	def iterator(x, y):

		a = 0
		b = 0
		c = 100
		d = 100

		for a in range(c):
			f = x*a
			print("x:", "times", a, "is", f)
		print("""





			""")
		for b in range(d):
			g = y*b
			print("y", "times", b, "is", g)
	def radius(px1, py1, x, y):

		radius.radius = ((px1 - x)**2 + (py1 - y)**2)**(1/2)
		print("the radius is ", radius.radius)

	def printer(x, y, radius):

		print("the equation of the circle is (x -", x, ")^2 + (y -", y, ")^2 =", radius, "^2")
		print("Be mindful of the signs, two negatives will give a positive")


	middlepoints(px1, py1, px2, py2, px3, py3)
	equationmaker(px1, py1, px2, py2, px3, py3, middlepoints.M1x, middlepoints.M2y)
	xsolver(equationmaker.slope2pb, equationmaker.slope1pb, equationmaker.b1, equationmaker.b2)
	ysolver(equationmaker.slope1pb, xsolver.x, equationmaker.b1)
	radius(px1, py1, xsolver.x, ysolver.y)
	printer(xsolver.x, ysolver.y, radius.radius)
	iterator(xsolver.x, ysolver.y)

circle(-5, 5, 5, -4, 6, -7)