---
layout: default
title: PIS: A Physics-Informed System for Accurate State Partitioning of $Aβ_{42}$ Protein Trajectories
---

# PIS: A Physics-Informed System for Accurate State Partitioning of $Aβ_{42}$ Protein Trajectories
**arXiv**：[2602.19444v1](https://arxiv.org/abs/2602.19444) · [PDF](https://arxiv.org/pdf/2602.19444.pdf)  
**作者**：Qianfeng Yu, Ningkang Peng, Yanhui Gu  

**一句话要点**：提出PIS系统以解决Aβ42蛋白轨迹中状态划分的物理约束不足问题

**关键词**：蛋白质轨迹分析, 物理约束模型, 状态划分, Aβ42蛋白, 交互式平台

## 3 点简述
- 核心问题：现有深度学习模型因缺乏物理约束，难以捕捉蛋白质轨迹中的细微状态转变。
- 方法要点：集成物理先验（如回转半径和溶剂可及表面积）到拓扑特征提取中，增强模型物理基础。
- 实验或效果：在Aβ42数据集上表现优异，并提供交互平台进行动态监控和多维验证。

## 摘要（原文）

> Understanding the conformational evolution of $β$-amyloid ($Aβ$), particularly the $Aβ_{42}$ isoform, is fundamental to elucidating the pathogenic mechanisms underlying Alzheimer's disease. However, existing end-to-end deep learning models often struggle to capture subtle state transitions in protein trajectories due to a lack of explicit physical constraints. In this work, we introduce PIS, a Physics-Informed System designed for robust metastable state partitioning. By integrating pre-computed physical priors, such as the radius of gyration and solvent-accessible surface area, into the extraction of topological features, our model achieves superior performance on the $Aβ_{42}$ dataset. Furthermore, PIS provides an interactive platform that features dynamic monitoring of physical characteristics and multi-dimensional result validation. This system offers biological researchers a powerful set of analytical tools with physically grounded interpretability. A demonstration video of PIS is available on https://youtu.be/AJHGzUtRCg0.

