---
layout: default
title: SfMamba: Efficient Source-Free Domain Adaptation via Selective Scan Modeling
---

# SfMamba: Efficient Source-Free Domain Adaptation via Selective Scan Modeling
**arXiv**：[2601.08608v1](https://arxiv.org/abs/2601.08608) · [PDF](https://arxiv.org/pdf/2601.08608.pdf)  
**作者**：Xi Chen, Hongxun Yao, Sicheng Zhao, Jiankun Zhu, Jing Jiang, Kui Jiang  

**一句话要点**：提出SfMamba框架，通过选择性扫描建模解决源自由域适应中的感知场与效率权衡问题。

**关键词**：源自由域适应, 选择性扫描建模, 通道序列扫描, 语义一致打乱, 域不变特征提取

## 3 点简述
- 核心问题：源自由域适应中，现有方法在域不变特征学习时难以平衡感知场与计算效率。
- 方法要点：引入通道视觉状态空间块进行通道序列扫描，并采用语义一致打乱策略保持预测一致性。
- 实验或效果：在多个基准测试中表现优于现有方法，同时保持参数效率。

## 摘要（原文）

> Source-free domain adaptation (SFDA) tackles the critical challenge of adapting source-pretrained models to unlabeled target domains without access to source data, overcoming data privacy and storage limitations in real-world applications. However, existing SFDA approaches struggle with the trade-off between perception field and computational efficiency in domain-invariant feature learning. Recently, Mamba has offered a promising solution through its selective scan mechanism, which enables long-range dependency modeling with linear complexity. However, the Visual Mamba (i.e., VMamba) remains limited in capturing channel-wise frequency characteristics critical for domain alignment and maintaining spatial robustness under significant domain shifts. To address these, we propose a framework called SfMamba to fully explore the stable dependency in source-free model transfer. SfMamba introduces Channel-wise Visual State-Space block that enables channel-sequence scanning for domain-invariant feature extraction. In addition, SfMamba involves a Semantic-Consistent Shuffle strategy that disrupts background patch sequences in 2D selective scan while preserving prediction consistency to mitigate error accumulation. Comprehensive evaluations across multiple benchmarks show that SfMamba achieves consistently stronger performance than existing methods while maintaining favorable parameter efficiency, offering a practical solution for SFDA. Our code is available at https://github.com/chenxi52/SfMamba.

