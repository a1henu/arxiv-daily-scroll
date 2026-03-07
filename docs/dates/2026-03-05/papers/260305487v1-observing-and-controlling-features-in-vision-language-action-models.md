---
layout: default
title: Observing and Controlling Features in Vision-Language-Action Models
---

# Observing and Controlling Features in Vision-Language-Action Models
**arXiv**：[2603.05487v1](https://arxiv.org/abs/2603.05487) · [PDF](https://arxiv.org/pdf/2603.05487.pdf)  
**作者**：Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone  

**一句话要点**：提出特征可观测性与可控性方法，以在线调控视觉-语言-动作模型的行为。

**关键词**：视觉-语言-动作模型, 特征可观测性, 特征可控性, 线性干预, 机器人控制, 在线适应

## 3 点简述
- 核心问题：视觉-语言-动作模型内部机制复杂，现有大语言模型可解释性方法难以直接应用。
- 方法要点：通过线性分类器观测特征，并基于最优控制进行线性干预以精确调控模型输出。
- 实验或效果：在模拟实验中验证了轻量级干预能可靠引导机器人行为，保持闭环能力，无需微调。

## 摘要（原文）

> Vision-Language-Action Models (VLAs) have shown remarkable progress towards embodied intelligence. While their architecture partially resembles that of Large Language Models (LLMs), VLAs exhibit higher complexity due to their multi-modal inputs/outputs and often hybrid nature of transformer and diffusion heads. This is part of the reason why insights from mechanistic interpretability in LLMs, which explain how the internal model representations relate to their output behavior, do not trivially transfer to VLA counterparts. In this work, we propose to close this gap by introducing and analyzing two main concepts: feature-observability and feature-controllability. In particular, we first study features that are linearly encoded in representation space, and show how they can be observed by means of a linear classifier. Then, we use a minimal linear intervention grounded in optimal control to accurately place internal representations and steer the VLA's output towards a desired region. Our results show that targeted, lightweight interventions can reliably steer a robot's behavior while preserving closed-loop capabilities. We demonstrate on different VLA architectures ($π_{0.5}$ and OpenVLA) through simulation experiments that VLAs possess interpretable internal structure amenable to online adaptation without fine-tuning, enabling real-time alignment with user preferences and task requirements.

