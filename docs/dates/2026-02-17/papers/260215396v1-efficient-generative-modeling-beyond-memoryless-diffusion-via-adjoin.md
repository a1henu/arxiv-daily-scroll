---
layout: default
title: Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching
---

# Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching
**arXiv**：[2602.15396v1](https://arxiv.org/abs/2602.15396) · [PDF](https://arxiv.org/pdf/2602.15396.pdf)  
**作者**：Jeongwoo Shin, Jinhwan Sul, Joonseok Lee, Jaewong Choi, Jaemoo Choi  

**一句话要点**：提出伴随薛定谔桥匹配以解决扩散模型轨迹弯曲和噪声问题，实现高效生成建模。

**关键词**：生成建模, 薛定谔桥, 轨迹优化, 图像生成, 蒸馏训练

## 3 点简述
- 扩散模型因前向过程无记忆性导致轨迹弯曲和噪声评分目标。
- ASBM通过两阶段学习最优轨迹：数据到能量采样和简单匹配损失。
- 实验显示ASBM在图像生成中提高保真度并减少采样步数。

## 摘要（原文）

> Diffusion models often yield highly curved trajectories and noisy score targets due to an uninformative, memoryless forward process that induces independent data-noise coupling. We propose Adjoint Schrödinger Bridge Matching (ASBM), a generative modeling framework that recovers optimal trajectories in high dimensions via two stages. First, we view the Schrödinger Bridge (SB) forward dynamic as a coupling construction problem and learn it through a data-to-energy sampling perspective that transports data to an energy-defined prior. Then, we learn the backward generative dynamic with a simple matching loss supervised by the induced optimal coupling. By operating in a non-memoryless regime, ASBM produces significantly straighter and more efficient sampling paths. Compared to prior works, ASBM scales to high-dimensional data with notably improved stability and efficiency. Extensive experiments on image generation show that ASBM improves fidelity with fewer sampling steps. We further showcase the effectiveness of our optimal trajectory via distillation to a one-step generator.

