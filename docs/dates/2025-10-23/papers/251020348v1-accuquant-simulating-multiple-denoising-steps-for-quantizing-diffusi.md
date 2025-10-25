---
layout: default
title: AccuQuant: Simulating Multiple Denoising Steps for Quantizing Diffusion Models
---

# AccuQuant: Simulating Multiple Denoising Steps for Quantizing Diffusion Models
**arXiv**：[2510.20348v1](https://arxiv.org/abs/2510.20348) · [PDF](https://arxiv.org/pdf/2510.20348.pdf)  
**作者**：Seunghoon Lee, Jeongwoo Choi, Byunggwan Son, Jaehyeon Moon, Jeimin Jeon, Bumsub Ham  

**一句话要点**：提出AccuQuant以缓解扩散模型量化中的误差累积问题

**关键词**：扩散模型, 后训练量化, 误差累积, 去噪步骤模拟, 内存优化

## 3 点简述
- 核心问题：扩散模型量化误差在采样去噪步骤中累积，影响性能。
- 方法要点：模拟多步去噪过程，最小化全精度与量化模型输出差异。
- 实验或效果：在标准基准上验证了方法的有效性和效率。

## 摘要（原文）

> We present in this paper a novel post-training quantization (PTQ) method,
> dubbed AccuQuant, for diffusion models. We show analytically and empirically
> that quantization errors for diffusion models are accumulated over denoising
> steps in a sampling process. To alleviate the error accumulation problem,
> AccuQuant minimizes the discrepancies between outputs of a full-precision
> diffusion model and its quantized version within a couple of denoising steps.
> That is, it simulates multiple denoising steps of a diffusion sampling process
> explicitly for quantization, accounting the accumulated errors over multiple
> denoising steps, which is in contrast to previous approaches to imitating a
> training process of diffusion models, namely, minimizing the discrepancies
> independently for each step. We also present an efficient implementation
> technique for AccuQuant, together with a novel objective, which reduces a
> memory complexity significantly from $\mathcal{O}(n)$ to $\mathcal{O}(1)$,
> where $n$ is the number of denoising steps. We demonstrate the efficacy and
> efficiency of AccuQuant across various tasks and diffusion models on standard
> benchmarks.

