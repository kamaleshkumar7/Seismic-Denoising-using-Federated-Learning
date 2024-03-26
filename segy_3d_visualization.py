import numpy as np
from mayavi import mlab
import segyio
from tvtk.util.ctf import ColorTransferFunction


with segyio.open(r'filt_mig.sgy', iline =13, xline =17) as segyfile:
    data = segyio.tools.cube(segyfile)
    ntraces = segyfile.tracecount
    sr = segyio.tools.dt(segyfile)
    nsamples = segyfile.samples.size
    twt = segyfile.samples + 1000
    size_mb= data.nbytes/1024**2
    inlines = segyfile.ilines
    crosslines = segyfile.xlines
    header = segyio.tools.wrap(segyfile.text[0])
    print(header)
fig = mlab.figure(figure='seismic', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0))

#scalars = data# specifying the data array
'''
# Create volume visualization for scalars
volume = mlab.pipeline.scalar_field(scalars)
vol = mlab.pipeline.volume(volume)

ctf = ColorTransferFunction()
ctf.add_rgb_point(0.0, 0.0, 0.0, 0.0)  # Transparent at the lower range
ctf.add_rgb_point(1.0, 1.0, 1.0, 1.0)  # Fully opaque white at the upper range

# Apply the grayscale color transfer function to the volume visualization
vol._volume_property.set_color(ctf)
vol._ctf = ctf
vol.update_ctf = True

# Create image plane widgets for each axis
x_plane = mlab.pipeline.image_plane_widget(volume, plane_orientation='x_axes', slice_index=10, colormap='Oranges')
x_plane1 = mlab.pipeline.image_plane_widget(volume, plane_orientation='x_axes', slice_index=60, colormap='Oranges')
#y_plane = mlab.pipeline.image_plane_widget(volume, plane_orientation='y_axes', slice_index=25, colormap='gray')
#z_plane = mlab.pipeline.image_plane_widget(volume, plane_orientation='z_axes', slice_index=50, colormap = 'gray')

# Set colormap and opacity for the image plane widgets
x_plane.module_manager.scalar_lut_manager.data_range = scalars.min(), scalars.max()
#y_plane.module_manager.scalar_lut_manager.data_range = scalars.min(), scalars.max()
#z_plane.module_manager.scalar_lut_manager.data_range = scalars.min(), scalars.max()
x_plane.module_manager.scalar_lut_manager.number_of_colors = 256
#y_plane.module_manager.scalar_lut_manager.number_of_colors = 256
#z_plane.module_manager.scalar_lut_manager.number_of_colors = 256
x_plane.module_manager.scalar_lut_manager.use_default_range = False
#y_plane.module_manager.scalar_lut_manager.use_default_range = False
#z_plane.module_manager.scalar_lut_manager.use_default_range = False
x_plane.module_manager.scalar_lut_manager.reverse_lut = True
#y_plane.module_manager.scalar_lut_manager.reverse_lut = True
#z_plane.module_manager.scalar_lut_manager.reverse_lut = True
'''
scalars = data[:,:-3,:]   # specifying the data array
print(data.shape)
mlab.volume_slice(scalars, slice_index=0, plane_orientation='x_axes', figure=fig, colormap='gray')   
mlab.volume_slice(scalars, slice_index=0,  plane_orientation='y_axes', figure=fig, colormap='gray')   
mlab.volume_slice(scalars, slice_index=0, plane_orientation='z_axes', figure=fig, colormap='gray')   
mlab.outline()
#mlab.title('TPot', figure=fig)
ax = mlab.axes(xlabel='Inline', ylabel='Crossline', zlabel='Time', nb_labels=10)
ax.axes.font_factor =  0.5
#mlab.text3d(10, 58, 0, 'Client 1', scale=(10, 10, 10), color=(0, 0, 0), figure=fig)
#mlab.text3d(300, 58, 0, 'Client 2', scale=(10, 10, 10), color=(0, 0, 0), figure=fig)

mlab.show()
