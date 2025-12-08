---
layout: default
title: Comparing the latent features of universal machine-learning interatomic potentials
---

# Comparing the latent features of universal machine-learning interatomic potentials
**arXiv**：[2512.05717v1](https://arxiv.org/abs/2512.05717) · [PDF](https://arxiv.org/pdf/2512.05717.pdf)  
**作者**：Sofiia Chorna, Davide Tisi, Cesare Malosso, Wei Bin How, Michele Ceriotti, Sanggyu Chong  

**一句话要点**：比较通用机器学习原子间势的潜在特征，分析其信息内容与训练影响

**关键词**：机器学习原子间势, 潜在特征分析, 特征重构误差, 化学空间编码, 训练协议影响, 特征压缩

## 3 点简述
- 核心问题：通用机器学习原子间势（uMLIPs）的潜在特征如何编码化学信息，模型间差异及训练因素影响未知
- 方法要点：使用特征重构误差定量评估潜在特征信息内容，分析训练集、协议和微调对特征趋势的影响
- 实验或效果：发现uMLIPs以显著不同方式编码化学空间，特征重构误差高，微调保留预训练偏差，原子级特征可压缩为结构级特征

## 摘要（原文）

> The past few years have seen the development of ``universal'' machine-learning interatomic potentials (uMLIPs) capable of approximating the ground-state potential energy surface across a wide range of chemical structures and compositions with reasonable accuracy. While these models differ in the architecture and the dataset used, they share the ability to compress a staggering amount of chemical information into descriptive latent features. Herein, we systematically analyze what the different uMLIPs have learned by quantitatively assessing the relative information content of their latent features with feature reconstruction errors as metrics, and observing how the trends are affected by the choice of training set and training protocol. We find that the uMLIPs encode chemical space in significantly distinct ways, with substantial cross-model feature reconstruction errors. When variants of the same model architecture are considered, trends become dependent on the dataset, target, and training protocol of choice. We also observe that fine-tuning of a uMLIP retains a strong pre-training bias in the latent features. Finally, we discuss how atom-level features, which are directly output by MLIPs, can be compressed into global structure-level features via concatenation of progressive cumulants, each adding significantly new information about the variability across the atomic environments within a given system.

