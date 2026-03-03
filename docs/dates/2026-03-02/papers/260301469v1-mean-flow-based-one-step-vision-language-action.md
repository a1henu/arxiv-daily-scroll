---
layout: default
title: Mean-Flow based One-Step Vision-Language-Action
---

# Mean-Flow based One-Step Vision-Language-Action
**arXiv**：[2603.01469v1](https://arxiv.org/abs/2603.01469) · [PDF](https://arxiv.org/pdf/2603.01469.pdf)  
**作者**：Yang Chen, Xiaoguang Ma, Bin Zhao  

**一句话要点**：提出基于均值流的单步视觉-语言-动作方法，以解决机器人操作中动作生成延迟问题。

**关键词**：视觉-语言-动作, 机器人操作, 流匹配, 单步生成, 动作生成, 高效骨干

## 3 点简述
- 核心问题：基于流匹配的视觉-语言-动作框架因迭代采样导致生成延迟，限制实际应用。
- 方法要点：通过解决噪声诱导问题，消除传统流匹配的一致性约束，实现高效单步动作生成。
- 实验或效果：在真实机器人实验中，生成速度比SmolVLA和Diffusion Policy分别快8.7倍和83.9倍。

## 摘要（原文）

> Recent advances in FlowMatching-based Vision-Language-Action (VLA) frameworks have demonstrated remarkable advantages in generating high-frequency action chunks, particularly for highly dexterous robotic manipulation tasks. Despite these notable achievements, their practical applications are constrained by prolonged generation latency, which stems from inherent iterative sampling requirements and architectural limitations. To address this critical bottleneck, we propose a Mean-Flow based One-Step VLA approach. Specifically, we resolve the noise-induced issues in the action generation process, thereby eliminating the consistency constraints inherent to conventional Flow-Matching methods. This significantly enhances generation efficiency and enables one-step action generation. Real-world robotic experiments show that the generation speed of the proposed Mean-Flow based One-Step VLA is 8.7 times and 83.9 times faster than that of SmolVLA and Diffusion Policy, respectively. These results elucidate its great potential as a high-efficiency backbone for VLA-based robotic manipulation.

