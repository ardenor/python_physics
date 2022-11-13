#calculates the gravitational force on a satellite object due to a primary object (moon and earth, etc..)
from vpython import *

#angular velocity = 2*pi / rotation period(s) ex: earth ang vel = 2*pi/86400(s) = 7.27e-5 rad/s

s1 = canvas()


gravConstant = 6.67e-11 #gravitational constant 6.67 x 10 ^ -11

sunMass = 1.989e30 #mass of sun 1.989 x 10 ^ 30 kilograms
sunRadius = 6.957e8 #radius of sun 6.957 x 10 ^ 8 meters
sunAngularVelocity = 2.90888e-6 #average angular velocity of sun 2.90888 x 10 ^ -6 rad/s

earthMass = 5.972e24 #mass of earth 5.972 x 10 ^ 24 kilograms
earthRadius = 6.378e6 #radius of earth 6.378 x 10 ^ 6 meters
earthAngularVelocity = 7.27e-5 #omega avg - average angular velocity of earth in rads/s 7.27 x 10 ^ -5 rad/s

sun = sphere(pos=vector(0,0,0), radius=sunRadius, color=color.yellow)#, texture=textures.sun)
sun.rotate(angle=pi/2, axis=vector(1,0,0), origin=sun.pos)

earthOrbitalRadius = (gravConstant*sunMass/sunAngularVelocity**2)**(1/3)
earth = sphere(canvas=s1, pos=vector(earthOrbitalRadius,0,0), radius=earthRadius, texture=textures.earth, trail_color=color.blue, make_trail=True, retain=10)
s1.camera.follow(earth)
earth.rotate(angle=pi/2, axis=vector(1,0,0), origin=earth.pos) 
#initially rotates earth about x axis, to display from the pole side for better view of rotation
earthVelocity = sqrt(gravConstant*sunMass/earthOrbitalRadius)
earth.p = earthMass * earthVelocity * vector(0,1,0)

#craftOrbitalRadius = 5.2*earthRadius
craftOrbitalRadius = (gravConstant*earthMass/earthAngularVelocity**2)**(1/3) #orbital radius of craft?
craft = sphere(pos=vector(craftOrbitalRadius,0,0), radius=earthRadius, color=color.white, make_trail=True, retain=100)
craft.m = 1000 # craft mass kilograms, arbitrary
craftVelocity = sqrt(gravConstant*earthMass/craftOrbitalRadius) #velocity of craft?
craft.p = craft.m * craftVelocity * vector(0,1,0) #momentum of craft = craft mass x velocity of craft x vector z direction

t = 0
dt = 100
day = 24*3600 # 24 hours

def xShift():
    return
#slider must be bound to a function

positionsx = wtext(text='')
xs = slider(bind=xShift, min=-10, max=10, value=1)
xwtxt1 = wtext(text='')
  
xwtxt2 = wtext(text='')
grvfrc = wtext(text='')
uvdist = wtext(text='')
xwtxt3 = wtext(text='')
#lbl = label(text='test') #overlays on display

while t < 9999*day:
    rate(25)
    sun.rotate(angle=sunAngularVelocity*dt, axis=vector(0,0,1), origin=sun.pos)
    
    earth.rotate(angle=earthAngularVelocity*dt, axis=vector(0,0,1), origin=earth.pos)
    #rotates earth by angular velocity every delta time tick on the z axis
    rEarth = earth.pos - sun.pos
    rEarthMeters = sqrt((earth.pos.x - sun.pos.x)**2 + (earth.pos.y - sun.pos.y)**2 + (earth.pos.z - sun.pos.z)**2)
    
    FVectorOnEarth = ( -gravConstant*(sunMass)*earthMass*norm(rEarth)/mag(rEarth)**2 )
    earth.p = earth.p + FVectorOnEarth*dt
    earth.pos = earth.pos + earth.p*dt/earthMass 
    
    rCraft = craft.pos - earth.pos #unit vector representing positional difference between earth and craft positions
    rCraftMeters = sqrt((craft.pos.x - earth.pos.x)**2 + (craft.pos.y - earth.pos.y)**2 + (craft.pos.z - earth.pos.z)**2)
    
    FVectorOnCraft = ( -gravConstant*(earthMass*xs.value)*craft.m*norm(rCraft)/mag(rCraft)**2 )
    #gravitational force = 
        #(neg because pulling toward earth)grav constant x mass of earth x mass of obj x unit vector rCraft / magnitude (length of vec) of rCraft squared 
    craft.p = craft.p + FVectorOnCraft*dt #updated momentum (Fnet) = momentum(change) + Grav Force * delta time
    craft.pos = craft.pos + craft.p*dt/craft.m #updates craft position by its momentum by time and mass
    
    t = t + dt #updates time
    
    positionsx.text = "Earth Position Vector: " + str(earth.pos) + " Craft Position Vector: " + str(craft.pos) + "\n" 
    xwtxt1.text = "\nEarth Mass mltplr: " + str(xs.value) + "\nEarth Mass [kilograms]: " + str(earthMass*xs.value) + " kilograms"
    
    xwtxt2.text = "\n\nGravForce Vector: " + str(FVectorOnCraft)
    grvfrc.text = "\nGravForce[Newtons]: " + str(gravConstant * earthMass * craft.m / rCraftMeters**2)
    #42010000
    uvdist.text = "\n\nCraft Vector Distance [meters]: " + str(rCraftMeters) + " meters"
    xwtxt3.text = '\\nx: ' #+ str(craft.pos)
    
    #print(xs.value)
    #sleep(.01)
    
  
    
