# **Repository for MSc Applied Bioinformatics thesis by Anja Tolic**

# **Thesis title: Evaluating current bioinformatics tools ​for microbial epigenetics analysis​ in long-read sequencing data**

Supervisors: Dr Tomasz Kurowski and Dr Alexey Larionov

## **Abstract**
<p align="justify">
Microbial DNA methylation is targeted to specific sequence motifs and can play different roles, from protecting the cell through restriction-modification systems, to regulating DNA replication and gene expression. The third generation long-read sequencing technologies allow direct detection of base modifications and are constantly refined alongside bioinformatic analysis tools, providing improved precision and accuracy. To keep up with the advancements, this project aims to assess select current bioinformatics tools for analyzing microbial epigenetic marks. Using latest tools’ versions, main methylation target motifs were identified from both PacBio and ONT data. In addition to using a predefined workflow, PacBio data was also analysed by a custom-devised pipeline that was able to identify target motifs with over 95% methylation after adjustment of Minimum Qmod Score. Utility and limitations of each analysis approach were thoroughly explored providing a comprehensive overview of current analysis options and paving the way to future, more complex metaepigenomic analysis.
</p>

This repository contains scripts used for analysing DNA methylation in bacteria. Following pipelines were used for the analysis:

## **Pipelines:**

### **PacBio Microbial Genome Analysis workflow**

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_wf.drawio.png)

### **PacBio custom pipeline**

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_custom.drawio.png)

### **ONT - MicrobeMod https://github.com/cultivarium/MicrobeMod**

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
|                            | mapping stats         | MGA workflow Qmod 251 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/mapping_stats.report.html     |
|                            | polished assembly     | MGA workflow Qmod 252 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/polished_assembly.report.html |
|                            | modifications         | MGA workflow Qmod 253 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/modifications.report.html     |
|                            | motifs                | MGA workflow Qmod 254 | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod250/motifs.report.html            |
|                            | coverage              | MGA workflow Qmod 35  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/coverage.report.html           |
|                            | mapping stats         | MGA workflow Qmod 36  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/mapping_stats.report.html      |
|                            | polished assembly     | MGA workflow Qmod 37  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/polished_assembly.report.html  |
|                            | modifications         | MGA workflow Qmod 38  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/modifications.report.html      |
|                            | motifs                | MGA workflow Qmod 39  | https://anjatolic.github.io/methylBact/CJB111_reports/PB_MGA_reports_Qmod35/motifs.report.html             |
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
