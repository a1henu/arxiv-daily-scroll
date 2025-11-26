---
layout: default
title: Reinforcing Action Policies by Prophesying
---

# Reinforcing Action Policies by Prophesying
**arXiv**：[2511.20633v1](https://arxiv.org/abs/2511.20633) · [PDF](https://arxiv.org/pdf/2511.20633.pdf)  
**作者**：Jiahui Zhang, Ze Huang, Chun Gu, Zipei Ma, Li Zhang  

**一句话要点**：提出ProphRL方法，通过世界模型和强化学习增强视觉-语言-动作策略的鲁棒性。

**关键词**：视觉-语言-动作策略, 强化学习, 世界模型, 机器人控制, 策略优化

## 3 点简述
- 核心问题：视觉-语言-动作策略模仿训练易过拟合，强化学习在真实机器人上成本高。
- 方法要点：使用Prophet世界模型预测动作结果，结合FA-GRPO和FlowScale优化策略。
- 实验效果：在基准测试和真实机器人上分别提升5-17%和24-30%成功率。

## 摘要（原文）

> Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

