---
layout: default
title: Understanding Diffusion Models via Ratio-Based Function Approximation with SignReLU Networks
---

# Understanding Diffusion Models via Ratio-Based Function Approximation with SignReLU Networks
**arXiv**：[2601.21242v1](https://arxiv.org/abs/2601.21242) · [PDF](https://arxiv.org/pdf/2601.21242.pdf)  
**作者**：Luwei Sun, Dongrui Shen, Jianfe Li, Yulong Zhao, Han Feng  

**一句话要点**：提出基于SignReLU网络的比率函数逼近理论框架，以解决扩散模型中条件生成建模的近似问题。

**关键词**：扩散模型, 比率函数逼近, SignReLU网络, 条件生成建模, KL风险分析, 泛化保证

## 3 点简述
- 核心问题：条件生成建模中目标密度为比率形式f1/f2，需高效逼近此类函数。
- 方法要点：利用SignReLU激活的分段结构，在标准正则性假设下建立L^p逼近界和收敛率。
- 实验或效果：应用于DDPM，构建SignReLU神经估计器，推导生成与真实分布间KL风险的泛化保证。

## 摘要（原文）

> Motivated by challenges in conditional generative modeling, where the target conditional density takes the form of a ratio f1 over f2, this paper develops a theoretical framework for approximating such ratio-type functionals. Here, f1 and f2 are kernel-based marginal densities that capture structured interactions, a setting central to diffusion-based generative models. We provide a concise proof for approximating these ratio-type functionals using deep neural networks with the SignReLU activation function, leveraging the activation's piecewise structure. Under standard regularity assumptions, we establish L^p(Omega) approximation bounds and convergence rates. Specializing to Denoising Diffusion Probabilistic Models (DDPMs), we construct a SignReLU-based neural estimator for the reverse process and derive bounds on the excess Kullback-Leibler (KL) risk between the generated and true data distributions. Our analysis decomposes this excess risk into approximation and estimation error components. These results provide generalization guarantees for finite-sample training of diffusion-based generative models.

