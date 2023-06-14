import pathlib

kbmodel_diagram = pathlib.Path(__file__).parent.resolve() / "../erdiagram-autogen" / "kbmodel.md"

with kbmodel_diagram.open() as f:
    diagram_txt = f.read()


to_fix_list = [
    "iri type",
    "predicate type",
    "category typeList",
    "label type",
    "narrative text",
    "biological sequence",
    "symbol type"
]

for el in to_fix_list:
    diagram_txt = diagram_txt.replace(el, "_".join(el.split()))

with kbmodel_diagram.open("w") as f:
    f.write(diagram_txt)
