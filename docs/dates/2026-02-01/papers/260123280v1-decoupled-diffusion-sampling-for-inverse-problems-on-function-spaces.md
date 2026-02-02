---
layout: default
title: Decoupled Diffusion Sampling for Inverse Problems on Function Spaces
---

# Decoupled Diffusion Sampling for Inverse Problems on Function Spaces
**arXiv**：[2601.23280v1](https://arxiv.org/abs/2601.23280) · [PDF](https://arxiv.org/pdf/2601.23280.pdf)  
**作者**：Thomas Y. L. Lin, Jiachen Yao, Lufang Chiang, Julius Berner, Anima Anandkumar  

**一句话要点**：提出解耦扩散逆求解器以解决函数空间逆PDE问题中的数据效率低和物理建模不足问题

**关键词**：函数空间逆问题, 解耦扩散采样, 物理感知生成, 神经算子, 数据高效学习, 后验采样优化

## 3 点简述
- 核心问题：现有扩散后验采样器在函数空间逆PDE问题中依赖大量配对数据，物理建模隐式，导致数据效率低和过平滑
- 方法要点：采用解耦设计，无条件扩散学习系数先验，神经算子显式建模前向PDE指导，支持解耦退火后验采样避免过平滑
- 实验或效果：在稀疏观测下实现最优性能，平均l2误差降低11%，谱误差降低54%；数据限制至1%时，l2误差优势达40%

## 摘要（原文）

> We propose a data-efficient, physics-aware generative framework in function space for inverse PDE problems. Existing plug-and-play diffusion posterior samplers represent physics implicitly through joint coefficient-solution modeling, requiring substantial paired supervision. In contrast, our Decoupled Diffusion Inverse Solver (DDIS) employs a decoupled design: an unconditional diffusion learns the coefficient prior, while a neural operator explicitly models the forward PDE for guidance. This decoupling enables superior data efficiency and effective physics-informed learning, while naturally supporting Decoupled Annealing Posterior Sampling (DAPS) to avoid over-smoothing in Diffusion Posterior Sampling (DPS). Theoretically, we prove that DDIS avoids the guidance attenuation failure of joint models when training data is scarce. Empirically, DDIS achieves state-of-the-art performance under sparse observation, improving $l_2$ error by 11% and spectral error by 54% on average; when data is limited to 1%, DDIS maintains accuracy with 40% advantage in $l_2$ error compared to joint models.

