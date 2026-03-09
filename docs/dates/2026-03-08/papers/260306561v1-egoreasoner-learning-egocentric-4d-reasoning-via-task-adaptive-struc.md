---
layout: default
title: EgoReasoner: Learning Egocentric 4D Reasoning via Task-Adaptive Structured Thinking
---

# EgoReasoner: Learning Egocentric 4D Reasoning via Task-Adaptive Structured Thinking
**arXiv**：[2603.06561v1](https://arxiv.org/abs/2603.06561) · [PDF](https://arxiv.org/pdf/2603.06561.pdf)  
**作者**：Fangrui Zhu, Yunfeng Xi, Jianmo Ni, Mu Cai, Boqing Gong, Long Zhao, Chen Qu, Ian Miao, Yi Li, Cheng Zhong, Huaizu Jiang, Shwetak Patel  

**一句话要点**：提出EgoReasoner框架，通过任务自适应结构化思维解决自我中心4D推理任务

**关键词**：自我中心视频理解, 4D推理, 任务自适应学习, 结构化思维链, 强化微调, 多任务基准

## 3 点简述
- 核心问题：自我中心视频理解因动态4D环境复杂，现有方法在空间锚定、时间跟踪和时长推理等不同认知任务上表现不足
- 方法要点：采用两阶段框架，第一阶段用任务自适应思维模板指导结构化思维链合成，第二阶段用任务感知奖励函数强化推理路径
- 实验或效果：在HD-EPIC基准上，3B参数模型仅用16K样本训练，平均准确率达37.5%，超越Qwen2.5-VL-7B模型

## 摘要（原文）

> Egocentric video understanding is inherently complex due to the dynamic 4D nature of the environment, where camera motion and object displacements necessitate a continuous re-evaluation of spatial relations. In this work, we target a suite of under-explored egocentric 4D reasoning tasks, including fixture interaction counting, viewpoint-relative fixture location, object movement itinerary tracking, and stationary object localization, that require fundamentally different cognitive operations: spatial anchoring, temporal tracking, and duration reasoning. We observe that these structural differences make task-agnostic approaches insufficient: generic Chain-of-Thought methods lack task-appropriate reasoning primitives, and uniform reinforcement learning actively destabilizes performance on spatial tasks. To address this, we propose EgoReasoner, a two-stage framework that aligns both the reasoning scaffold and the reward signal to each task's cognitive structure. In the first stage, Task-Adaptive Thinking Templates guide the synthesis of structured CoT traces that teach the model to reason adaptively across task types via supervised fine-tuning. In the second stage, task-aware reward functions verify entity grounding, temporal alignment, and task-adaptive logical consistency, selectively strengthening each reasoning pathway via reinforcement fine-tuning with GRPO. Our 3B-parameter model, trained on only 16K samples, achieves 37.5% average accuracy on the challenging HD-EPIC benchmark, surpassing Qwen2.5-VL-7B (25.7%) by over 10 points.

