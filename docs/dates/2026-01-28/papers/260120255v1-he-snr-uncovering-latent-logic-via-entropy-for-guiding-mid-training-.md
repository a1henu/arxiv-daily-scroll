---
layout: default
title: HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-BENCH
---

# HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-BENCH
**arXiv**：[2601.20255v1](https://arxiv.org/abs/2601.20255) · [PDF](https://arxiv.org/pdf/2601.20255.pdf)  
**作者**：Yueyang Wang, Jiawei Fu, Baolong Bi, Xili Wang, Xiaoqing Liu  

**一句话要点**：提出HE-SNR指标以指导大语言模型在软件工程任务中的中训练优化

**关键词**：软件工程基准, 中训练优化, 熵压缩假说, 高熵信噪比, 混合专家模型, 长上下文处理

## 3 点简述
- 核心问题：现有指标如困惑度受长上下文影响，与下游软件工程性能相关性弱，缺乏有效指导中训练的指标。
- 方法要点：基于熵压缩假说，定义高熵信噪比（HE-SNR）作为新指标，通过细粒度熵分析结构化不确定性。
- 实验或效果：在工业级混合专家模型上验证，HE-SNR在不同上下文窗口下展现优越的鲁棒性和预测能力。

## 摘要（原文）

> SWE-bench has emerged as the premier benchmark for evaluating Large Language Models on complex software engineering tasks. While these capabilities are fundamentally acquired during the mid-training phase and subsequently elicited during Supervised Fine-Tuning (SFT), there remains a critical deficit in metrics capable of guiding mid-training effectively. Standard metrics such as Perplexity (PPL) are compromised by the "Long-Context Tax" and exhibit weak correlation with downstream SWE performance. In this paper, we bridge this gap by first introducing a rigorous data filtering strategy. Crucially, we propose the Entropy Compression Hypothesis, redefining intelligence not by scalar Top-1 compression, but by the capacity to structure uncertainty into Entropy-Compressed States of low orders ("reasonable hesitation"). Grounded in this fine-grained entropy analysis, we formulate a novel metric, HE-SNR (High-Entropy Signal-to-Noise Ratio). Validated on industrial-scale Mixture-of-Experts (MoE) models across varying context windows (32K/128K), our approach demonstrates superior robustness and predictive power. This work provides both the theoretical foundation and practical tools for optimizing the latent potential of LLMs in complex engineering domains.

