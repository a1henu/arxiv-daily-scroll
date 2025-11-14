---
layout: default
title: VISTA: A Vision and Intent-Aware Social Attention Framework for Multi-Agent Trajectory Prediction
---

# VISTA: A Vision and Intent-Aware Social Attention Framework for Multi-Agent Trajectory Prediction
**arXiv**：[2511.10203v1](https://arxiv.org/abs/2511.10203) · [PDF](https://arxiv.org/pdf/2511.10203.pdf)  
**作者**：Stephane Da Silva Martins, Emanuel Aldea, Sylvie Le Hégarat-Mascle  

**一句话要点**：提出VISTA框架以解决多智能体轨迹预测中目标与社交交互的联合建模问题

**关键词**：多智能体轨迹预测, 目标条件预测, 社交注意力机制, Transformer模型, 碰撞率评估, 可解释性分析

## 3 点简述
- 现有方法难以同时捕捉智能体长期目标和细粒度社交交互，导致预测不现实
- VISTA采用递归目标条件Transformer，融合意图、运动历史和社交注意力机制
- 在MADRAS和SDD基准上实现高精度和极低碰撞率，提升轨迹真实性和可解释性

## 摘要（原文）

> Multi-agent trajectory prediction is crucial for autonomous systems operating in dense, interactive environments. Existing methods often fail to jointly capture agents' long-term goals and their fine-grained social interactions, which leads to unrealistic multi-agent futures. We propose VISTA, a recursive goal-conditioned transformer for multi-agent trajectory forecasting. VISTA combines (i) a cross-attention fusion module that integrates long-horizon intent with past motion, (ii) a social-token attention mechanism for flexible interaction modeling across agents, and (iii) pairwise attention maps that make social influence patterns interpretable at inference time. Our model turns single-agent goal-conditioned prediction into a coherent multi-agent forecasting framework. Beyond standard displacement metrics, we evaluate trajectory collision rates as a measure of joint realism. On the high-density MADRAS benchmark and on SDD, VISTA achieves state-of-the-art accuracy and substantially fewer collisions. On MADRAS, it reduces the average collision rate of strong baselines from 2.14 to 0.03 percent, and on SDD it attains zero collisions while improving ADE, FDE, and minFDE. These results show that VISTA generates socially compliant, goal-aware, and interpretable trajectories, making it promising for safety-critical autonomous systems.

