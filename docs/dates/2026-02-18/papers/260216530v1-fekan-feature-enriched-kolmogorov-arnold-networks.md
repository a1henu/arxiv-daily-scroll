---
layout: default
title: FEKAN: Feature-Enriched Kolmogorov-Arnold Networks
---

# FEKAN: Feature-Enriched Kolmogorov-Arnold Networks
**arXiv**：[2602.16530v1](https://arxiv.org/abs/2602.16530) · [PDF](https://arxiv.org/pdf/2602.16530.pdf)  
**作者**：Sidharth S. Menon, Ameya D. Jagtap  

**一句话要点**：提出FEKAN以提升KAN的计算效率和预测精度，适用于函数逼近和偏微分方程求解。

**关键词**：Kolmogorov-Arnold网络, 特征富集, 函数逼近, 偏微分方程求解, 计算效率

## 3 点简述
- 现有KAN架构计算成本高、收敛慢，限制可扩展性。
- FEKAN通过特征富集增强表示能力，不增加可训练参数。
- 实验显示FEKAN在多种任务中收敛更快、精度更高。

## 摘要（原文）

> Kolmogorov-Arnold Networks (KANs) have recently emerged as a compelling alternative to multilayer perceptrons, offering enhanced interpretability via functional decomposition. However, existing KAN architectures, including spline-, wavelet-, radial-basis variants, etc., suffer from high computational cost and slow convergence, limiting scalability and practical applicability. Here, we introduce Feature-Enriched Kolmogorov-Arnold Networks (FEKAN), a simple yet effective extension that preserves all the advantages of KAN while improving computational efficiency and predictive accuracy through feature enrichment, without increasing the number of trainable parameters. By incorporating these additional features, FEKAN accelerates convergence, increases representation capacity, and substantially mitigates the computational overhead characteristic of state-of-the-art KAN architectures. We investigate FEKAN across a comprehensive set of benchmarks, including function-approximation tasks, physics-informed formulations for diverse partial differential equations (PDEs), and neural operator settings that map between input and output function spaces. For function approximation, we systematically compare FEKAN against a broad family of KAN variants, FastKAN, WavKAN, ReLUKAN, HRKAN, ChebyshevKAN, RBFKAN, and the original SplineKAN. Across all tasks, FEKAN demonstrates substantially faster convergence and consistently higher approximation accuracy than the underlying baseline architectures. We also establish the theoretical foundations for FEKAN, showing its superior representation capacity compared to KAN, which contributes to improved accuracy and efficiency.

