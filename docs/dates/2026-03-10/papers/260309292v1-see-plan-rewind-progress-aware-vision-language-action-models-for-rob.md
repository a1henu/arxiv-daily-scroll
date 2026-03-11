---
layout: default
title: See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation
---

# See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation
**arXiv**：[2603.09292v1](https://arxiv.org/abs/2603.09292) · [PDF](https://arxiv.org/pdf/2603.09292.pdf)  
**作者**：Tingjun Dai, Mingfei Han, Tingwen Du, Zhiheng Liu, Zhihui Li, Salman Khan, Jun Yu, Xiaojun Chang  

**一句话要点**：提出SPR框架以增强机器人操作中的任务进度感知与鲁棒性

**关键词**：机器人操作, 视觉语言动作模型, 进度感知, 鲁棒性, 闭环控制, 泛化能力

## 3 点简述
- 核心问题：机器人操作中缺乏任务进度感知，导致失败检测与恢复困难
- 方法要点：通过See-Plan-Rewind循环动态将语言指令映射为空间子目标序列
- 实验或效果：在LIBERO和LIBERO-Plus基准上超越基线，展示优越的泛化与鲁棒性

## 摘要（原文）

> Measurement of task progress through explicit, actionable milestones is critical for robust robotic manipulation. This progress awareness enables a model to ground its current task status, anticipate verifiable intermediate states, and detect and recover from failures when progress stalls. To embody this capability, we introduce See, Plan, Rewind (SPR), a progress-aware vision-language-action framework that dynamically grounds language instructions into a sequence of spatial subgoals. SPR operates through a continuous core cycle, Seeing the current state and upcoming milestone, Planning a trajectory towards the next 2D waypoint, and Rewinding to a recoverable state upon failure by monitoring progress against the expected sequence. This closed-loop approach enables robust error correction without requiring additional training data or auxiliary models. Extensive experiments demonstrate the framework's effectiveness, generalization and robustness: SPR outperforms the MolmoAct baseline by 5\% on the LIBERO benchmark. On the challenging LIBERO-Plus benchmark with unseen instructions and initial states, SPR achieves state-of-the-art robustness with the smallest performance drop, surpassing OpenVLA-OFT and UniVLA, demonstrating superior out-of-distribution robustness.

