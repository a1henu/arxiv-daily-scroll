---
layout: default
title: Flexible Entropy Control in RLVR with Gradient-Preserving Perspective
---

# Flexible Entropy Control in RLVR with Gradient-Preserving Perspective
**arXiv**：[2602.09782v1](https://arxiv.org/abs/2602.09782) · [PDF](https://arxiv.org/pdf/2602.09782.pdf)  
**作者**：Kun Chen, Peng Shi, Fanfan Liu, Haibo Qiu, Zhixiong Zeng, Siqi Yang, Wenji Mao  

**一句话要点**：提出基于梯度保持裁剪的动态熵控制方法，以缓解强化学习中的策略熵崩溃问题

**关键词**：强化学习, 策略熵控制, 梯度保持裁剪, 大语言模型, 动态阈值调节

## 3 点简述
- 核心问题：强化学习持续训练易导致策略熵崩溃，引发过早过自信、输出多样性降低和梯度消失
- 方法要点：从梯度保持裁剪视角重塑熵控制，通过动态裁剪阈值精确管理熵，设计多种动态控制策略
- 实验效果：在多个基准测试中有效缓解熵崩溃，实现更优性能

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a critical method for enhancing the reasoning capabilities of Large Language Models (LLMs). However, continuous training often leads to policy entropy collapse, characterized by a rapid decay in entropy that results in premature overconfidence, reduced output diversity, and vanishing gradient norms that inhibit learning. Gradient-Preserving Clipping is a primary factor influencing these dynamics, but existing mitigation strategies are largely static and lack a framework connecting clipping mechanisms to precise entropy control. This paper proposes reshaping entropy control in RL from the perspective of Gradient-Preserving Clipping. We first theoretically and empirically verify the contributions of specific importance sampling ratio regions to entropy growth and reduction. Leveraging these findings, we introduce a novel regulation mechanism using dynamic clipping threshold to precisely manage entropy. Furthermore, we design and evaluate dynamic entropy control strategies, including increase-then-decrease, decrease-increase-decrease, and oscillatory decay. Experimental results demonstrate that these strategies effectively mitigate entropy collapse, and achieve superior performance across multiple benchmarks.

