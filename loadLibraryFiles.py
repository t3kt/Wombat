lib = op('/wombatNoiseLib')
files = op('shader_files')
for o in lib.findChildren(type=textDAT, tags=['wombatFunction']):
	if o.valid:
		o.destroy()

y = 400
for fileName in files.col('name')[1:]:
	name = fileName.val.replace('.glsl', '')
	name = name[0].lower() + name[1:]
	dat = lib.create(textDAT, name)
	dat.tags.add('wombatFunction')
	dat.par.file = fileName
	dat.par.loadonstartpulse.pulse()
	dat.nodeY = y
	y -= 150

op('merged_library_file_out').par.write.pulse()