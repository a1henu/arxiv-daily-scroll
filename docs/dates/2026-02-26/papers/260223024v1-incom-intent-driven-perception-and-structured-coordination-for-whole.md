---
layout: default
title: InCoM: Intent-Driven Perception and Structured Coordination for Whole-Body Mobile Manipulation
---

# InCoM: Intent-Driven Perception and Structured Coordination for Whole-Body Mobile Manipulation
**arXiv**：[2602.23024v1](https://arxiv.org/abs/2602.23024) · [PDF](https://arxiv.org/pdf/2602.23024.pdf)  
**作者**：Jiahao Liu, Cui Wenbo, Haoran Li, Dongbin Zhao  

**一句话要点**：提出InCoM框架，通过意图驱动感知与结构化协调解决全身移动操作问题

**关键词**：全身移动操作, 意图驱动感知, 结构化协调, 多尺度特征, 流匹配解码, 机器人控制

## 3 点简述
- 核心问题：全身移动操作中，基座与机械臂动作强耦合导致控制优化困难，且视角动态变化下感知注意力分配不佳
- 方法要点：InCoM推断潜在运动意图以动态重加权多尺度感知特征，并设计解耦协调流匹配动作解码器
- 实验或效果：在ManiSkill-HAB场景中，InCoM在成功率上优于现有方法，提升幅度达23.6%至28.2%

## 摘要（原文）

> Whole-body mobile manipulation is a fundamental capability for general-purpose robotic agents, requiring both coordinated control of the mobile base and manipulator and robust perception under dynamically changing viewpoints. However, existing approaches face two key challenges: strong coupling between base and arm actions complicates whole-body control optimization, and perceptual attention is often poorly allocated as viewpoints shift during mobile manipulation. We propose InCoM, an intent-driven perception and structured coordination framework for whole-body mobile manipulation. InCoM infers latent motion intent to dynamically reweight multi-scale perceptual features, enabling stage-adaptive allocation of perceptual attention. To support robust cross-modal perception, InCoM further incorporates a geometric-semantic structured alignment mechanism that enhances multimodal correspondence. On the control side, we design a decoupled coordinated flow matching action decoder that explicitly models coordinated base-arm action generation, alleviating optimization difficulties caused by control coupling. Without access to privileged perceptual information, InCoM outperforms state-of-the-art methods on three ManiSkill-HAB scenarios by 28.2%, 26.1%, and 23.6% in success rate, demonstrating strong effectiveness for whole-body mobile manipulation.

