---
layout: default
title: TADS: Task-Aware Data Selection for Multi-Task Multimodal Pre-Training
---

# TADS: Task-Aware Data Selection for Multi-Task Multimodal Pre-Training
**arXiv**：[2602.05251v1](https://arxiv.org/abs/2602.05251) · [PDF](https://arxiv.org/pdf/2602.05251.pdf)  
**作者**：Guanjie Cheng, Boyi Li, Lingyu Sun, Mengying Zhu, Yangyang Wu, Xinkui Zhao, Shuiguang Deng  

**一句话要点**：提出TADS框架以解决多任务多模态预训练中的数据选择问题

**关键词**：多任务学习, 多模态预训练, 数据选择, 元学习, 零样本性能

## 3 点简述
- 核心问题：网络爬取数据噪声大、对齐差、冗余多，导致训练低效和泛化不佳
- 方法要点：集成内在质量、任务相关性和分布多样性到可学习价值函数，通过元学习自适应优化
- 实验或效果：在CC12M上仅用36%数据，零样本性能平均提升1.0%，显著提高数据效率

## 摘要（原文）

> Large-scale multimodal pre-trained models like CLIP rely heavily on high-quality training data, yet raw web-crawled datasets are often noisy, misaligned, and redundant, leading to inefficient training and suboptimal generalization. Existing data selection methods are either heuristic-based, suffering from bias and limited diversity, or data-driven but task-agnostic, failing to optimize for multi-task scenarios. To address these gaps, we introduce TADS (Task-Aware Data Selection), a novel framework for multi-task multimodal pre-training that integrates Intrinsic Quality, Task Relevance, and Distributional Diversity into a learnable value function. TADS employs a comprehensive quality assessment system with unimodal and cross-modal operators, quantifies task relevance via interpretable similarity vectors, and optimizes diversity through cluster-based weighting. A feedback-driven meta-learning mechanism adaptively refines the selection strategy based on proxy model performance across multiple downstream tasks. Experiments on CC12M demonstrate that TADS achieves superior zero-shot performance on benchmarks like ImageNet, CIFAR-100, MS-COCO, and Flickr30K, using only 36% of the data while outperforming baselines by an average of 1.0%. This highlights that TADS significantly enhances data efficiency by curating a high-utility subset that yields a much higher performance ceiling within the same computational constraints.

