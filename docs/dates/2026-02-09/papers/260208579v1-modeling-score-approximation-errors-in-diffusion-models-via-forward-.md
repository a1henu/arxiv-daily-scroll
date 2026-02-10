---
layout: default
title: Modeling Score Approximation Errors in Diffusion Models via Forward SPDEs
---

# Modeling Score Approximation Errors in Diffusion Models via Forward SPDEs
**arXiv**：[2602.08579v1](https://arxiv.org/abs/2602.08579) · [PDF](https://arxiv.org/pdf/2602.08579.pdf)  
**作者**：Junsu Seo  

**一句话要点**：提出基于前向SPDE框架建模扩散模型分数近似误差，以分析生成模型动态与鲁棒性。

**关键词**：扩散模型, 分数近似误差, 前向SPDE, 概率密度演化, 生成模型鲁棒性, 评估指标

## 3 点简述
- 核心问题：研究扩散模型中分数估计误差对概率密度演化的影响，而非传统粒子SDE分析。
- 方法要点：采用SPDE框架将误差视为随机源驱动Fokker-Planck方程，结合几何稳定性和位移凸性解释鲁棒性。
- 实验或效果：提出基于SPDE解二次变分的候选评估指标，初步观察显示仅需采样轨迹前10%即可有效评估。

## 摘要（原文）

> This study investigates the dynamics of Score-based Generative Models (SGMs) by treating the score estimation error as a stochastic source driving the Fokker-Planck equation. Departing from particle-centric SDE analyses, we employ an SPDE framework to model the evolution of the probability density field under stochastic drift perturbations. Under a simplified setting, we utilize this framework to interpret the robustness of generative models through the lens of geometric stability and displacement convexity. Furthermore, we introduce a candidate evaluation metric derived from the quadratic variation of the SPDE solution projected onto a radial test function. Preliminary observations suggest that this metric remains effective using only the initial 10% of the sampling trajectory, indicating a potential for computational efficiency.

