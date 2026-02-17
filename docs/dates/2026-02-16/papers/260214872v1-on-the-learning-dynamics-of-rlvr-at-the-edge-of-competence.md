---
layout: default
title: On the Learning Dynamics of RLVR at the Edge of Competence
---

# On the Learning Dynamics of RLVR at the Edge of Competence
**arXiv**：[2602.14872v1](https://arxiv.org/abs/2602.14872) · [PDF](https://arxiv.org/pdf/2602.14872.pdf)  
**作者**：Yu Huang, Zixin Wen, Yuejie Chi, Yuting Wei, Aarti Singh, Yingbin Liang, Yuxin Chen  

**一句话要点**：提出基于难度谱平滑性的RLVR训练动态理论，以解释其在组合推理任务中的学习机制。

**关键词**：强化学习, 可验证奖励, 训练动态, 组合推理, 傅里叶分析, 难度谱

## 3 点简述
- 核心问题：仅基于最终结果的奖励如何帮助强化学习克服长视野推理障碍。
- 方法要点：利用有限群上的傅里叶分析工具，理论分析RL在组合推理任务中的训练动态。
- 实验或效果：通过合成实验验证理论预测，表明平滑难度谱能实现稳定改进。

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has been a main driver of recent breakthroughs in large reasoning models. Yet it remains a mystery how rewards based solely on final outcomes can help overcome the long-horizon barrier to extended reasoning. To understand this, we develop a theory of the training dynamics of RL for transformers on compositional reasoning tasks. Our theory characterizes how the effectiveness of RLVR is governed by the smoothness of the difficulty spectrum. When data contains abrupt discontinuities in difficulty, learning undergoes grokking-type phase transitions, producing prolonged plateaus before progress recurs. In contrast, a smooth difficulty spectrum leads to a relay effect: persistent gradient signals on easier problems elevate the model's capabilities to the point where harder ones become tractable, resulting in steady and continuous improvement. Our theory explains how RLVR can improve performance at the edge of competence, and suggests that appropriately designed data mixtures can yield scalable gains. As a technical contribution, our analysis develops and adapts tools from Fourier analysis on finite groups to our setting. We validate the predicted mechanisms empirically via synthetic experiments.

