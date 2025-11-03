---
layout: default
title: Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications
---

# Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications
**arXiv**：[2510.27186v1](https://arxiv.org/abs/2510.27186) · [PDF](https://arxiv.org/pdf/2510.27186.pdf)  
**作者**：Zixuan Hu, Yongxian Wei, Li Shen, Zhenyi Wang, Lei Li, Chun Yuan, Dacheng Tao  

**一句话要点**：提出稀疏模型反演以高效反演视觉变换器，用于数据缺失应用

**关键词**：模型反演, 视觉变换器, 稀疏优化, 数据缺失应用, 高效计算

## 3 点简述
- 现有密集反演方法效率低，因反演噪声背景和虚假相关性
- 选择性反演语义前景，避免背景和虚假相关，无需修改原损失函数
- 实验显示加速达3.79倍，保持或提升数据缺失量化和知识迁移性能

## 摘要（原文）

> Model inversion, which aims to reconstruct the original training data from
> pre-trained discriminative models, is especially useful when the original
> training data is unavailable due to privacy, usage rights, or size constraints.
> However, existing dense inversion methods attempt to reconstruct the entire
> image area, making them extremely inefficient when inverting high-resolution
> images from large-scale Vision Transformers (ViTs). We further identify two
> underlying causes of this inefficiency: the redundant inversion of noisy
> backgrounds and the unintended inversion of spurious correlations--a phenomenon
> we term "hallucination" in model inversion. To address these limitations, we
> propose a novel sparse model inversion strategy, as a plug-and-play extension
> to speed up existing dense inversion methods with no need for modifying their
> original loss functions. Specifically, we selectively invert semantic
> foregrounds while stopping the inversion of noisy backgrounds and potential
> spurious correlations. Through both theoretical and empirical studies, we
> validate the efficacy of our approach in achieving significant inversion
> acceleration (up to 3.79 faster) while maintaining comparable or even enhanced
> downstream performance in data-free model quantization and data-free knowledge
> transfer. Code is available at https://github.com/Egg-Hu/SMI.

