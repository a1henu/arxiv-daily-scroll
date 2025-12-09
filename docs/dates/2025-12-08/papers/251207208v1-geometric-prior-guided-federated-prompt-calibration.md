---
layout: default
title: Geometric Prior-Guided Federated Prompt Calibration
---

# Geometric Prior-Guided Federated Prompt Calibration
**arXiv**：[2512.07208v1](https://arxiv.org/abs/2512.07208) · [PDF](https://arxiv.org/pdf/2512.07208.pdf)  
**作者**：Fei Luo, Ziwei Zhao, Mingxuan Wang, Duoyang Li, Zhe Qian, Jiayi Tuo, Chenyue Zhou, Yanbiao Ma  

**一句话要点**：提出几何先验引导的联邦提示校准以解决数据异构性导致的本地训练偏差问题

**关键词**：联邦学习, 提示学习, 数据异构性, 几何先验, 特征校准, 隐私保护

## 3 点简述
- 核心问题：联邦提示学习中数据异构性导致本地提示训练偏差，现有方法未能根治此问题
- 方法要点：通过服务器重构全局几何先验，客户端使用几何先验校准层对齐本地特征分布
- 实验或效果：在标签偏斜CIFAR-100上超越SOTA 2.15%，极端偏斜下提升9.17%，作为插件模块提升FedAvg性能4.60%

## 摘要（原文）

> Federated Prompt Learning (FPL) offers a parameter-efficient solution for collaboratively training large models, but its performance is severely hindered by data heterogeneity, which causes locally trained prompts to become biased. Existing methods, focusing on aggregation or regularization, fail to address this root cause of local training bias. To this end, we propose Geometry-Guided Text Prompt Calibration (GGTPC), a novel framework that directly corrects this bias by providing clients with a global geometric prior. This prior, representing the shape of the global data distribution derived from the covariance matrix, is reconstructed on the server in a privacy-preserving manner. Clients then use a novel Geometry-Prior Calibration Layer (GPCL) to align their local feature distributions with this global prior during training. Extensive experiments show GGTPC's effectiveness. On the label-skewed CIFAR-100 dataset ($β$=0.1), it outperforms the state-of-the-art by 2.15\%. Under extreme skew ($β$=0.01), it improves upon the baseline by 9.17\%. Furthermore, as a plug-and-play module on the domain-skewed Office-Home dataset, it boosts FedAvg's performance by 4.60\%. These results demonstrate that GGTPC effectively mitigates data heterogeneity by correcting the fundamental local training bias, serving as a versatile module to enhance various FL algorithms.

