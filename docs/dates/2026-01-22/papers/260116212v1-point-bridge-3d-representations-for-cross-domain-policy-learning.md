---
layout: default
title: Point Bridge: 3D Representations for Cross Domain Policy Learning
---

# Point Bridge: 3D Representations for Cross Domain Policy Learning
**arXiv**：[2601.16212v1](https://arxiv.org/abs/2601.16212) · [PDF](https://arxiv.org/pdf/2601.16212.pdf)  
**作者**：Siddhant Haldar, Lars Johannsmeier, Lerrel Pinto, Abhishek Gupta, Dieter Fox, Yashraj Narang, Ajay Mandlekar  

**一句话要点**：提出Point Bridge框架，利用点云表示实现零样本仿真到现实的策略迁移

**关键词**：点云表示, 仿真到现实迁移, 机器人策略学习, 视觉语言模型, 零样本学习

## 3 点简述
- 核心问题：仿真与现实的视觉域差距限制了机器人基础模型利用合成数据的有效性
- 方法要点：结合视觉语言模型自动提取点云表示、基于Transformer的策略学习和高效推理管道
- 实验或效果：在零样本仿真到现实迁移中提升达44%，结合少量真实演示后提升达66%

## 摘要（原文）

> Robot foundation models are beginning to deliver on the promise of generalist robotic agents, yet progress remains constrained by the scarcity of large-scale real-world manipulation datasets. Simulation and synthetic data generation offer a scalable alternative, but their usefulness is limited by the visual domain gap between simulation and reality. In this work, we present Point Bridge, a framework that leverages unified, domain-agnostic point-based representations to unlock synthetic datasets for zero-shot sim-to-real policy transfer, without explicit visual or object-level alignment. Point Bridge combines automated point-based representation extraction via Vision-Language Models (VLMs), transformer-based policy learning, and efficient inference-time pipelines to train capable real-world manipulation agents using only synthetic data. With additional co-training on small sets of real demonstrations, Point Bridge further improves performance, substantially outperforming prior vision-based sim-and-real co-training methods. It achieves up to 44% gains in zero-shot sim-to-real transfer and up to 66% with limited real data across both single-task and multitask settings. Videos of the robot are best viewed at: https://pointbridge3d.github.io/

