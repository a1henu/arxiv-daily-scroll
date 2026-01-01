---
layout: default
title: Mobility-Assisted Decentralized Federated Learning: Convergence Analysis and A Data-Driven Approach
---

# Mobility-Assisted Decentralized Federated Learning: Convergence Analysis and A Data-Driven Approach
**arXiv**：[2512.24694v1](https://arxiv.org/abs/2512.24694) · [PDF](https://arxiv.org/pdf/2512.24694.pdf)  
**作者**：Reza Jahani, Md Farhamdur Reza, Richeng Jin, Huaiyu Dai  

**一句话要点**：提出利用用户移动性增强稀疏网络中分散联邦学习的收敛性与数据驱动轨迹优化方法

**关键词**：分散联邦学习, 移动性增强, 收敛分析, 数据驱动优化, 稀疏网络, 隐私保护机器学习

## 3 点简述
- 核心问题：分散联邦学习在稀疏网络和数据异构下性能下降，用户移动性影响被忽视
- 方法要点：理论分析移动性对收敛的促进作用，并设计数据驱动框架优化用户轨迹以增强信息传播
- 实验或效果：通过实验验证理论，证明方法优于基线，并分析网络参数对性能的影响

## 摘要（原文）

> Decentralized Federated Learning (DFL) has emerged as a privacy-preserving machine learning paradigm that enables collaborative training among users without relying on a central server. However, its performance often degrades significantly due to limited connectivity and data heterogeneity. As we move toward the next generation of wireless networks, mobility is increasingly embedded in many real-world applications. The user mobility, either natural or induced, enables clients to act as relays or bridges, thus enhancing information flow in sparse networks; however, its impact on DFL has been largely overlooked despite its potential. In this work, we systematically investigate the role of mobility in improving DFL performance. We first establish the convergence of DFL in sparse networks under user mobility and theoretically demonstrate that even random movement of a fraction of users can significantly boost performance. Building upon this insight, we propose a DFL framework that utilizes mobile users with induced mobility patterns, allowing them to exploit the knowledge of data distribution to determine their trajectories to enhance information propagation through the network. Through extensive experiments, we empirically confirm our theoretical findings, validate the superiority of our approach over baselines, and provide a comprehensive analysis of how various network parameters influence DFL performance in mobile networks.

