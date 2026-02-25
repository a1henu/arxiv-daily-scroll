---
layout: default
title: PIME: Prototype-based Interpretable MCTS-Enhanced Brain Network Analysis for Disorder Diagnosis
---

# PIME: Prototype-based Interpretable MCTS-Enhanced Brain Network Analysis for Disorder Diagnosis
**arXiv**：[2602.21046v1](https://arxiv.org/abs/2602.21046) · [PDF](https://arxiv.org/pdf/2602.21046.pdf)  
**作者**：Kunyu Zhang, Yanwu Yang, Jing Zhang, Xiangjie Shi, Shujian Yu  

**一句话要点**：提出PIME框架，通过原型分类与一致性训练增强脑网络分析，用于疾病诊断

**关键词**：脑网络分析, 原型分类, 一致性训练, MCTS, 可解释性, 疾病诊断

## 3 点简述
- 核心问题：现有fMRI诊断方法易受噪声干扰，后验解释方法可靠性不足，可能突出数据集特定伪影
- 方法要点：集成原型分类与一致性训练，结合结构扰动学习，利用MCTS提取最小充分解释子图
- 实验或效果：在三个基准fMRI数据集上实现最先进性能，识别关键脑区域与神经影像发现一致，稳定性分析显示90%可重复性

## 摘要（原文）

> Recent deep learning methods for fMRI-based diagnosis have achieved promising accuracy by modeling functional connectivity networks. However, standard approaches often struggle with noisy interactions, and conventional post-hoc attribution methods may lack reliability, potentially highlighting dataset-specific artifacts. To address these challenges, we introduce PIME, an interpretable framework that bridges intrinsic interpretability with minimal-sufficient subgraph optimization by integrating prototype-based classification and consistency training with structural perturbations during learning. This encourages a structured latent space and enables Monte Carlo Tree Search (MCTS) under a prototype-consistent objective to extract compact minimal-sufficient explanatory subgraphs post-training. Experiments on three benchmark fMRI datasets demonstrate that PIME achieves state-of-the-art performance. Furthermore, by constraining the search space via learned prototypes, PIME identifies critical brain regions that are consistent with established neuroimaging findings. Stability analysis shows 90% reproducibility and consistent explanations across atlases.

