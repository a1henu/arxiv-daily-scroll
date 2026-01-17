---
layout: default
title: EditEmoTalk: Controllable Speech-Driven 3D Facial Animation with Continuous Expression Editing
---

# EditEmoTalk: Controllable Speech-Driven 3D Facial Animation with Continuous Expression Editing
**arXiv**：[2601.10000v1](https://arxiv.org/abs/2601.10000) · [PDF](https://arxiv.org/pdf/2601.10000.pdf)  
**作者**：Diqiong Jiang, Kai Zhu, Dan Song, Jian Chang, Chenglizhao Chen, Zhenyu Wu  

**一句话要点**：提出EditEmoTalk框架，通过连续情感编辑实现可控的语音驱动3D面部动画

**关键词**：语音驱动3D面部动画, 连续情感编辑, 边界感知语义嵌入, 情感一致性损失, 表情流形, 唇同步

## 3 点简述
- 核心问题：现有方法依赖离散情感类别，限制了连续和细粒度的情感控制。
- 方法要点：采用边界感知语义嵌入学习情感决策边界的法向，构建连续表情流形，并引入情感一致性损失确保语义对齐。
- 实验或效果：实验显示EditEmoTalk在保持准确唇同步的同时，实现了优越的可控性、表达性和泛化能力。

## 摘要（原文）

> Speech-driven 3D facial animation aims to generate realistic and expressive facial motions directly from audio. While recent methods achieve high-quality lip synchronization, they often rely on discrete emotion categories, limiting continuous and fine-grained emotional control. We present EditEmoTalk, a controllable speech-driven 3D facial animation framework with continuous emotion editing. The key idea is a boundary-aware semantic embedding that learns the normal directions of inter-emotion decision boundaries, enabling a continuous expression manifold for smooth emotion manipulation. Moreover, we introduce an emotional consistency loss that enforces semantic alignment between the generated motion dynamics and the target emotion embedding through a mapping network, ensuring faithful emotional expression. Extensive experiments demonstrate that EditEmoTalk achieves superior controllability, expressiveness, and generalization while maintaining accurate lip synchronization. Code and pretrained models will be released.

