---
layout: default
title: A Micro-Macro Model of Encounter-Driven Information Diffusion in Robot Swarms
---

# A Micro-Macro Model of Encounter-Driven Information Diffusion in Robot Swarms
**arXiv**：[2602.21148v1](https://arxiv.org/abs/2602.21148) · [PDF](https://arxiv.org/pdf/2602.21148.pdf)  
**作者**：Davis S. Catherman, Carlo Pinciroli  

**一句话要点**：提出微宏观模型以解决机器人群体中仅靠相遇驱动的信息扩散问题

**关键词**：机器人群体, 信息扩散, 微宏观模型, 相遇驱动, 平均自由程, 模拟验证

## 3 点简述
- 核心问题：机器人仅能在相遇时交换信息，且无法预知相遇时间、地点和对象
- 方法要点：基于‘平均自由程’概念构建微观模型，结合宏观模型捕捉全局扩散动态
- 实验或效果：通过机器人模拟验证模型，考虑群体规模、通信范围、环境大小和运动模式

## 摘要（原文）

> In this paper, we propose the problem of Encounter-Driven Information Diffusion (EDID). In EDID, robots are allowed to exchange information only upon meeting. Crucially, EDID assumes that the robots are not allowed to schedule their meetings. As such, the robots have no means to anticipate when, where, and who they will meet. As a step towards the design of storage and routing algorithms for EDID, in this paper we propose a model of information diffusion that captures the essential dynamics of EDID. The model is derived from first principles and is composed of two levels: a micro model, based on a generalization of the concept of `mean free path'; and a macro model, which captures the global dynamics of information diffusion. We validate the model through extensive robot simulations, in which we consider swarm size, communication range, environment size, and different random motion regimes. We conclude the paper with a discussion of the implications of this model on the algorithms that best support information diffusion according to the parameters of interest.

