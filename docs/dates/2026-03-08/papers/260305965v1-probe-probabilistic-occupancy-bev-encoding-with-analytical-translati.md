---
layout: default
title: PROBE: Probabilistic Occupancy BEV Encoding with Analytical Translation Robustness for 3D Place Recognition
---

# PROBE: Probabilistic Occupancy BEV Encoding with Analytical Translation Robustness for 3D Place Recognition
**arXiv**：[2603.05965v1](https://arxiv.org/abs/2603.05965) · [PDF](https://arxiv.org/pdf/2603.05965.pdf)  
**作者**：Jinseop Lee, Byoungho Lee, Gichul Yoo  

**一句话要点**：提出PROBE，一种无学习的LiDAR地点识别描述符，通过概率建模和解析平移鲁棒性解决3D地点识别问题。

**关键词**：3D地点识别, LiDAR描述符, 概率建模, 平移鲁棒性, BEV编码, 无学习方法

## 3 点简述
- 核心问题：LiDAR地点识别中，传统方法依赖离散点云扰动，难以处理连续平移不确定性。
- 方法要点：将BEV单元占用建模为伯努利随机变量，通过极坐标雅可比解析边缘化连续平移，实现距离自适应角度不确定性。
- 实验或效果：在四种LiDAR数据集上评估，多会话评估中手工描述符精度最高，单会话性能与监督基线竞争。

## 摘要（原文）

> We present PROBE (PRobabilistic Occupancy BEV Encoding), a learning-free LiDAR place recognition descriptor that models each BEV cell's occupancy as a Bernoulli random variable. Rather than relying on discrete point-cloud perturbations, PROBE analytically marginalizes over continuous Cartesian translations via the polar Jacobian, yielding a distance-adaptive angular uncertainty $σ_θ= σ_t / r$ in $\mathcal{O}(R \times S)$ time. The primary parameter $σ_t$ represents the expected translational uncertainty in meters, a sensor-independent physical quantity allowing cross-sensor generalization without per-dataset tuning. Pairwise similarity combines a Bernoulli-KL Jaccard with exponential uncertainty gating and FFT-based height cosine similarity for rotation alignment. Evaluated on four datasets spanning four diverse LiDAR types, PROBE achieves the highest accuracy among handcrafted descriptors in multi-session evaluation and competitive single-session performance against both handcrafted and supervised baselines. The source code and supplementary materials are available at https://sites.google.com/view/probe-pr.

