from circleshape import CircleShape

class Shot(CircleShape) :

	def __init__(self, x, y) :
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen) :
		pygame.draw.circle(screen,(255,0,0),self.position,self.radius)

	def update(self, dt) :
		self.position += pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED * dt
