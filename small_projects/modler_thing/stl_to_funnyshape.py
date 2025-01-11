import numpy as np
import stl

def parse_stl(stl_file):

    # Load the STL file
    mesh_data = stl.mesh.Mesh.from_file(stl_file)

    # Extract vertices and faces
    vertices = mesh_data.vectors.reshape((-1, 3))
    faces = np.arange(len(vertices)).reshape((-1, 3))

    return vertices, faces

vertices, faces= parse_stl(".stl")

data = {
    "vertices": vertices.tolist(),
    "pivot": (0, 0, 0),
    "edges": faces.tolist(),
    "faces": [
        (face.tolist(), (255, 0, 0)) for face in faces
    ]
}

shape_name = input("Enter the name of the shape: ")
with open("big_modle.py", "a") as file:
    file.write(f"\nTEMP_MOVE = {{'{shape_name}': {data}}}")

    
    #modles
