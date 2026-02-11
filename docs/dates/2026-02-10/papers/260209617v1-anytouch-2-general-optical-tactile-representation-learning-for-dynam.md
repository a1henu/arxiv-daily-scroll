---
layout: default
title: AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception
---

# AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception
**arXiv**：[2602.09617v1](https://arxiv.org/abs/2602.09617) · [PDF](https://arxiv.org/pdf/2602.09617.pdf)  
**作者**：Ruoxuan Feng, Yuxuan Zhou, Siyu Mei, Dongzhan Zhou, Pengwei Wang, Shaowei Cui, Bin Fang, Guocai Yao, Di Hu  

**一句话要点**：提出AnyTouch 2框架与ToucHD数据集，以增强光学触觉传感器的动态触觉感知能力

**关键词**：光学触觉传感器, 动态触觉感知, 触觉表示学习, 分层数据集, 力动态建模, 机器人操作

## 3 点简述
- 核心问题：现有触觉数据集和模型缺乏细粒度动态信息，难以支持接触丰富的机器人操作。
- 方法要点：构建大规模分层触觉数据集ToucHD，并设计统一框架AnyTouch 2，结合像素级变形和力动态建模。
- 实验或效果：在静态和动态基准测试及真实世界操作任务中，展现出跨传感器和任务的强性能。

## 摘要（原文）

> Real-world contact-rich manipulation demands robots to perceive temporal tactile feedback, capture subtle surface deformations, and reason about object properties as well as force dynamics. Although optical tactile sensors are uniquely capable of providing such rich information, existing tactile datasets and models remain limited. These resources primarily focus on object-level attributes (e.g., material) while largely overlooking fine-grained tactile temporal dynamics during physical interactions. We consider that advancing dynamic tactile perception requires a systematic hierarchy of dynamic perception capabilities to guide both data collection and model design. To address the lack of tactile data with rich dynamic information, we present ToucHD, a large-scale hierarchical tactile dataset spanning tactile atomic actions, real-world manipulations, and touch-force paired data. Beyond scale, ToucHD establishes a comprehensive tactile dynamic data ecosystem that explicitly supports hierarchical perception capabilities from the data perspective. Building on it, we propose AnyTouch 2, a general tactile representation learning framework for diverse optical tactile sensors that unifies object-level understanding with fine-grained, force-aware dynamic perception. The framework captures both pixel-level and action-specific deformations across frames, while explicitly modeling physical force dynamics, thereby learning multi-level dynamic perception capabilities from the model perspective. We evaluate our model on benchmarks that covers static object properties and dynamic physical attributes, as well as real-world manipulation tasks spanning multiple tiers of dynamic perception capabilities-from basic object-level understanding to force-aware dexterous manipulation. Experimental results demonstrate consistent and strong performance across sensors and tasks.

