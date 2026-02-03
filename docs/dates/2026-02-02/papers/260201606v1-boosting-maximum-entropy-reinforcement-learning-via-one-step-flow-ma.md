---
layout: default
title: Boosting Maximum Entropy Reinforcement Learning via One-Step Flow Matching
---

# Boosting Maximum Entropy Reinforcement Learning via One-Step Flow Matching
**arXiv**：[2602.01606v1](https://arxiv.org/abs/2602.01606) · [PDF](https://arxiv.org/pdf/2602.01606.pdf)  
**作者**：Zeqiao Li, Yijing Wang, Haoyu Wang, Zheng Li, Zhiqiang Zuo  

**一句话要点**：提出FLAME框架，通过一步流匹配提升最大熵强化学习，解决扩散策略延迟高和探索偏差问题。

**关键词**：最大熵强化学习, 流匹配, 一步生成, 探索偏差纠正, 推理效率优化

## 3 点简述
- 核心问题：扩散策略延迟高，流匹配集成到最大熵强化学习面临分布难解和探索偏差挑战。
- 方法要点：设计Q重加权流匹配目标绕过配分函数估计，并引入解耦熵估计器纠正偏差。
- 实验或效果：在MuJoCo上超越高斯基线，匹配多步扩散策略性能，显著降低推理成本。

## 摘要（原文）

> Diffusion policies are expressive yet incur high inference latency. Flow Matching (FM) enables one-step generation, but integrating it into Maximum Entropy Reinforcement Learning (MaxEnt RL) is challenging: the optimal policy is an intractable energy-based distribution, and the efficient log-likelihood estimation required to balance exploration and exploitation suffers from severe discretization bias. We propose \textbf{F}low-based \textbf{L}og-likelihood-\textbf{A}ware \textbf{M}aximum \textbf{E}ntropy RL (\textbf{FLAME}), a principled framework that addresses these challenges. First, we derive a Q-Reweighted FM objective that bypasses partition function estimation via importance reweighting. Second, we design a decoupled entropy estimator that rigorously corrects bias, which enables efficient exploration and brings the policy closer to the optimal MaxEnt policy. Third, we integrate the MeanFlow formulation to achieve expressive and efficient one-step control. Empirical results on MuJoCo show that FLAME outperforms Gaussian baselines and matches multi-step diffusion policies with significantly lower inference cost. Code is available at https://github.com/lzqw/FLAME.

