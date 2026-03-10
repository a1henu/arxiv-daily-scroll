---
layout: default
title: Grow, Assess, Compress: Adaptive Backbone Scaling for Memory-Efficient Class Incremental Learning
---

# Grow, Assess, Compress: Adaptive Backbone Scaling for Memory-Efficient Class Incremental Learning
**arXiv**：[2603.08426v1](https://arxiv.org/abs/2603.08426) · [PDF](https://arxiv.org/pdf/2603.08426.pdf)  
**作者**：Adrian Garcia-Castañeda, Jon Irureta, Jon Imaz, Aizea Lojo  

**一句话要点**：提出GRACE框架以解决类增量学习中模型容量与内存效率的平衡问题

**关键词**：类增量学习, 动态模型缩放, 内存效率优化, 灾难性遗忘, 参数压缩, 饱和度评估

## 3 点简述
- 核心问题：类增量学习需平衡学习新任务的可塑性与防止灾难性遗忘的稳定性，扩展方法易导致参数爆炸和内存开销
- 方法要点：采用动态缩放框架，通过“增长、评估、压缩”循环策略自适应管理模型容量，引入饱和度评估优化决策
- 实验或效果：在多个基准测试中达到最先进性能，相比纯扩展模型内存占用减少高达73%

## 摘要（原文）

> Class Incremental Learning (CIL) poses a fundamental challenge: maintaining a balance between the plasticity required to learn new tasks and the stability needed to prevent catastrophic forgetting. While expansion-based methods effectively mitigate forgetting by adding task-specific parameters, they suffer from uncontrolled architectural growth and memory overhead. In this paper, we propose a novel dynamic scaling framework that adaptively manages model capacity through a cyclic "GRow, Assess, ComprEss" (GRACE) strategy. Crucially, we supplement backbone expansion with a novel saturation assessment phase that evaluates the utilization of the model's capacity. This assessment allows the framework to make informed decisions to either expand the architecture or compress the backbones into a streamlined representation, preventing parameter explosion. Experimental results demonstrate that our approach achieves state-of-the-art performance across multiple CIL benchmarks, while reducing memory footprint by up to a 73% compared to purely expansionist models.

