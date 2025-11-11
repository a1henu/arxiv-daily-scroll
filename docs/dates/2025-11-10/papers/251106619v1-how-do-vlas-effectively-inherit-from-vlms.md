---
layout: default
title: How Do VLAs Effectively Inherit from VLMs?
---

# How Do VLAs Effectively Inherit from VLMs?
**arXiv**：[2511.06619v1](https://arxiv.org/abs/2511.06619) · [PDF](https://arxiv.org/pdf/2511.06619.pdf)  
**作者**：Chuheng Zhang, Rushuai Yang, Xiaoyu Chen, Kaixin Wang, Li Zhao, Yi Chen, Jiang Bian  

**一句话要点**：提出GrinningFace基准以评估VLA如何有效继承VLM先验知识

**关键词**：视觉语言动作模型, 先验知识继承, 具身控制, 诊断基准, 参数高效微调

## 3 点简述
- 核心问题：VLA模型如何有效继承VLM的视觉语义先验知识以实现具身控制。
- 方法要点：设计表情符号桌面操作任务，比较参数高效微调、VLM冻结等技术。
- 实验或效果：在模拟和真实机器人中验证，强调保留VLM先验对泛化的重要性。

## 摘要（原文）

> Vision-language-action (VLA) models hold the promise to attain generalizable
> embodied control. To achieve this, a pervasive paradigm is to leverage the rich
> vision-semantic priors of large vision-language models (VLMs). However, the
> fundamental question persists: How do VLAs effectively inherit the prior
> knowledge from VLMs? To address this critical question, we introduce a
> diagnostic benchmark, GrinningFace, an emoji tabletop manipulation task where
> the robot arm is asked to place objects onto printed emojis corresponding to
> language instructions. This task design is particularly revealing -- knowledge
> associated with emojis is ubiquitous in Internet-scale datasets used for VLM
> pre-training, yet emojis themselves are largely absent from standard robotics
> datasets. Consequently, they provide a clean proxy: successful task completion
> indicates effective transfer of VLM priors to embodied control. We implement
> this diagnostic task in both simulated environment and a real robot, and
> compare various promising techniques for knowledge transfer. Specifically, we
> investigate the effects of parameter-efficient fine-tuning, VLM freezing,
> co-training, predicting discretized actions, and predicting latent actions.
> Through systematic evaluation, our work not only demonstrates the critical
> importance of preserving VLM priors for the generalization of VLA but also
> establishes guidelines for future research in developing truly generalizable
> embodied AI systems.

