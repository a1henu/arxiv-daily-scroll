---
layout: default
title: Robotic Scene Cloning:Advancing Zero-Shot Robotic Scene Adaptation in Manipulation via Visual Prompt Editing
---

# Robotic Scene Cloning:Advancing Zero-Shot Robotic Scene Adaptation in Manipulation via Visual Prompt Editing
**arXiv**：[2603.09712v1](https://arxiv.org/abs/2603.09712) · [PDF](https://arxiv.org/pdf/2603.09712.pdf)  
**作者**：Binyuan Huang, Yuqing Wen, Yucheng Zhao, Yaosi Hu, Tiancai Wang, Chang Wen Chen, Haoqiang Fan, Zhenzhong Chen  

**一句话要点**：提出Robotic Scene Cloning方法，通过视觉提示编辑实现零样本机器人场景适应

**关键词**：机器人场景适应, 零样本学习, 视觉提示编辑, 轨迹生成, 策略泛化

## 3 点简述
- 核心问题：预训练机器人模型在真实场景中零样本适应能力有限，需大量现场数据收集
- 方法要点：利用视觉提示机制和条件注入模块，编辑现有轨迹以生成场景一致的样本
- 实验或效果：在模拟和真实环境中显著提升策略泛化性能，适应多种对象类型

## 摘要（原文）

> Modern robots can perform a wide range of simple tasks and adapt to diverse scenarios in the well-trained environment. However, deploying pre-trained robot models in real-world user scenarios remains challenging due to their limited zero-shot capabilities, often necessitating extensive on-site data collection. To address this issue, we propose Robotic Scene Cloning (RSC), a novel method designed for scene-specific adaptation by editing existing robot operation trajectories. RSC achieves accurate and scene-consistent sample generation by leveraging a visual prompting mechanism and a carefully tuned condition injection module. Not only transferring textures but also performing moderate shape adaptations in response to the visual prompts, RSC demonstrates reliable task performance across a variety of object types. Experiments across various simulated and real-world environments demonstrate that RSC significantly enhances policy generalization in target environments.

