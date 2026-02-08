---
layout: default
title: Optimal scaling laws in learning hierarchical multi-index models
---

# Optimal scaling laws in learning hierarchical multi-index models
**arXiv**：[2602.05846v1](https://arxiv.org/abs/2602.05846) · [PDF](https://arxiv.org/pdf/2602.05846.pdf)  
**作者**：Leonardo Defilippis, Florent Krzakala, Bruno Loureiro, Antoine Maillard  

**一句话要点**：提出两层神经网络在分层多索引目标上的最优缩放定律理论

**关键词**：神经网络缩放定律, 分层多索引模型, 信息论分析, 谱估计器, 相变学习, 表示学习

## 3 点简述
- 研究两层神经网络在表示受限机制下学习分层多索引目标的缩放定律
- 推导子空间恢复和预测误差的精确信息论缩放定律，揭示目标分层特征通过相变级联顺序学习
- 证明简单目标无关谱估计器可实现最优速率，并解释为梯度下降小学习率极限

## 摘要（原文）

> In this work, we provide a sharp theory of scaling laws for two-layer neural networks trained on a class of hierarchical multi-index targets, in a genuinely representation-limited regime. We derive exact information-theoretic scaling laws for subspace recovery and prediction error, revealing how the hierarchical features of the target are sequentially learned through a cascade of phase transitions. We further show that these optimal rates are achieved by a simple, target-agnostic spectral estimator, which can be interpreted as the small learning-rate limit of gradient descent on the first-layer weights. Once an adapted representation is identified, the readout can be learned statistically optimally, using an efficient procedure. As a consequence, we provide a unified and rigorous explanation of scaling laws, plateau phenomena, and spectral structure in shallow neural networks trained on such hierarchical targets.

