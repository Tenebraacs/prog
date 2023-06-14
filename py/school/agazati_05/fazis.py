"""
1.) Készítsd el az "fazis.py" python programot,
ami kérjen be egy hőmérséklet adatot, és ez alapján döntse el,
hogy a víz milyen halmazállapotban van, az eredményt írja ki a képernyőre.
"""

viz_homerseklet = float(input("Irja be a viz homersekletet:"))
print("\n")
if 100 > viz_homerseklet > 0:
    print("A viz folyekony halmazallapotaban van")
elif viz_homerseklet >= 100:
    print("A viz legnemu halmazallapotaban van")
else:
    print("A viz szilard halmazallopataban van")
