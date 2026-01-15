---
layout: default
title: Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning
---

# Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning
**arXiv**：[2601.09708v1](https://arxiv.org/abs/2601.09708) · [PDF](https://arxiv.org/pdf/2601.09708.pdf)  
**作者**：Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz, Yu-Chiang Frank Wang, Fu-En Yang  

**一句话要点**：提出Fast-ThinkAct框架，通过可言语化潜在规划实现高效视觉-语言-动作推理，以降低推理延迟。

**关键词**：视觉-语言-动作推理, 潜在规划, 蒸馏训练, 推理延迟优化, 具身控制, 思维链压缩

## 3 点简述
- 核心问题：视觉-语言-动作任务中显式思维链推理导致高推理延迟，影响动态环境适应性。
- 方法要点：通过教师蒸馏学习潜在思维链，结合偏好引导目标对齐操作轨迹，实现紧凑规划。
- 实验或效果：在多个基准测试中，推理延迟降低高达89.3%，同时保持长时规划、少样本适应和失败恢复能力。

## 摘要（原文）

> Vision-Language-Action (VLA) tasks require reasoning over complex visual scenes and executing adaptive actions in dynamic environments. While recent studies on reasoning VLAs show that explicit chain-of-thought (CoT) can improve generalization, they suffer from high inference latency due to lengthy reasoning traces. We propose Fast-ThinkAct, an efficient reasoning framework that achieves compact yet performant planning through verbalizable latent reasoning. Fast-ThinkAct learns to reason efficiently with latent CoTs by distilling from a teacher, driven by a preference-guided objective to align manipulation trajectories that transfers both linguistic and visual planning capabilities for embodied control. This enables reasoning-enhanced policy learning that effectively connects compact reasoning to action execution. Extensive experiments across diverse embodied manipulation and reasoning benchmarks demonstrate that Fast-ThinkAct achieves strong performance with up to 89.3\% reduced inference latency over state-of-the-art reasoning VLAs, while maintaining effective long-horizon planning, few-shot adaptation, and failure recovery.

