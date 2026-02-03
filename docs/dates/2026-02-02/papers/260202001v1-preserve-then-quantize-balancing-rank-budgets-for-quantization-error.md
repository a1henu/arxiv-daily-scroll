---
layout: default
title: Preserve-Then-Quantize: Balancing Rank Budgets for Quantization Error Reconstruction in LLMs
---

# Preserve-Then-Quantize: Balancing Rank Budgets for Quantization Error Reconstruction in LLMs
**arXiv**：[2602.02001v1](https://arxiv.org/abs/2602.02001) · [PDF](https://arxiv.org/pdf/2602.02001.pdf)  
**作者**：Yoonjun Cho, Dongjae Jeon, Soeun Kim, Moongyu Jeon, Albert No  

**一句话要点**：提出结构化残差重建框架，通过平衡秩预算优化大语言模型量化误差重建。

**关键词**：量化误差重建, 结构化残差重建, 量化后训练, 参数高效微调, 大语言模型, 秩分配

## 3 点简述
- 量化误差重建方法在量化后训练中因全秩预算用于误差重建而次优，当权重具有内在低秩结构时。
- 提出结构化残差重建，先保留激活缩放权重的顶部奇异子空间，再量化残差并用剩余秩进行误差重建。
- 实验显示在量化后训练中降低困惑度，并在2位量化参数高效微调下提升GLUE分数5.9个百分点。

## 摘要（原文）

> Quantization Error Reconstruction (QER) reduces accuracy loss in Post-Training Quantization (PTQ) by approximating weights as $\mathbf{W} \approx \mathbf{Q} + \mathbf{L}\mathbf{R}$, using a rank-$r$ correction to reconstruct quantization error. Prior methods devote the full rank budget to error reconstruction, which is suboptimal when $\mathbf{W}$ has intrinsic low-rank structure and quantization corrupts dominant directions. We propose Structured Residual Reconstruction (SRR), a rank-allocation framework that preserves the top-$k$ singular subspace of the activation-scaled weight before quantization, quantizes only the residual, and uses the remaining rank $r-k$ for error reconstruction. We derive a theory-guided criterion for selecting $k$ by balancing quantization-exposed energy and unrecoverable error under rank constraints. We further show that resulting $\mathbf{Q} + \mathbf{L}\mathbf{R}$ parameterization naturally supports Quantized Parameter-Efficient Fine-Tuning (QPEFT), and stabilizes fine-tuning via gradient scaling along preserved directions. Experiments demonstrate consistent perplexity reductions across diverse models and quantization settings in PTQ, along with a 5.9 percentage-point average gain on GLUE under 2-bit QPEFT.

