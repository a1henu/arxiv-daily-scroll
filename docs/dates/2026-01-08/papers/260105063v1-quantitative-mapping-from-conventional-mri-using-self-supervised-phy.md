---
layout: default
title: Quantitative mapping from conventional MRI using self-supervised physics-guided deep learning: applications to a large-scale, clinically heterogeneous dataset
---

# Quantitative mapping from conventional MRI using self-supervised physics-guided deep learning: applications to a large-scale, clinically heterogeneous dataset
**arXiv**：[2601.05063v1](https://arxiv.org/abs/2601.05063) · [PDF](https://arxiv.org/pdf/2601.05063.pdf)  
**作者**：Jelmer van Lune, Stefano Mandija, Oscar van der Heide, Matteo Maspero, Martin B. Schilder, Jan Willem Dankbaar, Cornelis A. T. van den Berg, Alessandro Sbrizzi  

**一句话要点**：提出自监督物理引导深度学习框架，从常规MRI推断定量图谱以支持大规模生物标志物研究。

**关键词**：定量磁共振成像, 自监督学习, 物理引导深度学习, 生物标志物研究, 临床异质数据集, 图谱推断

## 3 点简述
- 常规MRI提供定性信息，依赖硬件和设置，定量MRI受限；
- 框架基于自监督物理引导深度学习，从T1加权、T2加权和FLAIR图像推断T1、T2和质子密度图谱；
- 在4,121次扫描的大规模临床异质数据集上评估，图谱值与文献一致，对硬件和协议具有不变性，重现性高。

## 摘要（原文）

> Magnetic resonance imaging (MRI) is a cornerstone of clinical neuroimaging, yet conventional MRIs provide qualitative information heavily dependent on scanner hardware and acquisition settings. While quantitative MRI (qMRI) offers intrinsic tissue parameters, the requirement for specialized acquisition protocols and reconstruction algorithms restricts its availability and impedes large-scale biomarker research. This study presents a self-supervised physics-guided deep learning framework to infer quantitative T1, T2, and proton-density (PD) maps directly from widely available clinical conventional T1-weighted, T2-weighted, and FLAIR MRIs. The framework was trained and evaluated on a large-scale, clinically heterogeneous dataset comprising 4,121 scan sessions acquired at our institution over six years on four different 3 T MRI scanner systems, capturing real-world clinical variability. The framework integrates Bloch-based signal models directly into the training objective. Across more than 600 test sessions, the generated maps exhibited white matter and gray matter values consistent with literature ranges. Additionally, the generated maps showed invariance to scanner hardware and acquisition protocol groups, with inter-group coefficients of variation $\leq$ 1.1%. Subject-specific analyses demonstrated excellent voxel-wise reproducibility across scanner systems and sequence parameters, with Pearson $r$ and concordance correlation coefficients exceeding 0.82 for T1 and T2. Mean relative voxel-wise differences were low across all quantitative parameters, especially for T2 ($<$ 6%). These results indicate that the proposed framework can robustly transform diverse clinical conventional MRI data into quantitative maps, potentially paving the way for large-scale quantitative biomarker research.

