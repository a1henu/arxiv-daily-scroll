---
layout: default
title: Nested Slice Sampling: Vectorized Nested Sampling for GPU-Accelerated Inference
---

# Nested Slice Sampling: Vectorized Nested Sampling for GPU-Accelerated Inference
**arXiv**：[2601.23252v1](https://arxiv.org/abs/2601.23252) · [PDF](https://arxiv.org/pdf/2601.23252.pdf)  
**作者**：David Yallup, Namu Kroupa, Will Handley  

**一句话要点**：提出Nested Slice Sampling以解决GPU加速推理中嵌套采样的并行化难题

**关键词**：嵌套采样, GPU加速推理, 切片采样, 贝叶斯推断, 多模态目标, 并行计算

## 3 点简述
- 核心问题：嵌套采样在复杂多模态目标上难以高效并行化，限制GPU加速。
- 方法要点：引入向量化嵌套切片采样，使用Hit-and-Run切片采样进行约束更新，优化切片宽度设置。
- 实验或效果：在合成目标、高维贝叶斯推理和Gaussian过程超参数边际化中保持准确证据估计和高质量后验样本。

## 摘要（原文）

> Model comparison and calibrated uncertainty quantification often require integrating over parameters, but scalable inference can be challenging for complex, multimodal targets. Nested Sampling is a robust alternative to standard MCMC, yet its typically sequential structure and hard constraints make efficient accelerator implementations difficult. This paper introduces Nested Slice Sampling (NSS), a GPU-friendly, vectorized formulation of Nested Sampling that uses Hit-and-Run Slice Sampling for constrained updates. A tuning analysis yields a simple near-optimal rule for setting the slice width, improving high-dimensional behavior and making per-step compute more predictable for parallel execution. Experiments on challenging synthetic targets, high dimensional Bayesian inference, and Gaussian process hyperparameter marginalization show that NSS maintains accurate evidence estimates and high-quality posterior samples, and is particularly robust on difficult multimodal problems where current state-of-the-art methods such as tempered SMC baselines can struggle. An open-source implementation is released to facilitate adoption and reproducibility.

