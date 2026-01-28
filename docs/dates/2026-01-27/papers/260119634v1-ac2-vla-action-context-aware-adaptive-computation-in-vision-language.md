---
layout: default
title: AC^2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation
---

# AC^2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation
**arXiv**：[2601.19634v1](https://arxiv.org/abs/2601.19634) · [PDF](https://arxiv.org/pdf/2601.19634.pdf)  
**作者**：Wenda Yu, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu  

**一句话要点**：提出AC^2-VLA框架，通过动作上下文感知自适应计算，提升视觉-语言-动作模型在机器人操作中的效率。

**关键词**：视觉-语言-动作模型, 自适应计算, 机器人操作, 动作上下文感知, 认知重用, 令牌剪枝

## 3 点简述
- 核心问题：VLA模型在闭环部署中因重复运行大型视觉-语言骨干网络导致高延迟和高计算成本。
- 方法要点：基于动作上下文，自适应执行时间步认知重用、令牌剪枝和模型组件选择性执行。
- 实验或效果：在机器人操作基准测试中，实现1.79倍加速，FLOPs降至密集基线的29.4%，任务成功率相当。

## 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet their closed-loop deployment is hindered by the high latency and compute cost of repeatedly running large vision-language backbones at every timestep. We observe that VLA inference exhibits structured redundancies across temporal, spatial, and depth dimensions, and that most existing efficiency methods ignore action context, despite its central role in embodied tasks. To address this gap, we propose Action-Context-aware Adaptive Computation for VLA models (AC^2-VLA), a unified framework that conditions computation on current visual observations, language instructions, and previous action states. Based on this action-centric context, AC^2-VLA adaptively performs cognition reuse across timesteps, token pruning, and selective execution of model components within a unified mechanism. To train the adaptive policy, we introduce an action-guided self-distillation scheme that preserves the behavior of the dense VLA policy while enabling structured sparsification that transfers across tasks and settings. Extensive experiments on robotic manipulation benchmarks show that AC^2-VLA achieves up to a 1.79\times speedup while reducing FLOPs to 29.4% of the dense baseline, with comparable task success.

