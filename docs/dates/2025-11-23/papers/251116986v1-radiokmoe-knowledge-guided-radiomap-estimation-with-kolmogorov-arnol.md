---
layout: default
title: RadioKMoE: Knowledge-Guided Radiomap Estimation with Kolmogorov-Arnold Networks and Mixture-of-Experts
---

# RadioKMoE: Knowledge-Guided Radiomap Estimation with Kolmogorov-Arnold Networks and Mixture-of-Experts
**arXiv**：[2511.16986v1](https://arxiv.org/abs/2511.16986) · [PDF](https://arxiv.org/pdf/2511.16986.pdf)  
**作者**：Fupei Guo, Kerry Pan, Songyang Zhang, Yue Wang, Zhi Ding  

**一句话要点**：提出RadioKMoE框架以解决复杂环境下的无线信号覆盖图估计问题

**关键词**：无线信号覆盖图估计, Kolmogorov-Arnold网络, 混合专家模型, 无线电传播建模, 深度学习应用

## 3 点简述
- 核心问题：复杂无线电传播行为和环境挑战无线信号覆盖图估计的准确性
- 方法要点：结合KAN预测粗覆盖图和MoE网络精修，提升局部细节与全局一致性
- 实验或效果：多频段和单频段实验显示，RadioKMoE在估计精度和鲁棒性上优于传统方法

## 摘要（原文）

> Radiomap serves as a vital tool for wireless network management and deployment by providing powerful spatial knowledge of signal propagation and coverage. However, increasingly complex radio propagation behavior and surrounding environments pose strong challenges for radiomap estimation (RME). In this work, we propose a knowledge-guided RME framework that integrates Kolmogorov-Arnold Networks (KAN) with Mixture-of-Experts (MoE), namely RadioKMoE. Specifically, we design a KAN module to predict an initial coarse coverage map, leveraging KAN's strength in approximating physics models and global radio propagation patterns. The initial coarse map, together with environmental information, drives our MoE network for precise radiomap estimation. Unlike conventional deep learning models, the MoE module comprises expert networks specializing in distinct radiomap patterns to improve local details while preserving global consistency. Experimental results in both multi- and single-band RME demonstrate the enhanced accuracy and robustness of the proposed RadioKMoE in radiomap estimation.

