---
layout: default
title: Deconstructing Generative Diversity: An Information Bottleneck Analysis of Discrete Latent Generative Models
---

# Deconstructing Generative Diversity: An Information Bottleneck Analysis of Discrete Latent Generative Models
**arXiv**：[2512.01831v1](https://arxiv.org/abs/2512.01831) · [PDF](https://arxiv.org/pdf/2512.01831.pdf)  
**作者**：Yudi Wu, Wenhao Zhao, Dianbo Liu  

**一句话要点**：提出基于信息瓶颈的诊断框架，分析离散潜在生成模型的生成多样性差异

**关键词**：生成多样性, 信息瓶颈分析, 离散潜在模型, 零样本干预, 压缩与多样性权衡

## 3 点简述
- 核心问题：AR、MIM和扩散模型在生成多样性上存在显著差异，原因未知
- 方法要点：将生成建模为压缩压力与多样性压力的冲突，并分解为路径多样性和执行多样性
- 实验或效果：应用零样本干预揭示三种模型的策略：MIM优先多样性、AR优先压缩、扩散解耦

## 摘要（原文）

> Generative diversity varies significantly across discrete latent generative models such as AR, MIM, and Diffusion. We propose a diagnostic framework, grounded in Information Bottleneck (IB) theory, to analyze the underlying strategies resolving this behavior. The framework models generation as a conflict between a 'Compression Pressure' - a drive to minimize overall codebook entropy - and a 'Diversity Pressure' - a drive to maximize conditional entropy given an input. We further decompose this diversity into two primary sources: 'Path Diversity', representing the choice of high-level generative strategies, and 'Execution Diversity', the randomness in executing a chosen strategy. To make this decomposition operational, we introduce three zero-shot, inference-time interventions that directly perturb the latent generative process and reveal how models allocate and express diversity. Application of this probe-based framework to representative AR, MIM, and Diffusion systems reveals three distinct strategies: "Diversity-Prioritized" (MIM), "Compression-Prioritized" (AR), and "Decoupled" (Diffusion). Our analysis provides a principled explanation for their behavioral differences and informs a novel inference-time diversity enhancement technique.

