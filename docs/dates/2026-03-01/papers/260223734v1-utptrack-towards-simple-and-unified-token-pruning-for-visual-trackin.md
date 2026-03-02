---
layout: default
title: UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking
---

# UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking
**arXiv**：[2602.23734v1](https://arxiv.org/abs/2602.23734) · [PDF](https://arxiv.org/pdf/2602.23734.pdf)  
**作者**：Hao Wu, Xudong Wang, Jialiang Zhang, Junlong Tong, Xinghao Chen, Junyan Lin, Yunpu Ma, Xiaoyu Shen  

**一句话要点**：提出UTPTrack统一令牌剪枝框架，以提升视觉跟踪效率与准确性。

**关键词**：视觉跟踪, 令牌剪枝, Transformer, 多模态跟踪, 效率优化

## 3 点简述
- 问题：单流Transformer跟踪器计算开销大，现有令牌剪枝方法孤立处理组件，忽略依赖关系。
- 方法：首次联合压缩搜索区域、动态模板和静态模板，采用注意力引导、令牌类型感知策略建模冗余。
- 效果：在10个基准测试中，剪枝65.4%视觉令牌，保持99.7%基线性能，实现精度-效率新最优。

## 摘要（原文）

> One-stream Transformer-based trackers achieve advanced performance in visual object tracking but suffer from significant computational overhead that hinders real-time deployment. While token pruning offers a path to efficiency, existing methods are fragmented. They typically prune the search region, dynamic template, and static template in isolation, overlooking critical inter-component dependencies, which yields suboptimal pruning and degraded accuracy. To address this, we introduce UTPTrack, a simple and Unified Token Pruning framework that, for the first time, jointly compresses all three components. UTPTrack employs an attention-guided, token type-aware strategy to holistically model redundancy, a design that seamlessly supports unified tracking across multimodal and language-guided tasks within a single model. Extensive evaluations on 10 benchmarks demonstrate that UTPTrack achieves a new state-of-the-art in the accuracy-efficiency trade-off for pruning-based trackers, pruning 65.4% of vision tokens in RGB-based tracking and 67.5% in unified tracking while preserving 99.7% and 100.5% of baseline performance, respectively. This strong performance across both RGB and multimodal scenarios underlines its potential as a robust foundation for future research in efficient visual tracking. Code will be released at https://github.com/EIT-NLP/UTPTrack.

