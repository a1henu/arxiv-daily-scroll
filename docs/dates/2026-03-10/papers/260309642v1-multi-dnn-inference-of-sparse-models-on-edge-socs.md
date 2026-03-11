---
layout: default
title: Multi-DNN Inference of Sparse Models on Edge SoCs
---

# Multi-DNN Inference of Sparse Models on Edge SoCs
**arXiv**：[2603.09642v1](https://arxiv.org/abs/2603.09642) · [PDF](https://arxiv.org/pdf/2603.09642.pdf)  
**作者**：Jiawei Luo, Di Wu, Simon Dobson, Blesson Varghese  

**一句话要点**：提出模型缝合技术以解决边缘SoC上多DNN推理系统效率低下的问题

**关键词**：多DNN推理, 模型缝合, 边缘计算, 稀疏模型, 异构处理器, SLO优化

## 3 点简述
- 核心问题：现有系统每任务仅支持单一模型，导致资源匹配不佳和SLO违规率高
- 方法要点：通过重组稀疏模型的子图创建变体，无需重新训练，实现模型缝合
- 实验或效果：SparseLoom系统降低SLO违规率最高74%，提升吞吐量最高2.31倍，平均减少内存开销28%

## 摘要（原文）

> Modern edge applications increasingly require multi-DNN inference systems to execute tasks on heterogeneous processors, gaining performance from both concurrent execution and from matching each model to the most suited accelerator. However, existing systems support only a single model (or a few sparse variants) per task, which impedes the efficiency of this matching and results in high Service Level Objective violation rates. We introduce model stitching for multi-DNN inference systems, which creates model variants by recombining subgraphs from sparse models without re-training. We present a demonstrator system, SparseLoom, that shows model stitching can be deployed to SoCs. We show experimentally that SparseLoom reduces SLO violation rates by up to 74%, improves throughput by up to 2.31x, and lowers memory overhead by an average of 28% compared to state-of-the-art multi-DNN inference systems.

