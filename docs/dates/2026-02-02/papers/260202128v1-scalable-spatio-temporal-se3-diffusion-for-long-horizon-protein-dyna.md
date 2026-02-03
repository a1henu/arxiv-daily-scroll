---
layout: default
title: Scalable Spatio-Temporal SE(3) Diffusion for Long-Horizon Protein Dynamics
---

# Scalable Spatio-Temporal SE(3) Diffusion for Long-Horizon Protein Dynamics
**arXiv**：[2602.02128v1](https://arxiv.org/abs/2602.02128) · [PDF](https://arxiv.org/pdf/2602.02128.pdf)  
**作者**：Nima Shoghi, Yuxuan Liu, Yuning Shen, Rob Brekelmans, Pan Li, Quanquan Gu  

**一句话要点**：提出STAR-MD扩散模型以解决蛋白质长时程动力学模拟的挑战

**关键词**：蛋白质动力学, 扩散模型, SE(3)-等变性, 时空建模, 长时程生成, 分子模拟

## 3 点简述
- 核心问题：分子动力学模拟计算成本高，现有生成模型在长时程生成中受架构限制和误差累积影响。
- 方法要点：采用SE(3)-等变扩散模型，结合因果扩散变换器和联合时空注意力，高效捕获时空依赖。
- 实验或效果：在ATLAS基准上实现最优性能，能稳定生成微秒级轨迹，提升构象覆盖和结构有效性。

## 摘要（原文）

> Molecular dynamics (MD) simulations remain the gold standard for studying protein dynamics, but their computational cost limits access to biologically relevant timescales. Recent generative models have shown promise in accelerating simulations, yet they struggle with long-horizon generation due to architectural constraints, error accumulation, and inadequate modeling of spatio-temporal dynamics. We present STAR-MD (Spatio-Temporal Autoregressive Rollout for Molecular Dynamics), a scalable SE(3)-equivariant diffusion model that generates physically plausible protein trajectories over microsecond timescales. Our key innovation is a causal diffusion transformer with joint spatio-temporal attention that efficiently captures complex space-time dependencies while avoiding the memory bottlenecks of existing methods. On the standard ATLAS benchmark, STAR-MD achieves state-of-the-art performance across all metrics--substantially improving conformational coverage, structural validity, and dynamic fidelity compared to previous methods. STAR-MD successfully extrapolates to generate stable microsecond-scale trajectories where baseline methods fail catastrophically, maintaining high structural quality throughout the extended rollout. Our comprehensive evaluation reveals severe limitations in current models for long-horizon generation, while demonstrating that STAR-MD's joint spatio-temporal modeling enables robust dynamics simulation at biologically relevant timescales, paving the way for accelerated exploration of protein function.

