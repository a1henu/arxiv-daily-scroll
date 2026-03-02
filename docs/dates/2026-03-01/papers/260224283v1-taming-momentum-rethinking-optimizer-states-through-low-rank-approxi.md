---
layout: default
title: Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation
---

# Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation
**arXiv**：[2602.24283v1](https://arxiv.org/abs/2602.24283) · [PDF](https://arxiv.org/pdf/2602.24283.pdf)  
**作者**：Zhengbo Wang, Jian Liang, Ran He, Zilei Wang, Tieniu Tan  

**一句话要点**：提出LoRA-Pre低秩优化器，通过低秩近似减少动量内存开销，提升大模型预训练和微调效率。

**关键词**：低秩近似, 优化器内存效率, 大语言模型预训练, 微调优化, 动量分解, 在线学习

## 3 点简述
- 现代优化器如Adam依赖动量导致内存开销大，限制大模型可扩展性。
- 将动量指数移动平均重构为在线线性回归，引入低秩分解减少内存占用。
- 在Llama架构预训练和微调中验证，性能优于基线，内存效率显著提升。

## 摘要（原文）

> Modern optimizers like Adam and Muon are central to training large language models, but their reliance on first- and second-order momenta introduces significant memory overhead, which constrains scalability and computational efficiency. In this work, we reframe the exponential moving average (EMA) used in these momenta as the training of a linear regressor via online gradient flow. Building on this equivalence, we introduce LoRA-Pre, a novel low-rank optimizer designed for efficient pre-training. Specifically, LoRA-Pre reduces the optimizer's memory footprint by decomposing the full momentum matrix into a compact low-rank subspace within the online linear learner, thereby maintaining optimization performance while improving memory efficiency. We empirically validate LoRA-Pre's efficacy by pre-training models from the Llama architecture family, scaling from 60M to 1B parameters. LoRA-Pre achieves the highest performance across all model sizes. Notably, LoRA-Pre demonstrates remarkable rank efficiency, achieving comparable or superior results using only 1/8 the rank of baseline methods. Beyond pre-training, we evaluate LoRA-Pre's effectiveness in fine-tuning scenarios. With the same rank, LoRA-Pre consistently outperforms all efficient fine-tuning baselines. Specifically, compared to standard LoRA, LoRA-Pre achieves substantial improvements of 3.14 points on Llama-3.1-8B and 6.17 points on Llama-2-7B, validating our approach's effectiveness across both pre-training and fine-tuning paradigms. Our code is publicly available at https://github.com/mrflogs/LoRA-Pre.

