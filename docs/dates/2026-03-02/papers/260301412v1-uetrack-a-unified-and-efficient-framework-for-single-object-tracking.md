---
layout: default
title: UETrack: A Unified and Efficient Framework for Single Object Tracking
---

# UETrack: A Unified and Efficient Framework for Single Object Tracking
**arXiv**：[2603.01412v1](https://arxiv.org/abs/2603.01412) · [PDF](https://arxiv.org/pdf/2603.01412.pdf)  
**作者**：Ben Kang, Jie Zhao, Xin Chen, Wanting Geng, Bin Zhang, Lu Zhang, Dong Wang, Huchuan Lu  

**一句话要点**：提出UETrack统一高效框架，解决单目标跟踪中多模态场景效率低下的问题。

**关键词**：单目标跟踪, 多模态跟踪, 混合专家机制, 自适应蒸馏, 高效框架, 实时性能

## 3 点简述
- 核心问题：现有方法局限于RGB输入，多模态跟踪设计复杂且效率低，难以在资源受限环境中部署。
- 方法要点：引入基于Token-Pooling的混合专家机制增强建模能力，采用目标感知自适应蒸馏策略减少冗余监督。
- 实验或效果：在12个基准测试和3个硬件平台上，UETrack实现速度-精度平衡，例如UETrack-B在LaSOT上达到69.2% AUC，GPU/CPU/AGX上分别运行163/56/60 FPS。

## 摘要（原文）

> With growing real-world demands, efficient tracking has received increasing attention. However, most existing methods are limited to RGB inputs and struggle in multi-modal scenarios. Moreover, current multi-modal tracking approaches typically use complex designs, making them too heavy and slow for resource-constrained deployment. To tackle these limitations, we propose UETrack, an efficient framework for single object tracking. UETrack demonstrates high practicality and versatility, efficiently handling multiple modalities including RGB, Depth, Thermal, Event, and Language, and addresses the gap in efficient multi-modal tracking. It introduces two key components: a Token-Pooling-based Mixture-of-Experts mechanism that enhances modeling capacity through feature aggregation and expert specialization, and a Target-aware Adaptive Distillation strategy that selectively performs distillation based on sample characteristics, reducing redundant supervision and improving performance. Extensive experiments on 12 benchmarks across 3 hardware platforms show that UETrack achieves a superior speed-accuracy trade-off compared to previous methods. For instance, UETrack-B achieves 69.2% AUC on LaSOT and runs at 163/56/60 FPS on GPU/CPU/AGX, demonstrating strong practicality and versatility. Code is available at https://github.com/kangben258/UETrack.

