---
layout: default
title: GRIP: A Unified Framework for Grid-Based Relay and Co-Occurrence-Aware Planning in Dynamic Environments
---

# GRIP: A Unified Framework for Grid-Based Relay and Co-Occurrence-Aware Planning in Dynamic Environments
**arXiv**：[2510.10865v1](https://arxiv.org/abs/2510.10865) · [PDF](https://arxiv.org/pdf/2510.10865.pdf)  
**作者**：Ahmed Alanazi, Duy Ho, Yugyung Lee  

**一句话要点**：提出GRIP框架以解决动态环境中机器人导航的适应性问题

**关键词**：机器人导航, 动态环境规划, 语义网格, 符号推理, 混合策略执行, 现实世界部署

## 3 点简述
- 核心问题：动态、杂乱环境中机器人导航受限于静态先验和部分可观测性
- 方法要点：集成动态网格构建、共现感知符号规划和混合策略执行
- 实验或效果：在AI2-THOR和RoboTHOR上提升成功率9.6%和路径效率2倍以上

## 摘要（原文）

> Robots navigating dynamic, cluttered, and semantically complex environments
> must integrate perception, symbolic reasoning, and spatial planning to
> generalize across diverse layouts and object categories. Existing methods often
> rely on static priors or limited memory, constraining adaptability under
> partial observability and semantic ambiguity. We present GRIP, Grid-based Relay
> with Intermediate Planning, a unified, modular framework with three scalable
> variants: GRIP-L (Lightweight), optimized for symbolic navigation via semantic
> occupancy grids; GRIP-F (Full), supporting multi-hop anchor chaining and
> LLM-based introspection; and GRIP-R (Real-World), enabling physical robot
> deployment under perceptual uncertainty. GRIP integrates dynamic 2D grid
> construction, open-vocabulary object grounding, co-occurrence-aware symbolic
> planning, and hybrid policy execution using behavioral cloning, D* search, and
> grid-conditioned control. Empirical results on AI2-THOR and RoboTHOR benchmarks
> show that GRIP achieves up to 9.6% higher success rates and over $2\times$
> improvement in path efficiency (SPL and SAE) on long-horizon tasks. Qualitative
> analyses reveal interpretable symbolic plans in ambiguous scenes. Real-world
> deployment on a Jetbot further validates GRIP's generalization under sensor
> noise and environmental variation. These results position GRIP as a robust,
> scalable, and explainable framework bridging simulation and real-world
> navigation.

