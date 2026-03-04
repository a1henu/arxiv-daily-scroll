---
layout: default
title: How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference
---

# How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference
**arXiv**：[2603.03280v1](https://arxiv.org/abs/2603.03280) · [PDF](https://arxiv.org/pdf/2603.03280.pdf)  
**作者**：Toru Lin, Shuying Deng, Zhao-Heng Yin, Pieter Abbeel, Jitendra Malik  

**一句话要点**：提出基于偏好微调的学习框架，以解决精细操作任务中隐式成功标准的对齐问题。

**关键词**：精细操作学习, 偏好微调, 模仿学习, 隐式奖励, 零样本泛化, 机器人操作

## 3 点简述
- 核心问题：精细操作任务如削皮具有连续主观的成功标准，难以量化评估和奖励设计。
- 方法要点：采用两阶段流程，先通过模仿学习获得初始策略，再基于偏好微调结合人类反馈优化策略。
- 实验或效果：仅需50-200条轨迹，在多种果蔬上实现超90%成功率，偏好微调提升性能达40%。

## 摘要（原文）

> Many essential manipulation tasks - such as food preparation, surgery, and craftsmanship - remain intractable for autonomous robots. These tasks are characterized not only by contact-rich, force-sensitive dynamics, but also by their "implicit" success criteria: unlike pick-and-place, task quality in these domains is continuous and subjective (e.g. how well a potato is peeled), making quantitative evaluation and reward engineering difficult. We present a learning framework for such tasks, using peeling with a knife as a representative example. Our approach follows a two-stage pipeline: first, we learn a robust initial policy via force-aware data collection and imitation learning, enabling generalization across object variations; second, we refine the policy through preference-based finetuning using a learned reward model that combines quantitative task metrics with qualitative human feedback, aligning policy behavior with human notions of task quality. Using only 50-200 peeling trajectories, our system achieves over 90% average success rates on challenging produce including cucumbers, apples, and potatoes, with performance improving by up to 40% through preference-based finetuning. Remarkably, policies trained on a single produce category exhibit strong zero-shot generalization to unseen in-category instances and to out-of-distribution produce from different categories while maintaining over 90% success rates.

