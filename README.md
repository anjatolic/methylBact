# **Repository for MSc Applied Bioinformatics thesis by Anja Tolic**

# **Thesis title: Evaluating current bioinformatics tools ​for microbial epigenetics analysis​ in long-read sequencing data**

Supervisors: Dr Tomasz Kurowski and Dr Alexey Larionov

## **Abstract**
<p align="justify">
Microbial DNA methylation is targeted to specific sequence motifs and can play different roles, from protecting the cell through restriction-modification systems, to regulating DNA replication and gene expression. The third generation long-read sequencing technologies allow direct detection of base modifications and are constantly refined alongside bioinformatic analysis tools, providing improved precision and accuracy. To keep up with the advancements, this project aims to assess select current bioinformatics tools for analyzing microbial epigenetic marks. Using latest tools’ versions, main methylation target motifs were identified from both PacBio and ONT data. In addition to using a predefined workflow, PacBio data was also analysed by a custom-devised pipeline that was able to identify target motifs with over 95% methylation after adjustment of Minimum Qmod Score. Utility and limitations of each analysis approach were thoroughly explored providing a comprehensive overview of current analysis options and paving the way to future, more complex metaepigenomic analysis.
</p>

## **Datasets availability**

|    <br>Species                      |    <br>Strain                       |    <br>System    |    <br>Platform                  |    <br>Format              |    <br>Ref. genome                                         |    <br>Ref.                                   |   |
|-------------------------------------|-------------------------------------|------------------|----------------------------------|----------------------------|------------------------------------------------------------|-----------------------------------------------|---|
|    <br>Streptococcus agalactiae     |    <br>clinical   isolate NEM316    |    <br>PacBio    |    <br>Sequel   II               |    <br>BAM   (CCS)         |    <br>https://www.ncbi.nlm.nih.gov/nuccore/NC_004368.1    |     <br>(Manzer & Doran, 2024)                |   |
| Streptococcus agalactiae            |    <br>clinical   isolate CJB111    |    <br>PacBio    |    <br>Sequel   II               |    <br>BAM   (CCS)         |    <br>https://www.ncbi.nlm.nih.gov/nuccore/CP063198       |                                               |   |
|    <br>Myxococcus xanthus           |    <br>DZ2                          |    <br>PacBio    |    <br>Sequel   II               |    <br>BAM   (subreads)    |    <br>https://www.ncbi.nlm.nih.gov/nuccore/CP070500       |     <br>(Jain et al., 2021)                   |   |
|    <br>Rhizobium leguminosarum      |    <br>ATCC   10004                 |    <br>ONT       |    <br>MinION R10.4.1 (5 kHz)    |    <br>POD5                |    <br>Provided with the data                              |     <br>(Crits-Christoph et    al., 2023)     |   |

Crits-Christoph, A., Kang, S. C., Lee, H. H., & Ostrov, N. (2023). MicrobeMod: A computational toolkit for identifying prokaryotic methylation and restriction-modification with nanopore sequencing. BioRxiv, 2023.11.13.566931. https://doi.org/10.1101/2023.11.13.566931
Jain, R., Habermann, B. H., Mignot, T., & Stewart, F. J. (2021). Complete Genome Assembly of Myxococcus xanthus Strain DZ2 Using Long High-Fidelity (HiFi) Reads Generated with PacBio Technology. Microbiology Resource Announcements, 10(28). https://doi.org/10.1128/MRA.00530-21
Manzer, H. S., & Doran, K. S. (2024). Complete m6A and m4C methylomes for group B streptococcal clinical isolates CJB111, A909, COH1, and NEM316. Microbiology Resource Announcements, 13(1). https://doi.org/10.1128/MRA.00733-23/ASSET/3F8A8632-BC9D-48FC-A231-B305F66EFA60/ASSETS/IMAGES/LARGE/MRA.00733-23.F001.JPG

## **Pipelines:**

This repository contains scripts used for analysing DNA methylation in bacteria. Following pipelines were used for the analysis:

### **PacBio Microbial Genome Analysis workflow**
<p align="justify">
Microbial genome analysis workflow has several stages that include: assembly of large contigs, assembly of plasmids, alignment of input data to assembled contigs, polishing and base modification detection. The assembly steps are done by IPA tool for HiFi genome assembly and polishing is performed by Racon. Modification detection includes both detection of methylation and identification of methylated motifs. The input files have to be provided in XML format. To make XML file using raw BAM files ‘dataset create’ SMRT tool was used. PacBio uses Cromwell as its official workflow manager and has its own wrapper for it – ‘pbcromwell’ that is used to run the analysis by ‘pbcromwell run pb_microbial_analysis’ command.
</p>

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_wf.drawio.png)

### **PacBio custom pipeline**
<p align="justify">
For the analysis of PacBio data additional custom pipeline was designed focusing on DNA methylation analysis and omitting the genome assembly steps as all of the analysed data have appropriate reference genome files available. First steps in the pipeline include conditional data preprocessing with ‘ccs-kinetics-bystrandify’ tool and XML file creation with ‘dataset create’. Reference and datase XML files were used as input to ‘pb_align_ccs’ workflow that aligns data to reference and outputs alignment BAM and coverage GFF files. Alignment file was then used as input for ‘ipdSummary’ tool that identifies modifications (m6A and m4C). Its output, a GFF file, was input for ‘motifMaker’ tool, performing motif identification and creating CSV file of motifs and updating modification GFF file with motif information. The coverage GFF file from the alignment step was used by ‘summarizeModifications’ tool to create modification summary GFF file, and a custom script was made to plot the data.
</p>

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_custom.drawio.png)

### **ONT - MicrobeMod https://github.com/cultivarium/MicrobeMod**
<p align="justify">
ONT data was first preprocessed by basecalling with Dorado, followed by mapping reads to reference by minimap2 (Figure 2 3). Basecalling was done by using either latest Dorado model (v5.0.0.) or Rerio research model that is optimised for highly methylated bacterial DNA. In addition to that, compatible official Dorado modification models were used for m6A, m4C and 5mC methylation calling.
MicrobeMod call_methylation workflow workflow first identifies methylated sites and extracts methylation frequencies with Modkit tool. Next, 24 bases long sequences, surrounding highly methylated positions, are extracted and analysed with STREME that can identify significantly enriched motifs. Finally, fraction of methylated motif occurrences is recorded.
MicrobeMod annotate_rm was can identify genes potentially involved in DNA methylation and restriction. This is achieved by the use of prodigal, HHMER and cath-resolve-hits tools. Next, BLASTP is used to find gene homologs in REBASE database, in order to, when available, include additional information on target motifs for MTases coded by identified genes.
</p>

![Model](https://github.com/anjatolic/methylBact/blob/main/PipelineOverview%20ONT.png)


## **List of links for all reports generated as part of the analysis**

| **Organism**               | **Report**            | **Pipeline**          | **Link**                                                                                                   |
|----------------------------|-----------------------|-----------------------|------------------------------------------------------------------------------------------------------------|
| **_S. agalactiae NEM316_** | coverage              | Custom                | https://anjatolic.github.io/methylBact/NEM316_reports/PB_custom_pipeline_reports/coverage.report.html      |
|                            | mapping stats         | Custom                | https://anjatolic.github.io/methylBact/NEM316_reports/PB_custom_pipeline_reports/mapping_stats.report.html |
|                            | coverage              | MGA workflow          | https://anjatolic.github.io/methylBact/NEM316_reports/PB_MGA_reports/coverage.report.html                  |
|                            | mapping stats         | MGA workflow          | https://anjatolic.github.io/methylBact/NEM316_reports/PB_MGA_reports/mapping_stats.report.html             |
|                            | polished assembly     | MGA workflow          | https://anjatolic.github.io/methylBact/NEM316_reports/PB_MGA_reports/polished_assembly.report.html         |
|                            | modifications         | MGA workflow          | https://anjatolic.github.io/methylBact/NEM316_reports/PB_MGA_reports/modifications.report.html             |
|                            | motifs                | MGA workflow          | https://anjatolic.github.io/methylBact/NEM316_reports/PB_MGA_reports/motifs.report.html                    |
|                            | runQC                 | PacBio runQC          | https://anjatolic.github.io/methylBact/NEM316_reports/QC/PB_runqc_report/ccs.report.html                   |
|                            | NanoPlot              | NanoPlot              | https://anjatolic.github.io/methylBact/NEM316_reports/QC/Nanoplot_report/NanoPlot-report.html              |
|                            | nanoQC                | nanoQC                | https://anjatolic.github.io/methylBact/NEM316_reports/QC/nanoQC.html                                       |
|                            | RabbitQCPlus          | RabbitQCPlus          | https://anjatolic.github.io/methylBact/NEM316_reports/QC/RabbitQCPlus.html                                 |
| **_S. agalactiae CJB111_** | coverage              | Custom                | https://anjatolic.github.io/methylBact/CJB111_reports/PB_custom_pipeline_reports/coverage.report.html      |
|                            | mapping stats         | Custom                | https://anjatolic.github.io/methylBact/CJB111_reports/PB_custom_pipeline_reports/mapping_stats.report.html |
|                            | coverage              | MGA workflow Qmod 250 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/coverage.report.html          |
|                            | mapping stats         | MGA workflow Qmod 250 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/mapping_stats.report.html     |
|                            | polished assembly     | MGA workflow Qmod 250 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/polished_assembly.report.html |
|                            | modifications         | MGA workflow Qmod 250 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/modifications.report.html     |
|                            | motifs                | MGA workflow Qmod 250 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/motifs.report.html            |
|                            | coverage              | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/coverage.report.html           |
|                            | mapping stats         | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/mapping_stats.report.html      |
|                            | polished assembly     | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/polished_assembly.report.html  |
|                            | modifications         | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/modifications.report.html      |
|                            | motifs                | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/motifs.report.html             |
|                            | runQC                 | PacBio runQC          | https://anjatolic.github.io/methylBact/CJB111_reports/QC/ccs.report.html                                   |
| **_M.xanthus_**            | coverage              | Custom                | https://anjatolic.github.io/methylBact/Mx_reports/PB_custom_pipeline_reports/coverage.report.html          |
|                            | mapping stats         | Custom                | https://anjatolic.github.io/methylBact/Mx_reports/PB_custom_pipeline_reports/mapping_stats.report.html     |
|                            | coverage              | MGA workflow          | https://anjatolic.github.io/methylBact/Mx_reports/PB_MGA_reports/coverage.report.html                      |
|                            | mapping stats         | MGA workflow          | https://anjatolic.github.io/methylBact/Mx_reports/PB_MGA_reports/mapping_stats.report.html                 |
|                            | polished assembly     | MGA workflow          | https://anjatolic.github.io/methylBact/Mx_reports/PB_MGA_reports/polished_assembly.report.html             |
|                            | modifications         | MGA workflow          | https://anjatolic.github.io/methylBact/Mx_reports/PB_MGA_reports/modifications.report.html                 |
|                            | motifs                | MGA workflow          | https://anjatolic.github.io/methylBact/Mx_reports/PB_MGA_reports/motifs.report.html                        |
|                            | runQC                 | PacBio runQC          | https://anjatolic.github.io/methylBact/Mx_reports/QC/PB_runqc_report/ccs.report.html                       |
|                            | NanoPlot              | NanoPlot              | https://anjatolic.github.io/methylBact/Mx_reports/QC/Nanoplot_report/NanoPlot-report.html                  |
| **_R. leguminosarum_**     | Dorado official model | NanoPlot              | https://anjatolic.github.io/methylBact/ONT_QC_NanoPlot/Dorado_official_model/NanoPlot-report.html          |
|                            | Rerio research model  | NanoPlot              | https://anjatolic.github.io/methylBact/ONT_QC_NanoPlot/Rerio_research_model/NanoPlot-report.html           |
