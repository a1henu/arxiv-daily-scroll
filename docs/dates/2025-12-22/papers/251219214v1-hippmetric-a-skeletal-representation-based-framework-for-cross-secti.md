---
layout: default
title: HippMetric: A skeletal-representation-based framework for cross-sectional and longitudinal hippocampal substructural morphometry
---

# HippMetric: A skeletal-representation-based framework for cross-sectional and longitudinal hippocampal substructural morphometry
**arXiv**：[2512.19214v1](https://arxiv.org/abs/2512.19214) · [PDF](https://arxiv.org/pdf/2512.19214.pdf)  
**作者**：Na Gao, Chenfei Ye, Yanwu Yang, Anqi Li, Zhengbo He, Li Liang, Zhiyuan Liu, Xingyu Hao, Ting Ma, Tengfei Guo  

**一句话要点**：提出HippMetric框架，基于骨骼表示解决海马体亚结构跨个体与纵向形态测量的对应问题。

**关键词**：海马体形态测量, 骨骼表示, 跨个体对应, 纵向分析, 轴参考模型, 几何约束

## 3 点简述
- 核心问题：海马体高个体差异和复杂折叠模式阻碍跨个体与纵向分析，现有方法缺乏稳定内在坐标系。
- 方法要点：采用轴参考形态模型，构建可变形骨骼坐标系，结合表面重建和几何约束生成个性化骨骼表示。
- 实验或效果：在两个国际队列上验证，相比现有形状模型，实现更高准确性、可靠性和对应稳定性。

## 摘要（原文）

> Accurate characterization of hippocampal substructure is crucial for detecting subtle structural changes and identifying early neurodegenerative biomarkers. However, high inter-subject variability and complex folding pattern of human hippocampus hinder consistent cross-subject and longitudinal analysis. Most existing approaches rely on subject-specific modelling and lack a stable intrinsic coordinate system to accommodate anatomical variability, which limits their ability to establish reliable inter- and intra-individual correspondence. To address this, we propose HippMetric, a skeletal representation (s-rep)-based framework for hippocampal substructural morphometry and point-wise correspondence across individuals and scans. HippMetric builds on the Axis-Referenced Morphometric Model (ARMM) and employs a deformable skeletal coordinate system aligned with hippocampal anatomy and function, providing a biologically grounded reference for correspondence. Our framework comprises two core modules: a skeletal-based coordinate system that respects the hippocampus' conserved longitudinal lamellar architecture, in which functional units (lamellae) are stacked perpendicular to the long-axis, enabling anatomically consistent localization across subjects and time; and individualized s-reps generated through surface reconstruction, deformation, and geometrically constrained spoke refinement, enforcing boundary adherence, orthogonality and non-intersection to produce mathematically valid skeletal geometry. Extensive experiments on two international cohorts demonstrate that HippMetric achieves higher accuracy, reliability, and correspondence stability compared to existing shape models.

