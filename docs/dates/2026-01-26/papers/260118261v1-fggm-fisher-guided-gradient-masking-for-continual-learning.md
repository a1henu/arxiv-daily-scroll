---
layout: default
title: FGGM: Fisher-Guided Gradient Masking for Continual Learning
---

# FGGM: Fisher-Guided Gradient Masking for Continual Learning
**arXiv**：[2601.18261v1](https://arxiv.org/abs/2601.18261) · [PDF](https://arxiv.org/pdf/2601.18261.pdf)  
**作者**：Chao-Hong Tan, Qian Chen, Wen Wang, Yukun Ma, Chong Zhang, Chong Deng, Qinglin Zhang, Xiangang Li, Jieping Ye  

**一句话要点**：提出Fisher-Guided Gradient Masking以缓解大语言模型持续学习中的灾难性遗忘

**关键词**：持续学习, 灾难性遗忘, Fisher信息, 梯度掩码, 大语言模型, 参数重要性估计

## 3 点简述
- 核心问题：灾难性遗忘阻碍大语言模型的持续学习能力
- 方法要点：基于对角Fisher信息动态生成二元掩码，选择性更新参数以平衡稳定性和可塑性
- 实验或效果：在TRACE基准上相对SFT提升9.6%，优于MIGU，代码生成任务验证性能

## 摘要（原文）

> Catastrophic forgetting impairs the continuous learning of large language models. We propose Fisher-Guided Gradient Masking (FGGM), a framework that mitigates this by strategically selecting parameters for updates using diagonal Fisher Information. FGGM dynamically generates binary masks with adaptive thresholds, preserving critical parameters to balance stability and plasticity without requiring historical data. Unlike magnitude-based methods such as MIGU, our approach offers a mathematically principled parameter importance estimation. On the TRACE benchmark, FGGM shows a 9.6% relative improvement in retaining general capabilities over supervised fine-tuning (SFT) and a 4.4% improvement over MIGU on TRACE tasks. Additional analysis on code generation tasks confirms FGGM's superior performance and reduced forgetting, establishing it as an effective solution.

