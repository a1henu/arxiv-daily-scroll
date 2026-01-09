---
layout: default
title: How to Set the Batch Size for Large-Scale Pre-training?
---

# How to Set the Batch Size for Large-Scale Pre-training?
**arXiv**：[2601.05034v1](https://arxiv.org/abs/2601.05034) · [PDF](https://arxiv.org/pdf/2601.05034.pdf)  
**作者**：Yunhua Zhou, Junhao Huang, Shuhao Xin, Yechen Zhang, Runyu Peng, Qiping Guo, Xipeng Qiu  

**一句话要点**：提出动态批大小调度器以优化WSD调度下的大规模预训练效率

**关键词**：大规模预训练, 批大小调度, 学习率调度, 训练效率, 数据效率, WSD调度器

## 3 点简述
- 核心问题：传统临界批大小理论不适用于WSD学习率调度器，导致理论与实际预训练动态脱节。
- 方法要点：推导WSD调度下的E(S)关系，定义最小批大小B_min和最优批大小B_opt，并基于此设计动态批大小调度策略。
- 实验或效果：实验验证修订公式准确捕捉预训练动态，调度策略显著提升训练效率和最终模型质量。

## 摘要（原文）

> The concept of Critical Batch Size, as pioneered by OpenAI, has long served as a foundational principle for large-scale pre-training. However, with the paradigm shift towards the Warmup-Stable-Decay (WSD) learning rate scheduler, we observe that the original theoretical framework and its underlying mechanisms fail to align with new pre-training dynamics. To bridge this gap between theory and practice, this paper derives a revised E(S) relationship tailored for WSD scheduler, characterizing the trade-off between training data consumption E and steps S during pre-training. Our theoretical analysis reveals two fundamental properties of WSD-based pre-training: 1) B_min, the minimum batch size threshold required to achieve a target loss, and 2) B_opt, the optimal batch size that maximizes data efficiency by minimizing total tokens. Building upon these properties, we propose a dynamic Batch Size Scheduler. Extensive experiments demonstrate that our revised formula precisely captures the dynamics of large-scale pre-training, and the resulting scheduling strategy significantly enhances both training efficiency and final model quality.

