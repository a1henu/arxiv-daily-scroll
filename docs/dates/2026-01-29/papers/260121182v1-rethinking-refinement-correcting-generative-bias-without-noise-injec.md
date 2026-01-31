---
layout: default
title: Rethinking Refinement: Correcting Generative Bias without Noise Injection
---

# Rethinking Refinement: Correcting Generative Bias without Noise Injection
**arXiv**：[2601.21182v1](https://arxiv.org/abs/2601.21182) · [PDF](https://arxiv.org/pdf/2601.21182.pdf)  
**作者**：Xin Peng, Ang Gao  

**一句话要点**：提出双阶段流精炼框架以纠正生成模型偏差，无需噪声注入或重采样

**关键词**：生成模型偏差纠正, 流精炼, 潜在空间对齐, 数据空间精炼, 单步评估优化, 高维样本质量

## 3 点简述
- 生成模型如扩散和流模型存在系统性偏差，影响高维样本质量
- 基于流匹配设计双阶段精炼，在潜在空间和数据空间进行确定性校正
- 在MNIST等数据集上显著提升保真度和覆盖度，MNIST上FID达1.46

## 摘要（原文）

> Generative models, including diffusion and flow-based models, often exhibit systematic biases that degrade sample quality, particularly in high-dimensional settings. We revisit refinement methods and show that effective bias correction can be achieved as a post-hoc procedure, without noise injection or multi-step resampling of the sampling process. We propose a flow-matching-based \textbf{Bi-stage Flow Refinement (BFR)} framework with two refinement strategies operating at different stages: latent space alignment for approximately invertible generators and data space refinement trained with lightweight augmentations. Unlike previous refiners that perturb sampling dynamics, BFR preserves the original ODE trajectory and applies deterministic corrections to generated samples. Experiments on MNIST, CIFAR-10, and FFHQ at 256x256 resolution demonstrate consistent improvements in fidelity and coverage; notably, starting from base samples with FID 3.95, latent space refinement achieves a \textbf{state-of-the-art} FID of \textbf{1.46} on MNIST using only a single additional function evaluation (1-NFE), while maintaining sample diversity.

