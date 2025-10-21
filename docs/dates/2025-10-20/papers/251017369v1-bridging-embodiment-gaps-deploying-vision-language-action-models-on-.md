---
layout: default
title: Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots
---

# Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots
**arXiv**：[2510.17369v1](https://arxiv.org/abs/2510.17369) · [PDF](https://arxiv.org/pdf/2510.17369.pdf)  
**作者**：Haochen Su, Cristian Meo, Francesco Stella, Andrea Peirone, Kai Junge, Josie Hughes  

**一句话要点**：部署视觉-语言-动作模型于软机器人，实现安全人机交互

**关键词**：视觉-语言-动作模型, 软机器人, 微调部署, 人机交互, 安全控制

## 3 点简述
- 核心问题：视觉-语言-动作模型部署于刚性机器人，缺乏安全交互能力。
- 方法要点：提出结构化微调流程，评估OpenVLA-OFT和π_0模型。
- 实验或效果：微调后软机器人性能与刚性机器人相当，支持安全交互。

## 摘要（原文）

> Robotic systems are increasingly expected to operate in human-centered,
> unstructured environments where safety, adaptability, and generalization are
> essential. Vision-Language-Action (VLA) models have been proposed as a language
> guided generalized control framework for real robots. However, their deployment
> has been limited to conventional serial link manipulators. Coupled by their
> rigidity and unpredictability of learning based control, the ability to safely
> interact with the environment is missing yet critical. In this work, we present
> the deployment of a VLA model on a soft continuum manipulator to demonstrate
> autonomous safe human-robot interaction. We present a structured finetuning and
> deployment pipeline evaluating two state-of-the-art VLA models (OpenVLA-OFT and
> $\pi_0$) across representative manipulation tasks, and show while
> out-of-the-box policies fail due to embodiment mismatch, through targeted
> finetuning the soft robot performs equally to the rigid counterpart. Our
> findings highlight the necessity of finetuning for bridging embodiment gaps,
> and demonstrate that coupling VLA models with soft robots enables safe and
> flexible embodied AI in human-shared environments.

