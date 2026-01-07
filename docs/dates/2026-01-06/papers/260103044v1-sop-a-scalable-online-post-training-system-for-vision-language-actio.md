---
layout: default
title: SOP: A Scalable Online Post-Training System for Vision-Language-Action Models
---

# SOP: A Scalable Online Post-Training System for Vision-Language-Action Models
**arXiv**：[2601.03044v1](https://arxiv.org/abs/2601.03044) · [PDF](https://arxiv.org/pdf/2601.03044.pdf)  
**作者**：Mingjie Pan, Siyuan Feng, Qinglin Zhang, Xinchen Li, Jianheng Song, Chendi Qu, Yi Wang, Chuankang Li, Ziyu Xiong, Zhi Chen, Yi Liu, Jianlan Luo  

**一句话要点**：提出SOP系统以实现在线、分布式、多任务的后训练，提升视觉-语言-动作模型在物理世界中的任务熟练度。

**关键词**：视觉-语言-动作模型, 在线后训练, 分布式学习, 机器人舰队, 闭环架构, 多任务适应

## 3 点简述
- 现有VLA模型后训练方法多为离线、单机器人或任务特定，限制了在线策略适应和可扩展学习。
- SOP采用闭环架构，机器人舰队流式传输在线策略经验和人类干预信号至云端学习器，异步接收更新策略。
- 在布料折叠、箱子组装和杂货补货等真实世界操作任务中，SOP显著提升预训练VLA模型性能，保持跨任务共享策略，性能随机器人数量近线性扩展。

## 摘要（原文）

> Vision-language-action (VLA) models achieve strong generalization through large-scale pre-training, but real-world deployment requires expert-level task proficiency in addition to broad generality. Existing post-training approaches for VLA models are typically offline, single-robot, or task-specific, limiting effective on-policy adaptation and scalable learning from real-world interaction. We introduce a Scalable Online Post-training (SOP) system that enables online, distributed, multi-task post-training of generalist VLA models directly in the physical world. SOP tightly couples execution and learning through a closed-loop architecture in which a fleet of robots continuously streams on-policy experience and human intervention signals to a centralized cloud learner, and asynchronously receives updated policies. This design supports prompt on-policy correction, scales experience collection through parallel deployment, and preserves generality during adaptation. SOP is agnostic to the choice of post-training algorithm; we instantiate it with both interactive imitation learning (HG-DAgger) and reinforcement learning (RECAP). Across a range of real-world manipulation tasks including cloth folding, box assembly, and grocery restocking, we show that SOP substantially improves the performance of large pretrained VLA models while maintaining a single shared policy across tasks. Effective post-training can be achieved within hours of real-world interaction, and performance scales near-linearly with the number of robots in the fleet. These results suggest that tightly coupling online learning with fleet-scale deployment is instrumental to enabling efficient, reliable, and scalable post-training of generalist robot policies in the physical world.

