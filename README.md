# NuclearSizeCheminformatics
Cheminformatics analysis of targets hit in the Rizzotto et.al. Nuclear size paper
Currently incomplete, awaiting submission/acceptance for release of data and full code.

Python programs starting with:

## 01_
Are used in generation of dictionaries stored in JSON objects, and populated by querying the ChEMBL webresource.

## 02_
Are used to profile the number of times a target was hit by NSR/NSW compounds.

## 03_
Are used to profile global NSR/NSW compounds active in all cell lines.

## 04_
Are used to profile nuclear size increasers and decreasers.

## 05_gen_unique_by_cellline.py
Is used to profile uniquely affected targets by cell line.

## 06_how_many_cpds_with_activities_at_our_cutoff.py
Is used to query the sqllite version of ChEMBL27 and determine how many compounds are active against all targets at our activity cutoff levels

## 07_
Are used to investigate protein to compound and compound to target mappings