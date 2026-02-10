---
layout: default
title: retinalysis-vascx: An explainable software toolbox for the extraction of retinal vascular biomarkers
---

# retinalysis-vascx: An explainable software toolbox for the extraction of retinal vascular biomarkers
**arXiv**：[2602.08580v1](https://arxiv.org/abs/2602.08580) · [PDF](https://arxiv.org/pdf/2602.08580.pdf)  
**作者**：Jose D. Vargas Quiros, Michael J. Beyeler, Sofia Ortin Vela, EyeNED Reading Center, Sven Bergmann, Caroline C. W. Klaver, Bart Liefers  

**一句话要点**：提出VascX开源工具箱，用于从视网膜血管分割中自动提取生物标志物，支持大规模眼科学研究。

**关键词**：视网膜血管分析, 生物标志物提取, 开源工具箱, 眼科学, 图像处理, 可解释性框架

## 3 点简述
- 核心问题：自动提取视网膜血管生物标志物对大规模研究至关重要，但现有工具缺乏标准化和可解释性。
- 方法要点：基于血管分割构建有向和无向图，解析连续血管，计算密度、角度、弯曲度等生物标志物。
- 实验或效果：通过解剖标志物实现空间标准化测量，提供可视化框架，支持可重复研究和临床部署。

## 摘要（原文）

> The automatic extraction of retinal vascular biomarkers from color fundus images (CFI) is essential for large-scale studies of the retinal vasculature. We present VascX, an open-source Python toolbox designed for the automated extraction of biomarkers from artery and vein segmentations. The VascX workflow processes vessel segmentation masks into skeletons to build undirected and directed vessel graphs, which are then used to resolve segments into continuous vessels. This architecture enables the calculation of a comprehensive suite of biomarkers, including vascular density, bifurcation angles, central retinal equivalents (CREs), tortuosity, and temporal angles, alongside image quality metrics.
>   A distinguishing feature of VascX is its region awareness; by utilizing the fovea, optic disc, and CFI boundaries as anatomical landmarks, the tool ensures spatially standardized measurements and identifies when specific biomarkers are not computable. Spatially localized biomarkers are calculated over grids relative to these landmarks, facilitating precise clinical analysis. Released via GitHub and PyPI, VascX provides an explainable and modifiable framework that supports reproducible vascular research through integrated visualizations. By enabling the rapid extraction of established biomarkers and the development of new ones, VascX advances the field of oculomics, offering a robust, computationally efficient solution for scalable deployment in large-scale clinical and epidemiological databases.

