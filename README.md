# Kicad JLCPCB export scripts

Helper scripts for convert Kicad BOM + pick and place files to expected JLCPCB PCBA format.

More info here: https://jlcpcb.com/help/article/81-How-to-generate-the-BOM-and-Centroid-file-from-KiCAD

Most code written by GPT-4...

```sh
 python3 ~/code/kicad-jlcpcb-scripts/bom_convert.py bom.csv > bom-jlcpcb.csv
python3 ~/code/kicad-jlcpcb-scripts/pip_convert.py pip.csv/your-proj-all-pos.csv > pip-jlcpcb.csv
```
