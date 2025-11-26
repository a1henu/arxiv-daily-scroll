---
layout: default
title: Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving
---

# Map-World: Masked Action planning and Path-Integral World Model for Autonomous Driving
**arXiv**：[2511.20156v1](https://arxiv.org/abs/2511.20156) · [PDF](https://arxiv.org/pdf/2511.20156.pdf)  
**作者**：Bin Hu, Zijian Lu, Haicheng Liao, Chengran Yuan, Bin Rao, Yongkang Li, Guofa Li, Zhiyong Cui, Cheng-zhong Xu, Zhenning Li  

**一句话要点**：提出MAP-World框架，通过掩码动作规划和路径积分世界模型实现自动驾驶多模态运动规划。

**关键词**：自动驾驶规划, 多模态轨迹, 世界模型, 掩码序列, 路径积分, 实时推理

## 3 点简述
- 自动驾驶运动规划需处理多模态未来，但现有方法依赖手工锚点或强化学习，丢弃信息并复杂化优化。
- MAP-World结合掩码动作规划和路径加权世界模型，生成多样轨迹并基于语义损失学习全部分布。
- 在NAVSIM上匹配锚点方法，实现世界模型方法中最优性能，保持实时推理。

## 摘要（原文）

> Motion planning for autonomous driving must handle multiple plausible futures while remaining computationally efficient. Recent end-to-end systems and world-model-based planners predict rich multi-modal trajectories, but typically rely on handcrafted anchors or reinforcement learning to select a single best mode for training and control. This selection discards information about alternative futures and complicates optimization. We propose MAP-World, a prior-free multi-modal planning framework that couples masked action planning with a path-weighted world model. The Masked Action Planning (MAP) module treats future ego motion as masked sequence completion: past waypoints are encoded as visible tokens, future waypoints are represented as mask tokens, and a driving-intent path provides a coarse scaffold. A compact latent planning state is expanded into multiple trajectory queries with injected noise, yielding diverse, temporally consistent modes without anchor libraries or teacher policies. A lightweight world model then rolls out future BEV semantics conditioned on each candidate trajectory. During training, semantic losses are computed as an expectation over modes, using trajectory probabilities as discrete path weights, so the planner learns from the full distribution of plausible futures instead of a single selected path. On NAVSIM, our method matches anchor-based approaches and achieves state-of-the-art performance among world-model-based methods, while avoiding reinforcement learning and maintaining real-time inference latency.

