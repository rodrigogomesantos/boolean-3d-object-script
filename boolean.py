import trimesh
import open3d as o3d
import numpy as np
import os

# Caminho do arquivo OBJ que contém as malhas separadas
arquivo_obj = "./malha_separada2.obj"

# Carregar a malha OBJ que contém as geometrias separadas usando Open3D
print("Carregando a malha do arquivo...")
malha = o3d.io.read_triangle_mesh(arquivo_obj)

# Verificar se a malha foi carregada corretamente
if malha.is_empty():
    raise RuntimeError("Falha ao carregar a malha do arquivo. Verifique o caminho e o conteúdo do arquivo.")
print("Malha carregada com sucesso.")

# Converter a malha Open3D para Trimesh
print("Convertendo malha para formato Trimesh...")
vertices = np.asarray(malha.vertices)
faces = np.asarray(malha.triangles)
malha_trimesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# Reparar a malha para garantir que ela seja um volume fechado
print("Reparando a malha para remover faces duplicadas e vértices não referenciados...")
malha_trimesh.update_faces(malha_trimesh.unique_faces())  # Remove faces duplicadas
malha_trimesh.remove_unreferenced_vertices()  # Remove vértices não referenciados
malha_trimesh.fill_holes()  # Preenche buracos na malha
print("Reparos concluídos.")

# Verificar se a malha é um volume e tentar torná-la um se não for
if not malha_trimesh.is_volume:
    print("A malha não é um volume fechado. Tentando criar um volume usando Convex Hull...")
    malha_trimesh = malha_trimesh.convex_hull  # Tentar usar o convex hull para criar um volume fechado
    print("Convex Hull aplicado.")

# Realizar a união booleana para garantir que todas as partes sejam unificadas
try:
    print("Realizando a união booleana das partes...")
    malha_unida = trimesh.boolean.union([malha_trimesh])
    if malha_unida is None or malha_unida.is_empty:
        raise RuntimeError("A operação booleana falhou e não retornou uma malha unida válida.")
    print("União booleana concluída com sucesso.")
except ValueError as e:
    raise RuntimeError("Erro ao tentar realizar a união booleana. Certifique-se de que todas as malhas são volumes fechados.") from e

# Verificar o conteúdo da malha antes de salvar
num_vertices = len(malha_unida.vertices)
num_faces = len(malha_unida.faces)
print(f"Número de vértices na malha unida: {num_vertices}")
print(f"Número de faces na malha unida: {num_faces}")
if num_vertices == 0 or num_faces == 0:
    raise RuntimeError("A malha unificada não possui vértices ou faces. Verifique o processo de união booleana.")

# Salvar a malha unificada diretamente usando Trimesh
caminho_saida_obj = os.path.join(os.getcwd(), 'malha_unificada.obj')
print("Salvando a malha unificada diretamente usando Trimesh em formato OBJ...")
malha_unida.export(caminho_saida_obj)
print(f"União das malhas concluída e salva como '{caminho_saida_obj}'")

# Além disso, salvar a malha unificada no formato PLY usando Open3D
print("Convertendo a malha unida de volta para formato Open3D...")
malha_unida_o3d = o3d.geometry.TriangleMesh()
malha_unida_o3d.vertices = o3d.utility.Vector3dVector(malha_unida.vertices)
malha_unida_o3d.triangles = o3d.utility.Vector3iVector(malha_unida.faces)

# Verificar se o diretório atual tem permissões de escrita
print("Verificando permissões de escrita no diretório...")
caminho_saida_ply = os.path.join(os.getcwd(), 'malha_unificada.ply')
if not os.access(os.getcwd(), os.W_OK):
    raise PermissionError("Sem permissão para escrever no diretório atual. Verifique as permissões.")

# Salvar a malha unificada no formato PLY
print("Salvando a malha unificada em formato PLY...")
salvo_com_sucesso_ply = o3d.io.write_triangle_mesh(caminho_saida_ply, malha_unida_o3d)

if salvo_com_sucesso_ply:
    print(f"União das malhas concluída e salva como '{caminho_saida_ply}'")
else:
    raise RuntimeError("Falha ao salvar a malha unificada no formato PLY. Verifique as permissões do diretório e o estado da malha.")
