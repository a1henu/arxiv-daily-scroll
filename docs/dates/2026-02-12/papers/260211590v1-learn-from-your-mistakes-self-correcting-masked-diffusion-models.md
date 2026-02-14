---
layout: default
title: Learn from Your Mistakes: Self-Correcting Masked Diffusion Models
---

# Learn from Your Mistakes: Self-Correcting Masked Diffusion Models
**arXiv**：[2602.11590v1](https://arxiv.org/abs/2602.11590) · [PDF](https://arxiv.org/pdf/2602.11590.pdf)  
**作者**：Yair Schiff, Omer Belhasin, Roy Uziel, Guanghan Wang, Marianne Arriola, Gilad Turok, Michael Elad, Volodymyr Kuleshov  

**一句话要点**：提出渐进式自校正框架以解决掩码扩散模型错误累积问题

**关键词**：掩码扩散模型, 自校正训练, 并行生成, 错误累积, 渐进式细化

## 3 点简述
- 掩码扩散模型在并行生成时存在错误累积，导致样本质量下降
- 训练模型同时执行去掩码和校正，利用去噪网络输出进行自校正训练
- 实验显示在质量和效率上优于标准模型，支持推理时计算扩展

## 摘要（原文）

> Masked diffusion models (MDMs) have emerged as a promising alternative to autoregressive models, enabling parallel token generation while achieving competitive performance. Despite these advantages, MDMs face a fundamental limitation: once tokens are unmasked, they remain fixed, leading to error accumulation and ultimately degrading sample quality. We address this by proposing a framework that trains a model to perform both unmasking and correction. By reusing outputs from the MDM denoising network as inputs for corrector training, we train a model to recover from potential mistakes. During generation we apply additional corrective refinement steps between unmasking ones in order to change decoded tokens and improve outputs. We name our training and sampling method Progressive Self-Correction (ProSeCo) for its unique ability to iteratively refine an entire sequence, including already generated tokens. We conduct extensive experimental validation across multiple conditional and unconditional tasks, demonstrating that ProSeCo yields better quality-efficiency trade-offs (up to ~2-3x faster sampling) and enables inference-time compute scaling to further increase sample quality beyond standard MDMs (up to ~1.3x improvement on benchmarks).

