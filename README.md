**Repository for MSc Applied Bioinformatics thesis by Anja Tolic**

**Thesis title: Evaluating current bioinformatics tools ​for microbial epigenetics analysis​ in long-read sequencing data**

Supervisors: Dr Tomasz Kurowski and Dr Alexey Larionov

Abstract
<p align="justify">
Microbial DNA methylation is targeted to specific sequence motifs and can play different roles, from protecting the cell through restriction-modification systems, to regulating DNA replication and gene expression. The third generation long-read sequencing technologies allow direct detection of base modifications and are constantly refined alongside bioinformatic analysis tools, providing improved precision and accuracy. To keep up with the advancements, this project aims to assess select current bioinformatics tools for analyzing microbial epigenetic marks. Using latest tools’ versions, main methylation target motifs were identified from both PacBio and ONT data. In addition to using a predefined workflow, PacBio data was also analysed by a custom-devised pipeline that was able to identify target motifs with over 95% methylation after adjustment of Minimum Qmod Score. Utility and limitations of each analysis approach were thoroughly explored providing a comprehensive overview of current analysis options and paving the way to future, more complex metaepigenomic analysis.
</p>

Scripts used in this project can be found in scripts folder.

Pipelines:
PacBio Microbial Genome Analysis workflow

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_wf.drawio.png)

PacBio custom pipeline

![Model](https://github.com/anjatolic/methylBact/blob/main/pb_custom.drawio.png)

ONT - MicrobeMod https://github.com/cultivarium/MicrobeMod

![Model](https://github.com/anjatolic/methylBact/blob/main/PipelineOverview%20ONT.png)

