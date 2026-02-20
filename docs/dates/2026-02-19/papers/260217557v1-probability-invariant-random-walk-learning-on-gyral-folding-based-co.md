---
layout: default
title: Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis
---

# Probability-Invariant Random Walk Learning on Gyral Folding-Based Cortical Similarity Networks for Alzheimer's and Lewy Body Dementia Diagnosis
**arXiv**：[2602.17557v1](https://arxiv.org/abs/2602.17557) · [PDF](https://arxiv.org/pdf/2602.17557.pdf)  
**作者**：Minheng Chen, Jing Zhang, Tong Chen, Chao Cao, Tianming Liu, Li Su, Dajiang Zhu  

**一句话要点**：提出概率不变随机游走框架，基于脑回折叠网络解决阿尔茨海默病和路易体痴呆诊断中的个体化网络分类问题。

**关键词**：脑回折叠网络, 概率不变随机游走, 阿尔茨海默病诊断, 路易体痴呆诊断, 个体化网络分类, 置换不变编码

## 3 点简述
- 核心问题：脑回折叠网络因个体解剖变异和病理变化导致节点不对齐和网络大小不规则，传统图学习方法假设固定拓扑和节点对齐不适用。
- 方法要点：构建基于局部形态特征的皮质相似网络，使用匿名随机游走分布表示，通过解剖感知编码保持置换不变性，无需显式节点对齐。
- 实验或效果：在大型临床队列中，相比现有脑回折叠和基于图谱模型，该方法在阿尔茨海默病和路易体痴呆诊断上表现更优，展示稳健性和应用潜力。

## 摘要（原文）

> Alzheimer's disease (AD) and Lewy body dementia (LBD) present overlapping clinical features yet require distinct diagnostic strategies. While neuroimaging-based brain network analysis is promising, atlas-based representations may obscure individualized anatomy. Gyral folding-based networks using three-hinge gyri provide a biologically grounded alternative, but inter-individual variability in cortical folding results in inconsistent landmark correspondence and highly irregular network sizes, violating the fixed-topology and node-alignment assumptions of most existing graph learning methods, particularly in clinical datasets where pathological changes further amplify anatomical heterogeneity. We therefore propose a probability-invariant random-walk-based framework that classifies individualized gyral folding networks without explicit node alignment. Cortical similarity networks are built from local morphometric features and represented by distributions of anonymized random walks, with an anatomy-aware encoding that preserves permutation invariance. Experiments on a large clinical cohort of AD and LBD subjects show consistent improvements over existing gyral folding and atlas-based models, demonstrating robustness and potential for dementia diagnosis.

