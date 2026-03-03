---
layout: default
title: Scalable Multi-Task Low-Rank Model Adaptation
---

# Scalable Multi-Task Low-Rank Model Adaptation
**arXiv**：[2603.01526v1](https://arxiv.org/abs/2603.01526) · [PDF](https://arxiv.org/pdf/2603.01526.pdf)  
**作者**：Zichen Tian, Antoine Ledent, Qianru Sun  

**一句话要点**：提出mtLoRA以解决多任务低秩适应在任务扩展时的性能崩溃问题

**关键词**：多任务学习, 低秩适应, 模型可扩展性, 正则化技术, 参数效率

## 3 点简述
- 核心问题：多任务LoRA扩展导致参数和表示错位，引发灾难性性能下降。
- 方法要点：采用谱感知正则化、块级适应和细粒度路由，提升可扩展性和效率。
- 实验或效果：在四个大规模基准上，平均准确率提升2.3%，参数减少47%，训练时间减少24%。

## 摘要（原文）

> Scaling multi-task low-rank adaptation (LoRA) to a large number of tasks induces catastrophic performance degradation, such as an accuracy drop from 88.2% to 2.0% on DOTA when scaling from 5 to 15 tasks. This failure is due to parameter and representation misalignment. We find that existing solutions, like regularization and dynamic routing, fail at scale because they are constrained by a fundamental trade-off: strengthening regularization to reduce inter-task conflict inadvertently suppresses the essential feature discrimination required for effective routing. In this work, we identify two root causes for this trade-off. First, uniform regularization disrupts inter-task knowledge sharing: shared underlying knowledge concentrates in high-SV components (89% alignment on Flanv2->BBH). Uniform regularization forces high-SV components to update in orthogonal directions, directly disrupting the shared knowledge. Second, Conflict Amplification: Applying LoRA at the component-level (e.g., W_q, W_v) amplifies gradient conflicts; we show block-level adaptation reduces this conflict by 76% with only 50% parameters. Based on these insights, we propose mtLoRA, a scalable solution with three novel designs: 1) Spectral-Aware Regularization to selectively orthogonalize low-SV components while preserving high-SV shared knowledge, 2) Block-Level Adaptation to mitigate conflict amplification and largely improve parameter efficiency, and 3) Fine-Grained Routing using dimension-specific weights for superior expressive power. On four large-scale (15-25 tasks) vision (DOTA and iNat2018) and NLP (Dolly-15k and BBH) benchmarks, mtLoRA achieves 91.7%, 81.5%, 44.5% and 38.5% accuracy on DOTA, iNat2018, Dolly-15k and BBH respectively, outperforming the state-of-the-art by 2.3% on average while using 47% fewer parameters and 24% less training time.

