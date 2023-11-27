from photoshop import Session
import photoshop
app = photoshop.api.Application()


with Session(action="new_document") as ps:
    doc = ps.active_document
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = 'Hello, World!'
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    # options = ps.JPEGSaveOptions(quality=5)
    # jpg = 'd:/hello_world.jpg'
    # doc.saveAs(jpg, options, asCopy=True)
    # ps.app.doJavaScript(f'alert("save to jpg: {jpg}")')

Session.alert(app,"done")
Session.echo()
