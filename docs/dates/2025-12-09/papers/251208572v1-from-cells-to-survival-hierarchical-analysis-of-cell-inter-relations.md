---
layout: default
title: From Cells to Survival: Hierarchical Analysis of Cell Inter-Relations in Multiplex Microscopy for Lung Cancer Prognosis
---

# From Cells to Survival: Hierarchical Analysis of Cell Inter-Relations in Multiplex Microscopy for Lung Cancer Prognosis
**arXiv**：[2512.08572v1](https://arxiv.org/abs/2512.08572) · [PDF](https://arxiv.org/pdf/2512.08572.pdf)  
**作者**：Olle Edgren Schüllerqvist, Jens Baumann, Joakim Lindblad, Love Nordling, Artur Mezheyeuski, Patrick Micke, Nataša Sladoje  

**一句话要点**：提出HiGINE分层图方法，基于多路免疫荧光图像预测肺癌患者生存风险。

**关键词**：肿瘤微环境分析, 分层图模型, 多路免疫荧光, 生存预测, 肺癌预后

## 3 点简述
- 核心问题：肿瘤微环境中细胞间复杂交互的捕获不足，影响预后生物标志物开发。
- 方法要点：采用分层图编码细胞邻域的局部与全局关系，融合细胞类型和形态信息。
- 实验或效果：在两个公共数据集上验证，显示风险分层、鲁棒性和泛化性提升。

## 摘要（原文）

> The tumor microenvironment (TME) has emerged as a promising source of prognostic biomarkers. To fully leverage its potential, analysis methods must capture complex interactions between different cell types. We propose HiGINE -- a hierarchical graph-based approach to predict patient survival (short vs. long) from TME characterization in multiplex immunofluorescence (mIF) images and enhance risk stratification in lung cancer. Our model encodes both local and global inter-relations in cell neighborhoods, incorporating information about cell types and morphology. Multimodal fusion, aggregating cancer stage with mIF-derived features, further boosts performance. We validate HiGINE on two public datasets, demonstrating improved risk stratification, robustness, and generalizability.

