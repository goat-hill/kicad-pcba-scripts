# KiCad PCBA export scripts

Helper scripts for convert KiCad BOM + pick and place files to various PCBA formats.

## JLCPCB

https://jlcpcb.com/help/article/81-How-to-generate-the-BOM-and-Centroid-file-from-KiCAD

```sh
python3 ~/code/kicad-jlcpcb-scripts/bom_convert_jlcpcb.py bom.csv > bom-jlcpcb.csv
python3 ~/code/kicad-jlcpcb-scripts/pip_convert_jlcpcb.py pip.csv/your-proj-all-pos.csv \
  > pip-jlcpcb.csv
```

## Macrofab

https://help.macrofab.com/knowledge/how-to-use-kicad-with-macrofab

```sh
python3 ~/code/kicad-jlcpcb-scripts/bom_convert_macrofab.py \
  bom.csv pip.csv/your-proj-all-pos.csv > bom-macrofab.xyrs
```
