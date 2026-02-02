---
layout: default
title: Detect and Act: Automated Dynamic Optimizer through Meta-Black-Box Optimization
---

# Detect and Act: Automated Dynamic Optimizer through Meta-Black-Box Optimization
**arXiv**：[2601.22542v1](https://arxiv.org/abs/2601.22542) · [PDF](https://arxiv.org/pdf/2601.22542.pdf)  
**作者**：Zijian Gao, Yuanting Zhong, Zeyuan Ma, Yue-Jiao Gong, Hongshu Guo  

**一句话要点**：提出基于元黑盒优化的强化学习辅助方法，实现动态优化问题的自动检测与自适应

**关键词**：动态优化问题, 元黑盒优化, 强化学习, 进化算法, 自适应策略, 深度Q网络

## 3 点简述
- 核心问题：现有进化动态优化方法依赖人工策略，在未知场景中可能失效
- 方法要点：使用深度Q网络作为优化动态检测器和搜索策略适配器，基于元黑盒优化思想
- 实验或效果：在多样化合成实例测试床上验证，相比先进基线展现灵活搜索行为和优越性能

## 摘要（原文）

> Dynamic Optimization Problems (DOPs) are challenging to address due to their complex nature, i.e., dynamic environment variation. Evolutionary Computation methods are generally advantaged in solving DOPs since they resemble dynamic biological evolution. However, existing evolutionary dynamic optimization methods rely heavily on human-crafted adaptive strategy to detect environment variation in DOPs, and then adapt the searching strategy accordingly. These hand-crafted strategies may perform ineffectively at out-of-box scenarios. In this paper, we propose a reinforcement learning-assisted approach to enable automated variation detection and self-adaption in evolutionary algorithms. This is achieved by borrowing the bi-level learning-to-optimize idea from recent Meta-Black-Box Optimization works. We use a deep Q-network as optimization dynamics detector and searching strategy adapter: It is fed as input with current-step optimization state and then dictates desired control parameters to underlying evolutionary algorithms for next-step optimization. The learning objective is to maximize the expected performance gain across a problem distribution. Once trained, our approach could generalize toward unseen DOPs with automated environment variation detection and self-adaption. To facilitate comprehensive validation, we further construct an easy-to-difficult DOPs testbed with diverse synthetic instances. Extensive benchmark results demonstrate flexible searching behavior and superior performance of our approach in solving DOPs, compared to state-of-the-art baselines.

