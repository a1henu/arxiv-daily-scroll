---
layout: default
title: Towards Adaptive Environment Generation for Training Embodied Agents
---

# Towards Adaptive Environment Generation for Training Embodied Agents
**arXiv**：[2602.06366v1](https://arxiv.org/abs/2602.06366) · [PDF](https://arxiv.org/pdf/2602.06366.pdf)  
**作者**：Teresa Yeo, Dulaj Weerakoon, Dulanga Weerakoon, Archan Misra  

**一句话要点**：提出闭环环境生成方法，根据具身智能体性能自适应调整训练难度

**关键词**：具身智能体, 环境生成, 自适应训练, 闭环控制, 泛化能力

## 3 点简述
- 核心问题：具身智能体在结构相似新环境中泛化能力差，现有开环生成方法效率低
- 方法要点：基于可控环境表示和细粒度性能反馈，实现闭环难度自适应机制
- 实验或效果：概念验证表明，该方法能生成更具挑战性的训练环境，提升学习效率和泛化能力

## 摘要（原文）

> Embodied agents struggle to generalize to new environments, even when those environments share similar underlying structures to their training settings. Most current approaches to generating these training environments follow an open-loop paradigm, without considering the agent's current performance. While procedural generation methods can produce diverse scenes, diversity without feedback from the agent is inefficient. The generated environments may be trivially easy, providing limited learning signal. To address this, we present a proof-of-concept for closed-loop environment generation that adapts difficulty to the agent's current capabilities. Our system employs a controllable environment representation, extracts fine-grained performance feedback beyond binary success or failure, and implements a closed-loop adaptation mechanism that translates this feedback into environment modifications. This feedback-driven approach generates training environments that more challenging in the ways the agent needs to improve, enabling more efficient learning and better generalization to novel settings.

