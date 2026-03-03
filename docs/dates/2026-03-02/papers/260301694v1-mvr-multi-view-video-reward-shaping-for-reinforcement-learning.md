---
layout: default
title: MVR: Multi-view Video Reward Shaping for Reinforcement Learning
---

# MVR: Multi-view Video Reward Shaping for Reinforcement Learning
**arXiv**：[2603.01694v1](https://arxiv.org/abs/2603.01694) · [PDF](https://arxiv.org/pdf/2603.01694.pdf)  
**作者**：Lirui Luo, Guoxi Zhang, Hongming Xu, Yaodong Yang, Cong Fang, Qing Li  

**一句话要点**：提出多视角视频奖励塑形框架以解决强化学习中视觉反馈的偏差与动态任务挑战

**关键词**：强化学习, 奖励塑形, 多视角视频, 视觉语言模型, 动态任务, 状态相关性

## 3 点简述
- 核心问题：基于单视角静态图像的视觉语言模型奖励方法易受姿态偏差影响，难以处理动态复杂任务。
- 方法要点：利用多视角视频和视频-文本相似性学习状态相关性函数，结合任务奖励进行状态依赖的奖励塑形。
- 实验或效果：在HumanoidBench和MetaWorld任务上验证有效性，并通过消融研究确认设计选择。

## 摘要（原文）

> Reward design is of great importance for solving complex tasks with reinforcement learning. Recent studies have explored using image-text similarity produced by vision-language models (VLMs) to augment rewards of a task with visual feedback. A common practice linearly adds VLM scores to task or success rewards without explicit shaping, potentially altering the optimal policy. Moreover, such approaches, often relying on single static images, struggle with tasks whose desired behavior involves complex, dynamic motions spanning multiple visually different states. Furthermore, single viewpoints can occlude critical aspects of an agent's behavior. To address these issues, this paper presents Multi-View Video Reward Shaping (MVR), a framework that models the relevance of states regarding the target task using videos captured from multiple viewpoints. MVR leverages video-text similarity from a frozen pre-trained VLM to learn a state relevance function that mitigates the bias towards specific static poses inherent in image-based methods. Additionally, we introduce a state-dependent reward shaping formulation that integrates task-specific rewards and VLM-based guidance, automatically reducing the influence of VLM guidance once the desired motion pattern is achieved. We confirm the efficacy of the proposed framework with extensive experiments on challenging humanoid locomotion tasks from HumanoidBench and manipulation tasks from MetaWorld, verifying the design choices through ablation studies.

