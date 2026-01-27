---
layout: default
title: HeterCSI: Channel-Adaptive Heterogeneous CSI Pretraining Framework for Generalized Wireless Foundation Models
---

# HeterCSI: Channel-Adaptive Heterogeneous CSI Pretraining Framework for Generalized Wireless Foundation Models
**arXiv**：[2601.18200v1](https://arxiv.org/abs/2601.18200) · [PDF](https://arxiv.org/pdf/2601.18200.pdf)  
**作者**：Chenyu Zhang, Xinchen Lyu, Chenshan Ren, Shuhan Liu, Qimei Cui, Xiaofeng Tao  

**一句话要点**：提出HeterCSI框架以解决无线基础模型在异构CSI预训练中的泛化与效率问题

**关键词**：无线基础模型, CSI预训练, 异构数据处理, 梯度对齐, 自适应批处理, 零填充优化

## 3 点简述
- 核心问题：CSI在规模和场景维度存在双重异构性，现有方法限制输入维度或隔离训练，影响泛化能力。
- 方法要点：通过梯度动态分析，设计尺度感知自适应批处理策略和双重掩码机制，优化批构建以减少填充开销。
- 实验或效果：在12个数据集上验证，无需场景微调即实现泛化，性能优于基线，训练延迟降低53%。

## 摘要（原文）

> Wireless foundation models promise transformative capabilities for channel state information (CSI) processing across diverse 6G network applications, yet face fundamental challenges due to the inherent dual heterogeneity of CSI across both scale and scenario dimensions. However, current pretraining approaches either constrain inputs to fixed dimensions or isolate training by scale, limiting the generalization and scalability of wireless foundation models. In this paper, we propose HeterCSI, a channel-adaptive pretraining framework that reconciles training efficiency with robust cross-scenario generalization via a new understanding of gradient dynamics in heterogeneous CSI pretraining. Our key insight reveals that CSI scale heterogeneity primarily causes destructive gradient interference, while scenario diversity actually promotes constructive gradient alignment when properly managed. Specifically, we formulate heterogeneous CSI batch construction as a partitioning optimization problem that minimizes zero-padding overhead while preserving scenario diversity. To solve this, we develop a scale-aware adaptive batching strategy that aligns CSI samples of similar scales, and design a double-masking mechanism to isolate valid signals from padding artifacts. Extensive experiments on 12 datasets demonstrate that HeterCSI establishes a generalized foundation model without scenario-specific finetuning, achieving superior average performance over full-shot baselines. Compared to the state-of-the-art zero-shot benchmark WiFo, it reduces NMSE by 7.19 dB, 4.08 dB, and 5.27 dB for CSI reconstruction, time-domain, and frequency-domain prediction, respectively. The proposed HeterCSI framework also reduces training latency by 53% compared to existing approaches while improving generalization performance by 1.53 dB on average.

