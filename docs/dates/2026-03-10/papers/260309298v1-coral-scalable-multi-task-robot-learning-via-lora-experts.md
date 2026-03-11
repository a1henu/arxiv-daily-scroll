---
layout: default
title: CORAL: Scalable Multi-Task Robot Learning via LoRA Experts
---

# CORAL: Scalable Multi-Task Robot Learning via LoRA Experts
**arXiv**：[2603.09298v1](https://arxiv.org/abs/2603.09298) · [PDF](https://arxiv.org/pdf/2603.09298.pdf)  
**作者**：Yuankai Luo, Woping Chen, Tong Liang, Zhenguo Li  

**一句话要点**：提出CORAL框架，通过LoRA专家解决机器人多任务学习中的任务干扰问题。

**关键词**：多任务机器人学习, LoRA专家, 任务干扰缓解, 动态推理引擎, 视觉语言动作模型

## 3 点简述
- 核心问题：多任务联合微调时梯度冲突导致负迁移，降低单任务性能。
- 方法要点：冻结预训练VLA骨干，为每个任务附加轻量LoRA专家，运行时动态路由指令。
- 实验或效果：在真实和仿真机器人上验证，显著优于联合训练，支持任务持续扩展。

## 摘要（原文）

> Deploying Vision-Language-Action (VLA) models in real-world robotics exposes a core multi-task learning challenge: reconciling task interference in multi-task robotic learning. When multiple tasks are jointly fine-tuned in a single stage, gradients from different tasks can conflict, causing negative transfer and reducing per-task performance. Yet maintaining a separate full checkpoint per task is often storage- and deployment-prohibitive. To address this dilemma, we present CORAL, a backbone- and embodiment-agnostic framework designed primarily to mitigate multi-task interference while remaining naturally extensible to a continuous stream of new tasks. CORAL freezes a single pre-trained VLA backbone and attaches one lightweight Low-Rank Adaptation (LoRA) expert per task; at runtime, a dynamic inference engine (the CORAL Manager) routes language instructions to the appropriate expert and swaps experts on the fly with zero inference overhead. This strict parameter isolation avoids complex gating networks and prevents parameter-level cross-task interference by construction; as an added capability, it also enables sequentially introducing new tasks without parameter overwriting caused by catastrophic forgetting. We validate CORAL on a real-world Galaxea R1 dual-arm mobile manipulator and three simulation benchmarks (LIBERO, WidowX, Google Robot), where CORAL overcomes fine-grained instructional ambiguity and substantially outperforms joint training, yielding a practical and scalable system for lifelong multi-task robot learning. Website: https://frontierrobo.github.io/CORAL

