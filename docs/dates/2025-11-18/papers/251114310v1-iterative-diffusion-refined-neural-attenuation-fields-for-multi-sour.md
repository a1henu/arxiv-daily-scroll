---
layout: default
title: Iterative Diffusion-Refined Neural Attenuation Fields for Multi-Source Stationary CT Reconstruction: NAF Meets Diffusion Model
---

# Iterative Diffusion-Refined Neural Attenuation Fields for Multi-Source Stationary CT Reconstruction: NAF Meets Diffusion Model
**arXiv**：[2511.14310v1](https://arxiv.org/abs/2511.14310) · [PDF](https://arxiv.org/pdf/2511.14310.pdf)  
**作者**：Jiancheng Fang, Shaoyu Wang, Junlin Wang, Weiwen Wu, Yikun Zhang, Qiegen Liu  

**一句话要点**：提出Diff-NAF以解决超稀疏视图多源静态CT重建问题

**关键词**：CT重建, 神经衰减场, 扩散模型, 超稀疏视图, 多源CT, 迭代优化

## 3 点简述
- 超稀疏视图采样导致CT重建质量严重下降
- 结合神经衰减场与双分支条件扩散模型进行迭代优化
- 实验显示在超稀疏视图条件下性能最佳

## 摘要（原文）

> Multi-source stationary computed tomography (CT) has recently attracted attention for its ability to achieve rapid image reconstruction, making it suitable for time-sensitive clinical and industrial applications. However, practical systems are often constrained by ultra-sparse-view sampling, which significantly degrades reconstruction quality. Traditional methods struggle under ultra-sparse-view settings, where interpolation becomes inaccurate and the resulting reconstructions are unsatisfactory. To address this challenge, this study proposes Diffusion-Refined Neural Attenuation Fields (Diff-NAF), an iterative framework tailored for multi-source stationary CT under ultra-sparse-view conditions. Diff-NAF combines a Neural Attenuation Field representation with a dual-branch conditional diffusion model. The process begins by training an initial NAF using ultra-sparse-view projections. New projections are then generated through an Angle-Prior Guided Projection Synthesis strategy that exploits inter view priors, and are subsequently refined by a Diffusion-driven Reuse Projection Refinement Module. The refined projections are incorporated as pseudo-labels into the training set for the next iteration. Through iterative refinement, Diff-NAF progressively enhances projection completeness and reconstruction fidelity under ultra-sparse-view conditions, ultimately yielding high-quality CT reconstructions. Experimental results on multiple simulated 3D CT volumes and real projection data demonstrate that Diff-NAF achieves the best performance under ultra-sparse-view conditions.

