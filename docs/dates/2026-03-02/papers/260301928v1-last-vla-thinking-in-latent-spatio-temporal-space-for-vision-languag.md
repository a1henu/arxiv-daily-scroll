---
layout: default
title: LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving
---

# LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving
**arXiv**：[2603.01928v1](https://arxiv.org/abs/2603.01928) · [PDF](https://arxiv.org/pdf/2603.01928.pdf)  
**作者**：Yuechen Luo, Fang Li, Shaoqing Xu, Yang Ji, Zehan Zhang, Bing Wang, Yuannan Shen, Jianwei Cui, Long Chen, Guang Chen, Hangjun Ye, Zhi-Xin Yang, Fuxi Wen  

**一句话要点**：提出LaST-VLA框架，通过潜在时空推理解决自动驾驶中视觉-语言-动作模型的语义感知解耦问题。

**关键词**：自动驾驶, 视觉-语言-动作模型, 潜在推理, 时空推理, 特征对齐, 强化学习

## 3 点简述
- 核心问题：现有VLA模型依赖显式文本链式思考，导致语义感知解耦和感知符号冲突。
- 方法要点：引入潜在时空链式思考，通过双特征对齐机制从3D基础模型和世界模型蒸馏几何约束与动态预见。
- 实验或效果：在NAVSIM v1和v2基准上创纪录，并在SURDS和NuDynamics上表现出色。

## 摘要（原文）

> While Vision-Language-Action (VLA) models have revolutionized autonomous driving by unifying perception and planning, their reliance on explicit textual Chain-of-Thought (CoT) leads to semantic-perceptual decoupling and perceptual-symbolic conflicts. Recent shifts toward latent reasoning attempt to bypass these bottlenecks by thinking in continuous hidden space. However, without explicit intermediate constraints, standard latent CoT often operates as a physics-agnostic representation. To address this, we propose the Latent Spatio-Temporal VLA (LaST-VLA), a framework shifting the reasoning paradigm from discrete symbolic processing into a physically grounded Latent Spatio-Temporal CoT. By implementing a dual-feature alignment mechanism, we distill geometric constraints from 3D foundation models and dynamic foresight from world models directly into the latent space. Coupled with a progressive SFT training strategy that transitions from feature alignment to trajectory generation, and refined via Reinforcement Learning with Group Relative Policy Optimization (GRPO) to ensure safety and rule compliance. \method~setting a new record on NAVSIM v1 (91.3 PDMS) and NAVSIM v2 (87.1 EPDMS), while excelling in spatial-temporal reasoning on SURDS and NuDynamics benchmarks.

