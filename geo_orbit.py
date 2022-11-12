from vpython import *

gravConstant = 6.67e-11 #gravitational constant 6.67 x 10 ^ -11
earthMass = 5.972e24 #mass of earth 5.972 x 10 ^ 24
earthRadius = 6.378e6 #radius of earth in meters 6.378 x 10 ^ 6
earthAngularVelocity = 7.3e-5 #omega avg - average angular velocity of earth in rads/s 7.3 x 10 ^ -5

earth = sphere(pos=vector(0,0,0), radius=earthRadius, texture=textures.earth)
earth.rotate(angle=pi/2, axis=vector(1,0,0), origin=earth.pos) 
#initially rotates earth about x axis, to display from the pole side for better view of rotation

#craftOrbitalRadius = 5.2*earthRadius
craftOrbitalRadius = (gravConstant*earthMass/earthAngularVelocity**2)**(1/3) #orbital radius of craft?
craft = sphere(pos=vector(craftOrbitalRadius,0,0), radius=earthRadius/10, color=color.yellow, make_trail=True, retain=100)
craft.m = 1000 # craft mass, arbitrary
craftVelocity = sqrt(gravConstant*earthMass/craftOrbitalRadius) #velocity of craft?
craft.p = craft.m * craftVelocity * vector(0,1,0) #momentum of craft = craft mass x velocity of craft x vector z direction

t = 0
dt = 100
day = 24*3600 # 24 hours

while t < 9999*day:
    rate(100)
    earth.rotate(angle=earthAngularVelocity*dt, axis=vector(0,0,1), origin=earth.pos)
    #rotates earth by angular velocity every delta time tick on the z axis
    
    r = craft.pos - earth.pos #unit vector(1) representing positional difference between earth and craft positions
    F = -gravConstant*earthMass*craft.m*norm(r)/mag(r)**2 
    #gravitational force = 
        #(neg because pulling toward earth)grav constant x mass of earth x mass of obj x unit vector r / magnitude (length of vec) of r squared 
    craft.p = craft.p + F*dt #updated momentum (Fnet) = momentum(change) + Grav Force * delta time
    craft.pos = craft.pos + craft.p*dt/craft.m #updates craft position by its momentum by time and mass
    
    t = t + dt #updates time