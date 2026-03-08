---
layout: default
title: LEGS-POMDP: Language and Gesture-Guided Object Search in Partially Observable Environments
---

# LEGS-POMDP: Language and Gesture-Guided Object Search in Partially Observable Environments
**arXiv**：[2603.04705v1](https://arxiv.org/abs/2603.04705) · [PDF](https://arxiv.org/pdf/2603.04705.pdf)  
**作者**：Ivy Xiao He, Stefanie Tellex, Jason Xinyu Liu  

**一句话要点**：提出LEGS-POMDP系统，通过语言和手势引导在部分可观测环境中搜索目标物体

**关键词**：部分可观测马尔可夫决策过程, 多模态融合, 物体搜索, 机器人感知, 不确定性建模, 开放世界导航

## 3 点简述
- 核心问题：机器人需在开放世界中根据模糊指令定位物体，现有方法难以系统处理长期任务中的不确定性
- 方法要点：构建模块化POMDP框架，融合语言、手势和视觉观测，显式建模目标物体身份和位置的不确定性
- 实验效果：仿真中多模态融合平均成功率89%，四足移动机械臂实验验证了鲁棒感知和不确定性降低能力

## 摘要（原文）

> To assist humans in open-world environments, robots must interpret ambiguous instructions to locate desired objects. Foundation model-based approaches excel at multimodal grounding, but they lack a principled mechanism for modeling uncertainty in long-horizon tasks. In contrast, Partially Observable Markov Decision Processes (POMDPs) provide a systematic framework for planning under uncertainty but are often limited in supported modalities and rely on restrictive environment assumptions. We introduce LanguagE and Gesture-Guided Object Search in Partially Observable Environments (LEGS-POMDP), a modular POMDP system that integrates language, gesture, and visual observations for open-world object search. Unlike prior work, LEGS-POMDP explicitly models two sources of partial observability: uncertainty over the target object's identity and its spatial location. In simulation, multimodal fusion significantly outperforms unimodal baselines, achieving an average success rate of 89\% across challenging environments and object categories. Finally, we demonstrate the full system on a quadruped mobile manipulator, where real-world experiments qualitatively validate robust multimodal perception and uncertainty reduction under ambiguous instructions.

