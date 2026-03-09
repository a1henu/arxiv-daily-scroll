---
layout: default
title: History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation
---

# History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation
**arXiv**：[2603.06480v1](https://arxiv.org/abs/2603.06480) · [PDF](https://arxiv.org/pdf/2603.06480.pdf)  
**作者**：Qitong Wang, Yijun Liang, Ming Li, Tianyi Zhou, Christopher Rasmussen  

**一句话要点**：提出无需训练的历史条件时空视觉令牌剪枝框架，以提升视觉语言导航的推理效率

**关键词**：视觉语言导航, 令牌剪枝, 时空压缩, 推理效率, 无需训练, 机器人部署

## 3 点简述
- 核心问题：视觉语言导航中视觉语言动作模型计算成本高，导致延迟，限制实时部署。
- 方法要点：基于注意力的令牌重要性和查询引导的时空过滤，对当前视图和历史记忆进行令牌剪枝，无需重新训练。
- 实验或效果：在标准基准测试中优于现有剪枝策略，保持高导航精度和推理效率，并在真实机器人上验证低延迟导航。

## 摘要（原文）

> Vision-Language Navigation (VLN) enables robots to follow natural-language instructions in visually grounded environments, serving as a key capability for embodied robotic systems. Recent Vision-Language-Action (VLA) models have demonstrated strong navigation performance, but their high computational cost introduces latency that limits real-time deployment. We propose a training-free spatio-temporal vision token pruning framework tailored to VLA-based VLN. We apply spatial token selection to the current view, alongside spatio-temporal compression for historical memories, enabling efficient long-horizon inference while reducing redundant computation. Leveraging attention-based token importance and query-guided spatio-temporal filtering, the proposed approach preserves navigation-relevant information without retraining or modifying pretrained models, allowing plug-and-play integration into existing VLA systems. Through experiments on standard VLN benchmarks, we confirm that our method significantly outperforms existing pruning strategies. It successfully preserves superior navigation accuracy under extreme pruning scenarios, all while maintaining the highly competitive inference efficiency. Real-world deployment on a Unitree Go2 quadruped robot further validates reliable and low-latency instruction-following navigation under practical robotic constraints. We hope this work helps bridge the gap between large-scale multimodal modeling and efficient, real-time embodied deployment in robotic navigation systems.

