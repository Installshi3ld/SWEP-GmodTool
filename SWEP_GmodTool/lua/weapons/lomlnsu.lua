

--Only informal
SWEP.PrintName			= "ymkxwtm" -- This will be shown in the spawn menu, and in the weapon selection menu
SWEP.Author			= "mkoc with SWEP Gmod tool" -- These two options will be shown when you have the weapon highlighted in the weapon selection menu
SWEP.Instructions		= "yfwjfge"

--Define if admin only
SWEP.Spawnable = true
SWEP.AdminOnly = false
SWEP.Category  = "hrth"


--Where the weapon is in inventory
SWEP.Weight			= 5
SWEP.AutoSwitchTo		= false
SWEP.AutoSwitchFrom		= false

SWEP.Slot			= 1
SWEP.SlotPos			= 2
SWEP.DrawAmmo			= false
SWEP.DrawCrosshair		= true



local ShootSound = Sound("Weapon_Pistol.Single")
SWEP.Primary.Damage = 0 --The amount of damage will the weapon do
SWEP.Primary.TakeAmmo = 1 -- How much ammo will be taken per shot
SWEP.Primary.ClipSize = 0  -- How much bullets are in the mag
SWEP.Primary.Ammo = "Pistol" --The ammo type will it use
SWEP.Primary.DefaultClip = 0 -- How much bullets preloaded when spawned
SWEP.Primary.Spread = 0.1 -- The spread when shot
SWEP.Primary.NumberofShots = 1 -- Number of bullets when shot
SWEP.Primary.Automatic = false -- Is it automatic
SWEP.Primary.Recoil = 0.0 -- The amount of recoil
SWEP.Primary.Delay = 0.1 -- Delay before the next shot
SWEP.Primary.Force = 100

canThrowGrenade = true
propabilityThrowGrenade = 0

canShotgun = true
propabilityShotgunShot = 0

canBounce = true
probabilityBounce = 0

canTeleport = true
probabilityTeleport = 0

canJumpShot = true
probabilityJumpShot = 0


function SWEP:CustomAmmoDisplay()
	self.AmmoDisplay = self.AmmoDisplay or {} 
 
	self.AmmoDisplay.Draw = true //draw the display?
 
	if self.Primary.ClipSize > 0 then
		self.AmmoDisplay.PrimaryClip = self:Clip1() //amount in clip
		self.AmmoDisplay.PrimaryAmmo = self:Ammo1() //amount in reserve
	end
	return self.AmmoDisplay //return the table
end


-- The view-model and the world-model to use.
SWEP.ViewModel			= "models/weapons/c_Pistol.mdl"
SWEP.WorldModel			= "models/weapons/w_Pistol.mdl"


--Weapon sound
SWEP.ShootSound = Sound( "Metal.SawbladeStick" )

function SWEP:Initialize()
    self:SetWeaponHoldType( self.HoldType )
end

-- Called when the left mouse button is pressed
function SWEP:PrimaryAttack()

    if ( !self:CanPrimaryAttack() ) then return end

        randomGrenade = math.random(1, 100)
        randomShotgunShot = math.random(1, 100)
        randomTeleport = math.random(1, 100)
        randomBounce = math.random(1, 100)
        randomJump = math.random(1, 100)

        grenadeThrowed = false
        shotgunShootStatement = false
        bounceStatement = false

        if(canThrowGrenade && randomGrenade <= propabilityThrowGrenade) then
            self:throw_attack (10000);
            self.Weapon:SetNextPrimaryFire( CurTime() + self.Primary.Delay )
            self.Owner:ViewPunch( Angle( -5, 0, 0 ) )
            grenadeThrowed = true
            

        --Classic weapon
        elseif(!grenadeThrowed) then
            --Shotgunshoot
            
            if(canShotgun && randomShotgunShot <= propabilityShotgunShot) then 
                self.Primary.NumberofShots = 20
                self.Primary.Spread = 1
                shotgunShootStatement = true
            end
                

-------------------------------------------------------------------------------------------------------------------------------------------
            rayCast = self.Owner:GetEyeTrace()
          
            local bullet = {}
            bullet.Num = self.Primary.NumberofShots
            bullet.Src = self.Owner:GetShootPos()
            bullet.Dir = self.Owner:GetAimVector()
            bullet.Tracer = 1
            bullet.Spread = Vector( self.Primary.Spread * 0.1 , self.Primary.Spread * 0.1, 0)
            bullet.TracerName = "AR2Tracer"
            bullet.Force = self.Primary.Force
            bullet.Damage = self.Primary.Damage
            bullet.AmmoType = self.Primary.Ammo
                    
            local rnda = self.Primary.Recoil * -1
            local rndb = self.Primary.Recoil * math.random(-1, 1)

            self:ShootEffects()
            print(self.Primary.Spread)
            self.Owner:FireBullets( bullet )


            if(canBounce && randomBounce <= probabilityBounce) then
                --Bounce system
                bullet.Src = rayCast.HitPos
                bullet.Dir = self.Owner:GetAimVector() - 2 * (rayCast.HitNormal * (rayCast.HitNormal:Dot(self.Owner:GetAimVector())))
                self.Owner:FireBullets( bullet )

                bounceStatement = true
            end
            
            self:EmitSound(ShootSound)
            self.Owner:ViewPunch( Angle( rnda,rndb,rnda ) )
            self:TakePrimaryAmmo(self.Primary.TakeAmmo)
---------------------------------------------------------------------------------------------------------------------------------------------------
            
            -- Teleport at view
            if(canTeleport && !self.Owner:GetEyeTrace().HitSky && !shotgunShootStatement && !bounceStatement && randomTeleport <= probabilityTeleport) then

                self.Owner:SetPos(self.Owner:GetEyeTrace().HitPos + self.Owner:GetEyeTrace().HitNormal * 25)
                print("test")
            end 

            self:SetNextPrimaryFire( CurTime() + self.Primary.Delay )

            
        end

        if(canJumpShot && randomJump <= probabilityJumpShot) then

            self.Owner:SetVelocity(Vector(0,0,500))
        end

        --Reset value
        if(shotgunShootStatement) then
            self.Primary.NumberofShots = 1
            self.Primary.Spread = 0.1
            shotgunShootStatement = false
        end
        grenadeThrowed = false
        bounceStatement = false


    end

 

-- Called when the rightmouse button is pressed
function SWEP:SecondaryAttack()
	-- Though the secondary fire isn't automatic
	-- players shouldn't be able to fire too fast
	self:SetNextSecondaryFire( CurTime() + 0.1 )

end


function SWEP:Reload()
    self.Weapon:DefaultReload( ACT_VM_RELOAD )
end


function SWEP:throw_attack(range)
    self.BaseClass.ShootEffects (self);
    if (!SERVER) then return end;
    local ent = ents.Create ("npc_grenade_frag");
    ent:SetPos (self.Owner:EyePos() + (self.Owner:GetAimVector() * 14));
    ent:SetAngles (self.Owner:EyeAngles());
    ent:SetOwner(self.Owner)
    ent:Input("settimer",self.Owner,self.Owner,"1")
    ent:Spawn();
    local phys = ent:GetPhysicsObject();
    phys:ApplyForceCenter (self.Owner:GetAimVector():GetNormalized() * range);
end



