---
layout: default
title: DCG ReID: Disentangling Collaboration and Guidance Fusion Representations for Multi-modal Vehicle Re-Identification
---

# DCG ReID: Disentangling Collaboration and Guidance Fusion Representations for Multi-modal Vehicle Re-Identification
**arXiv**：[2601.02924v1](https://arxiv.org/abs/2601.02924) · [PDF](https://arxiv.org/pdf/2601.02924.pdf)  
**作者**：Aihua Zheng, Ya Gao, Shihao Li, Chenglong Li, Jin Tang  

**一句话要点**：提出DCG-ReID以解决多模态车辆重识别中质量分布不平衡导致的融合冲突问题

**关键词**：多模态车辆重识别, 解耦融合, 动态置信度加权, 协作融合模块, 引导融合模块, 模态质量分布

## 3 点简述
- 核心问题：多模态数据质量分布不确定，导致平衡与不平衡分布数据对融合需求冲突，难以解耦类内一致性和模态间异质性。
- 方法要点：设计动态置信度解耦加权机制，基于模态置信度动态重加权；针对平衡分布，开发协作融合模块挖掘共识特征；针对不平衡分布，开发引导融合模块强化主导模态优势。
- 实验或效果：在三个多模态重识别基准数据集上验证有效性，代码将在接受后发布。

## 摘要（原文）

> Multi-modal vehicle Re-Identification (ReID) aims to leverage complementary information from RGB, Near Infrared (NIR), and Thermal Infrared (TIR) modalities to retrieve the same vehicle. The challenges of multi-modal vehicle ReID arise from the uncertainty of modality quality distribution induced by inherent discrepancies across modalities, resulting in distinct conflicting fusion requirements for data with balanced and unbalanced quality distributions. Existing methods handle all multi-modal data within a single fusion model, overlooking the different needs of the two data types and making it difficult to decouple the conflict between intra-class consistency and inter-modal heterogeneity. To this end, we propose Disentangle Collaboration and Guidance Fusion Representations for Multi-modal Vehicle ReID (DCG-ReID). Specifically, to disentangle heterogeneous quality-distributed modal data without mutual interference, we first design the Dynamic Confidence-based Disentangling Weighting (DCDW) mechanism: dynamically reweighting three-modal contributions via interaction-derived modal confidence to build a disentangled fusion framework. Building on DCDW, we develop two scenario-specific fusion strategies: (1) for balanced quality distributions, Collaboration Fusion Module (CFM) mines pairwise consensus features to capture shared discriminative information and boost intra-class consistency; (2) for unbalanced distributions, Guidance Fusion Module (GFM) implements differential amplification of modal discriminative disparities to reinforce dominant modality advantages, guide auxiliary modalities to mine complementary discriminative info, and mitigate inter-modal divergence to boost multi-modal joint decision performance. Extensive experiments on three multi-modal ReID benchmarks (WMVeID863, MSVR310, RGBNT100) validate the effectiveness of our method. Code will be released upon acceptance.

