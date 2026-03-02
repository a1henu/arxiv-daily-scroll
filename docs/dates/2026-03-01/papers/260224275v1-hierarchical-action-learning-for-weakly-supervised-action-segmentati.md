---
layout: default
title: Hierarchical Action Learning for Weakly-Supervised Action Segmentation
---

# Hierarchical Action Learning for Weakly-Supervised Action Segmentation
**arXiv**：[2602.24275v1](https://arxiv.org/abs/2602.24275) · [PDF](https://arxiv.org/pdf/2602.24275.pdf)  
**作者**：Junxian Huang, Ruichu Cai, Hao Zhu, Juntao Fang, Boyan Xu, Weilin Chen, Zijian Li, Shenghua Gao  

**一句话要点**：提出HAL模型以解决弱监督动作分割中的层次推理问题

**关键词**：弱监督动作分割, 层次推理, 潜在变量模型, 时间尺度对齐, 因果生成过程

## 3 点简述
- 核心问题：机器视觉特征易导致过分割，缺乏人类感知动作的层次结构。
- 方法要点：引入层次因果数据生成过程，通过确定性过程对齐不同时间尺度的潜在变量。
- 实验或效果：在多个基准测试中显著优于现有方法，潜在动作变量严格可识别。

## 摘要（原文）

> Humans perceive actions through key transitions that structure actions across multiple abstraction levels, whereas machines, relying on visual features, tend to over-segment. This highlights the difficulty of enabling hierarchical reasoning in video understanding. Interestingly, we observe that lower-level visual and high-level action latent variables evolve at different rates, with low-level visual variables changing rapidly, while high-level action variables evolve more slowly, making them easier to identify. Building on this insight, we propose the Hierarchical Action Learning (\textbf{HAL}) model for weakly-supervised action segmentation. Our approach introduces a hierarchical causal data generation process, where high-level latent action governs the dynamics of low-level visual features. To model these varying timescales effectively, we introduce deterministic processes to align these latent variables over time. The \textbf{HAL} model employs a hierarchical pyramid transformer to capture both visual features and latent variables, and a sparse transition constraint is applied to enforce the slower dynamics of high-level action variables. This mechanism enhances the identification of these latent variables over time. Under mild assumptions, we prove that these latent action variables are strictly identifiable. Experimental results on several benchmarks show that the \textbf{HAL} model significantly outperforms existing methods for weakly-supervised action segmentation, confirming its practical effectiveness in real-world applications.

