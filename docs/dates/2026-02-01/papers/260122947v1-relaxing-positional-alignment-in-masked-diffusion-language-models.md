---
layout: default
title: Relaxing Positional Alignment in Masked Diffusion Language Models
---

# Relaxing Positional Alignment in Masked Diffusion Language Models
**arXiv**：[2601.22947v1](https://arxiv.org/abs/2601.22947) · [PDF](https://arxiv.org/pdf/2601.22947.pdf)  
**作者**：Mengyu Ye, Ryosuke Takahashi, Keito Kudo, Jun Suzuki  

**一句话要点**：提出对齐灵活监督策略以提升掩码扩散语言模型的开放文本生成质量

**关键词**：掩码扩散语言模型, 开放文本生成, 位置对齐, 连接主义时序分类, 微调策略

## 3 点简述
- 核心问题：MDLM在开放文本生成中因严格位置预测导致解码对令牌错位敏感，语义易受破坏。
- 方法要点：通过连接主义时序分类目标引入<slack>令牌，在微调中采用对齐灵活监督策略。
- 实验或效果：在五个开放文本生成基准上，方法持续优于原模型，并增强了对位置偏移的鲁棒性。

## 摘要（原文）

> Masked diffusion language models (MDLMs) have emerged as a promising alternative to dominant autoregressive approaches. Although they achieve competitive performance on several tasks, a substantial gap remains in open-ended text generation. We hypothesize that one cause of this gap is that strict positional prediction makes MDLM decoding highly sensitive to token misalignment, and we show through controlled interventions that a one-position shift can severely disrupt semantics. This observation suggests that enforcing strict positional supervision during training is misaligned with the irreversible denoising dynamics of MDLM decoding. Motivated by this mismatch, we adopt an alignment-flexible supervision strategy during fine-tuning. Specifically, we introduce a special token <slack> via the connectionist temporal classification objective. We apply this approach to the widely used MDLM model and conduct experiments on five open-ended text generation benchmarks. Our method consistently outperforms the original model and improves robustness to positional shifts, indicating that relaxing strict positional supervision is an important factor in improving generation quality in MDLMs.

