---
layout: default
title: Uniform Spectral Growth and Convergence of Muon in LoRA-Style Matrix Factorization
---

# Uniform Spectral Growth and Convergence of Muon in LoRA-Style Matrix Factorization
**arXiv**：[2602.06385v1](https://arxiv.org/abs/2602.06385) · [PDF](https://arxiv.org/pdf/2602.06385.pdf)  
**作者**：Changmin Kang, Jihun Yun, Baekrok Shin, Yeseul Cho, Chulhee Yun  

**一句话要点**：分析Muon在LoRA风格矩阵分解中的谱均匀增长与收敛性，揭示奇异值等速率动态。

**关键词**：谱梯度下降, LoRA微调, 矩阵分解, 奇异值动态, 全局收敛, 优化理论

## 3 点简述
- 核心问题：Muon优化器在LoRA微调中奇异值近均匀增长的现象缺乏理论理解。
- 方法要点：在简化LoRA风格矩阵分解中分析谱梯度流，证明奇异值等速率增长和全局收敛。
- 实验或效果：通过实验验证理论，显示小奇异值先于大奇异值达到目标，与标准梯度流形成对比。

## 摘要（原文）

> Spectral gradient descent (SpecGD) orthogonalizes the matrix parameter updates and has inspired practical optimizers such as Muon. They often perform well in large language model (LLM) training, but their dynamics remain poorly understood. In the low-rank adaptation (LoRA) setting, where weight updates are parameterized as a product of two low-rank factors, we find a distinctive spectral phenomenon under Muon in LoRA fine-tuning of LLMs: singular values of the LoRA product show near-uniform growth across the spectrum, despite orthogonalization being performed on the two factors separately. Motivated by this observation, we analyze spectral gradient flow (SpecGF)-a continuous-time analogue of SpecGD-in a simplified LoRA-style matrix factorization setting and prove "equal-rate" dynamics: all singular values grow at equal rates up to small deviations. Consequently, smaller singular values attain their target values earlier than larger ones, sharply contrasting with the largest-first stepwise learning observed in standard gradient flow. Moreover, we prove that SpecGF in our setting converges to global minima from almost all initializations, provided the factor norms remain bounded; with $\ell_2$ regularization, we obtain global convergence. Lastly, we corroborate our theory with experiments in the same setting.

