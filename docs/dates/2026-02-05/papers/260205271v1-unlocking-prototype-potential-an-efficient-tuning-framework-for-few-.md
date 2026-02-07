---
layout: default
title: Unlocking Prototype Potential: An Efficient Tuning Framework for Few-Shot Class-Incremental Learning
---

# Unlocking Prototype Potential: An Efficient Tuning Framework for Few-Shot Class-Incremental Learning
**arXiv**：[2602.05271v1](https://arxiv.org/abs/2602.05271) · [PDF](https://arxiv.org/pdf/2602.05271.pdf)  
**作者**：Shengqin Jiang, Xiaoran Feng, Yuankai Qi, Haokui Zhang, Renlong Hang, Qingshan Liu, Lina Yao, Quan Z. Sheng, Ming-Hsuan Yang  

**一句话要点**：提出原型微调框架以解决少样本类增量学习中的决策区域优化问题

**关键词**：少样本类增量学习, 原型微调, 双校准方法, 决策区域优化, 高效参数更新

## 3 点简述
- 核心问题：传统方法使用静态原型，受限于骨干网络表示偏差，难以在数据稀缺下提升全局判别力。
- 方法要点：冻结特征提取器，通过类特定和任务感知偏移的双校准方法，动态微调原型以优化决策区域。
- 实验或效果：在多个基准测试中实现优越性能，同时仅需少量可学习参数。

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) seeks to continuously learn new classes from very limited samples while preserving previously acquired knowledge. Traditional methods often utilize a frozen pre-trained feature extractor to generate static class prototypes, which suffer from the inherent representation bias of the backbone. While recent prompt-based tuning methods attempt to adapt the backbone via minimal parameter updates, given the constraint of extreme data scarcity, the model's capacity to assimilate novel information and substantively enhance its global discriminative power is inherently limited. In this paper, we propose a novel shift in perspective: freezing the feature extractor while fine-tuning the prototypes. We argue that the primary challenge in FSCIL is not feature acquisition, but rather the optimization of decision regions within a static, high-quality feature space. To this end, we introduce an efficient prototype fine-tuning framework that evolves static centroids into dynamic, learnable components. The framework employs a dual-calibration method consisting of class-specific and task-aware offsets. These components function synergistically to improve the discriminative capacity of prototypes for ongoing incremental classes. Extensive results demonstrate that our method attains superior performance across multiple benchmarks while requiring minimal learnable parameters.

