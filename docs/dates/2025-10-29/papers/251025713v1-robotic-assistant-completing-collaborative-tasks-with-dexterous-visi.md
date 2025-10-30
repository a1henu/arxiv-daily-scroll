---
layout: default
title: Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models
---

# Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models
**arXiv**：[2510.25713v1](https://arxiv.org/abs/2510.25713) · [PDF](https://arxiv.org/pdf/2510.25713.pdf)  
**作者**：Boshi An, Chenyu Yang, Robert Katzschmann  

**一句话要点**：提出改进的视觉-语言-动作模型，用于灵巧人机协作任务，减少语言提示需求。

**关键词**：视觉-语言-动作模型, 人机协作, 动作后处理, 意图预测, 机器人控制, 多模态学习

## 3 点简述
- 核心问题：如何使预训练VLA模型适应灵巧人机协作，减少语言提示依赖。
- 方法要点：添加FiLM条件化、辅助意图头和动作后处理，预测紧凑动作。
- 实验或效果：在真实机器人上实现长视野行为，动作后处理是性能主要驱动因素。

## 摘要（原文）

> We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for
> dexterous human-robot collaboration with minimal language prompting. Our
> approach adds (i) FiLM conditioning to visual backbones for task-aware
> perception, (ii) an auxiliary intent head that predicts collaborator hand pose
> and target cues, and (iii) action-space post-processing that predicts compact
> deltas (position/rotation) and PCA-reduced finger joints before mapping to full
> commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset
> augmented with MediaPipe hand poses, we demonstrate that delta actions are
> well-behaved and that four principal components explain ~96% of hand-joint
> variance. Ablations identify action post-processing as the primary performance
> driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is
> detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes
> "pick-up" and "pass" into a long-horizon behavior. We surface "trainer
> overfitting" to specific demonstrators as the key limitation.

