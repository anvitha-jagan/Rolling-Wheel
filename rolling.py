import omni.usd
from pxr import Usd, UsdGeom, Gf  # Import Gf for vector types

# Get the Omniverse stage (this connects to the current stage)
stage = omni.usd.get_context().get_stage()

# If no stage exists, create a new one
if not stage:
    stage = Usd.Stage.CreateNew('rolling_scene.usd')

# Define a transform (Xform) at /World
world_xform = UsdGeom.Xform.Define(stage, '/World')

# Create a sphere as a child of /World
cylinder = UsdGeom.Cylinder.Define(stage, world_xform.GetPath().AppendPath('Cylinder'))

# Set the radius of the sphere
cylinder.GetRadiusAttr().Set(1.0)
cylinder.GetHeightAttr().Set(3.0)

# Create a cube (box) as a backdrop
box = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Backdrop"))
box.GetDisplayColorAttr().Set([(0.0, 0.0, 1.0)])

# Apply transformations to the box (scale and translate)
cube_xform_api = UsdGeom.XformCommonAPI(box)
cube_xform_api.SetScale(Gf.Vec3f(5.0, 0.1, 5.0))
cube_xform_api.SetTranslate(Gf.Vec3d(0, 0, 0))

# Create a cube (box) as a wall
box_2 = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Wall"))
box_2.GetDisplayColorAttr().Set([(128, 0.0, 0.0)])

# Apply transformations to the box (scale and translate)
cube2_xform_api = UsdGeom.XformCommonAPI(box_2)
cube2_xform_api.SetScale(Gf.Vec3f(0.50, 2.0, 5.0))
cube2_xform_api.SetTranslate(Gf.Vec3d(2.8, 2.05, 0))

# Set the time range for the scene
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(60)

# Create XformCommonAPI object for the cylinder
cylinder_xform_api = UsdGeom.XformCommonAPI(cylinder)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-5, 1.05, 0))
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 0.0))

# Set translation of the cylinder at different times
cylinder_xform_api.SetTranslate(Gf.Vec3d(-5,  1.05, 0), time=1)  # Time 1
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 0.0), time = 1)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-2.906,  1.05, 0), time=10)  # Time 10
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, -120.0), time = 10)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-0.811,  1.05, 0), time=20)  # Time 20
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, -240.0), time = 20)
cylinder_xform_api.SetTranslate(Gf.Vec3d(1.283, 1.05, 0), time=30)  # Time 30
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, -360.0), time = 30)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-0.811, 1.05, 0), time=40)  # Time 40
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 120.0), time = 40)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-1.859, 1.05, 0), time=45)  # Time 40
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 180.0), time = 45)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-2.906, 1.05, 0), time=50)  # Time 50
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 240), time = 50)
cylinder_xform_api.SetTranslate(Gf.Vec3d(-5, 1.05, 0), time=60)  # Time 60
cylinder_xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, 360.0), time = 60)

# Save the stage to disk
stage.GetRootLayer().Save()  # Use Save() instead of Export()

# Optionally, open and display the USD file in Omniverse (assuming you have the visualization set up)
omni.usd.get_context().open_stage('rolling_scene.usd')

print("Cylinder created and scene saved as 'rolling_scene.usd'")


