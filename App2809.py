import qgis

# Tạo một dự án QGIS
project = qgis.core.QgsProject.instance()

# Thêm dữ liệu bản đồ Việt Nam vào dự án
layer = project.addMapLayer("path/to/vietnam_map.shp")

# Tạo cửa sổ hiển thị bản đồ
canvas = qgis.gui.QgsMapCanvas()
canvas.setMap(project.mapSettings())

# Hiển thị bản đồ
canvas.show()

# Chạy ứng dụng
sys.exit(app.exec_())
