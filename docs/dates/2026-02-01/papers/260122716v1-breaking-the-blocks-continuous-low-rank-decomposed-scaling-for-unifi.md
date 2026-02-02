---
layout: default
title: Breaking the Blocks: Continuous Low-Rank Decomposed Scaling for Unified LLM Quantization and Adaptation
---

# Breaking the Blocks: Continuous Low-Rank Decomposed Scaling for Unified LLM Quantization and Adaptation
**arXiv**：[2601.22716v1](https://arxiv.org/abs/2601.22716) · [PDF](https://arxiv.org/pdf/2601.22716.pdf)  
**作者**：Pingzhi Tang, Ruijie Zhou, Fanxu Meng, Wenjie Pei, Muhan Zhang  

**一句话要点**：提出LoRDS框架，通过连续低秩分解实现统一LLM量化与适配，提升表达效率。

**关键词**：低秩分解, 大语言模型量化, 参数高效微调, 连续缩放, 元素级量化, 统一压缩适配

## 3 点简述
- 核心问题：现有LLM量化方法依赖块结构，牺牲表达灵活性以维持效率。
- 方法要点：建模缩放流形为连续低秩矩阵，实现元素级量化，支持高效PTQ、QAT和PEFT。
- 实验或效果：在Llama3-8B上，3位量化精度提升27.0%，推理加速1.5倍，PEFT性能提升9.6%。

## 摘要（原文）

> Current quantization methods for LLMs predominantly rely on block-wise structures to maintain efficiency, often at the cost of representational flexibility. In this work, we demonstrate that element-wise quantization can be made as efficient as block-wise scaling while providing strictly superior expressive power by modeling the scaling manifold as continuous low-rank matrices ($S = BA$). We propose Low-Rank Decomposed Scaling (LoRDS), a unified framework that rethinks quantization granularity through this low-rank decomposition. By "breaking the blocks" of spatial constraints, LoRDS establishes a seamless efficiency lifecycle: it provides high-fidelity PTQ initialization refined via iterative optimization, enables joint QAT of weights and scaling factors, and facilitates high-rank multiplicative PEFT adaptation. Unlike additive PEFT approaches such as QLoRA, LoRDS enables high-rank weight updates within a low-rank budget while incurring no additional inference overhead. Supported by highly optimized Triton kernels, LoRDS consistently outperforms state-of-the-art baselines across various model families in both quantization and downstream fine-tuning tasks. Notably, on Llama3-8B, our method achieves up to a 27.0% accuracy improvement at 3 bits over NormalFloat quantization and delivers a 1.5x inference speedup on NVIDIA RTX 4090 while enhancing PEFT performance by 9.6% on downstream tasks over 4bit QLoRA, offering a robust and integrated solution for unified compression and adaptation of LLMs.

