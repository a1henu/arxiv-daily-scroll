---
layout: default
title: Flexible Multitask Learning with Factorized Diffusion Policy
---

# Flexible Multitask Learning with Factorized Diffusion Policy
**arXiv**：[2512.21898v1](https://arxiv.org/abs/2512.21898) · [PDF](https://arxiv.org/pdf/2512.21898.pdf)  
**作者**：Chaoqi Liu, Haonan Chen, Sigmund H. Høeg, Shaoxiong Yao, Yunzhu Li, Kris Hauser, Yilun Du  

**一句话要点**：提出因子化扩散策略框架，通过模块化分解解决机器人多任务学习中的动作分布拟合难题

**关键词**：多任务学习, 扩散策略, 模块化策略, 机器人操作, 动作分布分解, 策略适应

## 3 点简述
- 核心问题：机器人多任务学习中动作分布高度多模态且多样，现有单一模型难以有效拟合且缺乏适应灵活性
- 方法要点：将复杂动作分布分解为多个专用扩散模型的组合，每个模型捕获行为空间的不同子模式
- 实验效果：在仿真和真实机器人操作场景中，该方法持续优于模块化和单一基线模型

## 摘要（原文）

> Multitask learning poses significant challenges due to the highly multimodal and diverse nature of robot action distributions. However, effectively fitting policies to these complex task distributions is often difficult, and existing monolithic models often underfit the action distribution and lack the flexibility required for efficient adaptation. We introduce a novel modular diffusion policy framework that factorizes complex action distributions into a composition of specialized diffusion models, each capturing a distinct sub-mode of the behavior space for a more effective overall policy. In addition, this modular structure enables flexible policy adaptation to new tasks by adding or fine-tuning components, which inherently mitigates catastrophic forgetting. Empirically, across both simulation and real-world robotic manipulation settings, we illustrate how our method consistently outperforms strong modular and monolithic baselines.

