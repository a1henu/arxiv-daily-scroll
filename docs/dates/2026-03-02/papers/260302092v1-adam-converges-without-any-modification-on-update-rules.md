---
layout: default
title: Adam Converges Without Any Modification On Update Rules
---

# Adam Converges Without Any Modification On Update Rules
**arXiv**：[2603.02092v1](https://arxiv.org/abs/2603.02092) · [PDF](https://arxiv.org/pdf/2603.02092.pdf)  
**作者**：Yushun Zhang, Bingran Li, Congliang Chen, Zhi-Quan Luo, Ruoyu Sun  

**一句话要点**：证明Adam在问题依赖超参数下收敛，揭示相变边界并提供调参建议

**关键词**：Adam优化器, 收敛性分析, 超参数调优, 相变理论, 批量大小影响, 大语言模型训练

## 3 点简述
- 核心问题：Reddi等人示例中Adam发散，但实践中超参数选择顺序不同，引发收敛性担忧
- 方法要点：证明当β₂大且β₁<√β₂时Adam收敛，识别小β₂时发散区域，揭示(β₁,β₂)相变边界
- 实验或效果：理论保证支持调参建议，如根据批量大小调高β₂，实证研究显示提升LLM训练性能

## 摘要（原文）

> Adam is the default algorithm for training neural networks, including large language models (LLMs). However, \citet{reddi2019convergence} provided an example that Adam diverges, raising concerns for its deployment in AI model training. We identify a key mismatch between the divergence example and practice: \citet{reddi2019convergence} pick the problem after picking the hyperparameters of Adam, i.e., $(β_1,β_2)$; while practical applications often fix the problem first and then tune $(β_1,β_2)$. In this work, we prove that Adam converges with proper problem-dependent hyperparameters. First, we prove that Adam converges when $β_2$ is large and $β_1 < \sqrt{β_2}$. Second, when $β_2$ is small, we point out a region of $(β_1,β_2)$ combinations where Adam can diverge to infinity. Our results indicate a phase transition for Adam from divergence to convergence when changing the $(β_1, β_2)$ combination. To our knowledge, this is the first phase transition in $(β_1,β_2)$ 2D-plane reported in the literature, providing rigorous theoretical guarantees for Adam optimizer. We further point out that the critical boundary $(β_1^*, β_2^*)$ is problem-dependent, and particularly, dependent on batch size. This provides suggestions on how to tune $β_1$ and $β_2$: when Adam does not work well, we suggest tuning up $β_2$ inversely with batch size to surpass the threshold $β_2^*$, and then trying $β_1< \sqrt{β_2}$. Our suggestions are supported by reports from several empirical studies, which observe improved LLM training performance when applying them.

