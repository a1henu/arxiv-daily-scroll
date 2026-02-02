---
layout: default
title: Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity
---

# Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity
**arXiv**：[2601.22450v1](https://arxiv.org/abs/2601.22450) · [PDF](https://arxiv.org/pdf/2601.22450.pdf)  
**作者**：Jianhao Huang, Baharan Mirzasoleiman  

**一句话要点**：提出优化掩码扩散语言模型隐式正则化方法，基于k-奇偶问题提升泛化性能

**关键词**：掩码扩散语言模型, 隐式正则化, k-奇偶问题, 泛化性能, 模型优化

## 3 点简述
- 研究掩码扩散语言模型在k-奇偶问题中的泛化特性，对比自回归模型
- 理论分解目标为信号与噪声机制，优化掩码概率分布以增强正则化
- 实验显示在50M和8B参数模型上显著提升困惑度，避免grokking现象

## 摘要（原文）

> Masked Diffusion Language Models have recently emerged as a powerful generative paradigm, yet their generalization properties remain understudied compared to their auto-regressive counterparts. In this work, we investigate these properties within the setting of the $k$-parity problem (computing the XOR sum of $k$ relevant bits), where neural networks typically exhibit grokking -- a prolonged plateau of chance-level performance followed by sudden generalization. We theoretically decompose the Masked Diffusion (MD) objective into a Signal regime which drives feature learning, and a Noise regime which serves as an implicit regularizer. By training nanoGPT using MD objective on the $k$-parity problem, we demonstrate that MD objective fundamentally alters the learning landscape, enabling rapid and simultaneous generalization without experiencing grokking. Furthermore, we leverage our theoretical insights to optimize the distribution of the mask probability in the MD objective. Our method significantly improves perplexity for 50M-parameter models and achieves superior results across both pre-training from scratch and supervised fine-tuning. Specifically, we observe performance gains peaking at $8.8\%$ and $5.8\%$, respectively, on 8B-parameter models, confirming the scalability and effectiveness of our framework in large-scale masked diffusion language model regimes.

