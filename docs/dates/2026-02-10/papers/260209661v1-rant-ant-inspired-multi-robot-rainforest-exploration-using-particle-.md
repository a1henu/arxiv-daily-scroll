---
layout: default
title: RANT: Ant-Inspired Multi-Robot Rainforest Exploration Using Particle Filter Localisation and Virtual Pheromone Coordination
---

# RANT: Ant-Inspired Multi-Robot Rainforest Exploration Using Particle Filter Localisation and Virtual Pheromone Coordination
**arXiv**：[2602.09661v1](https://arxiv.org/abs/2602.09661) · [PDF](https://arxiv.org/pdf/2602.09661.pdf)  
**作者**：Ameer Alhashemi, Layan Abdulhadi, Karam Abuodeh, Tala Baghdadi, Suryanarayana Datla  

**一句话要点**：提出RANT框架，结合粒子滤波定位与虚拟信息素协调，用于多机器人雨林探索。

**关键词**：多机器人探索, 粒子滤波定位, 虚拟信息素协调, 行为控制, 热点检测, 环境噪声

## 3 点简述
- 核心问题：在噪声不确定环境中，多机器人如何高效探索并定位热点区域。
- 方法要点：采用粒子滤波定位、基于行为的梯度驱动热点利用和轻量级虚拟信息素协调机制。
- 实验或效果：团队规模、定位精度和协调机制影响覆盖率、热点召回和冗余，协调显著减少重叠。

## 摘要（原文）

> This paper presents RANT, an ant-inspired multi-robot exploration framework for noisy, uncertain environments. A team of differential-drive robots navigates a 10 x 10 m terrain, collects noisy probe measurements of a hidden richness field, and builds local probabilistic maps while the supervisor maintains a global evaluation. RANT combines particle-filter localisation, a behaviour-based controller with gradient-driven hotspot exploitation, and a lightweight no-revisit coordination mechanism based on virtual pheromone blocking. We experimentally analyse how team size, localisation fidelity, and coordination influence coverage, hotspot recall, and redundancy. Results show that particle filtering is essential for reliable hotspot engagement, coordination substantially reduces overlap, and increasing team size improves coverage but yields diminishing returns due to interference.

