---
layout: default
title: POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models
---

# POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models
**arXiv**：[2602.06822v1](https://arxiv.org/abs/2602.06822) · [PDF](https://arxiv.org/pdf/2602.06822.pdf)  
**作者**：Yi Chen, Wonjin Shin, Shuhong Liu, Tho Mai, Jeongmo Lee, Chuanbo Hua, Kun Wang, Jun Liu, Joo-Young Kim  

**一句话要点**：提出POP在线结构化剪枝框架，以支持大型基础模型的高效推理。

**关键词**：在线剪枝, 结构化剪枝, 大型基础模型, 高效推理, 自回归生成

## 3 点简述
- 核心问题：现有结构化剪枝方法在推理时采用固定剪枝决策，忽略了自回归生成中的稀疏模式。
- 方法要点：POP通过分区引导在线剪枝，在预填充阶段定义粗粒度分区，解码阶段在候选区域内生成细粒度掩码。
- 实验或效果：在多种大型基础模型上评估，POP比现有方法精度更高、计算开销更小、推理延迟更低。

## 摘要（原文）

> Large foundation models (LFMs) achieve strong performance through scaling, yet current structural pruning methods derive fixed pruning decisions during inference, overlooking sparsity patterns that emerge in the autoregressive token generation. In this paper, we propose POP (Partition-guided Online Pruning), an efficient online structural pruning framework that enables context-conditioned dynamic pruning with minimal computational overhead. POP partitions model channels into retained, candidate, and pruned regions, where prefilling defines a coarse pruning partition, and the decoding stage generates a fine-grained mask within the candidate region, avoiding full-channel re-evaluation. The coarse pruning partition preserves consistently important weights, while the fine-grained masking provides context-conditioned variation during decoding. Moreover, POP is a lightweight, plug-and-play method that requires no preprocessing, including offline calibration, retraining, or learning predictors. Extensive evaluations across diverse LFMs, including large language models (LLMs), mixture-of-experts models (MoEs), and vision-language models (VLMs), demonstrate that POP consistently delivers higher accuracy than existing pruning approaches while incurring smaller computational overhead and minimizing inference latency.

