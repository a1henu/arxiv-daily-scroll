---
layout: default
title: Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining
---

# Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining
**arXiv**：[2603.01465v1](https://arxiv.org/abs/2603.01465) · [PDF](https://arxiv.org/pdf/2603.01465.pdf)  
**作者**：Yipeng Chen, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, Heng Tao Shen  

**一句话要点**：提出Keyframe-Chaining VLA框架，通过关键帧链建模非马尔可夫长时程依赖以提升机器人操作性能

**关键词**：非马尔可夫依赖, 长时程机器人操作, 关键帧选择, 视觉语言动作模型, 进度感知查询

## 3 点简述
- 核心问题：现有VLA模型依赖即时观测，难以泛化到长时程任务，且无法有效捕捉非马尔可夫依赖。
- 方法要点：设计自动关键帧选择器和进度感知查询机制，提取并链接历史关键帧作为视觉令牌集成到VLA中。
- 实验或效果：在基于ManiSkill模拟器的四个非马尔可夫操作任务上验证，方法表现优异，有效处理长时程依赖。

## 摘要（原文）

> Existing Vision-Language-Action (VLA) models often struggle to generalize to long-horizon tasks due to their heavy reliance on immediate observations. While recent studies incorporate retrieval mechanisms or extend context windows to handle procedural tasks, they often struggle to capture Non-Markovian dependencies, where optimal actions rely solely on specific past states rather than the current observation. To address this, we introduce Keyframe-Chaining VLA, a framework that extracts and links key historical frames to model long-horizon dependencies. Specifically, we propose an automatic keyframe selector that learns a discriminative embedding space, effectively identifying distinct state transitions. To capture task-critical information, we design a progress-aware query mechanism that dynamically retrieves historical frames based on their temporal relevance to the current execution phase. These selected keyframes are integrated into the VLA as interleaved visual tokens, explicitly grounding the policy in the long-horizon temporal context. Finally, we introduce a suite of four Non-Markovian manipulation tasks built upon the ManiSkill simulator to measure task success rates. Experimental results demonstrate that our method achieves superior performance, effectively tackling robot manipulation tasks characterized by long-horizon temporal dependencies. Code is available at https://github.com/cytoplastm/KC-VLA.

