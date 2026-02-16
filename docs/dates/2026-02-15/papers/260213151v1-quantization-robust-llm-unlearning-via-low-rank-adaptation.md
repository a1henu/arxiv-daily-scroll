---
layout: default
title: Quantization-Robust LLM Unlearning via Low-Rank Adaptation
---

# Quantization-Robust LLM Unlearning via Low-Rank Adaptation
**arXiv**：[2602.13151v1](https://arxiv.org/abs/2602.13151) · [PDF](https://arxiv.org/pdf/2602.13151.pdf)  
**作者**：João Vitor Boer Abitante, Joana Meneguzzo Pasquali, Luan Fonseca Garcia, Ewerton de Oliveira, Thomas da Silva Paula, Rodrigo C. Barros, Lucas S. Kupssinskü  

**一句话要点**：提出基于低秩适配的量化鲁棒LLM遗忘方法，以解决后训练量化导致遗忘失效的问题。

**关键词**：大语言模型遗忘, 后训练量化, 低秩适配, 量化鲁棒性, 隐私保护, 模型部署

## 3 点简述
- 核心问题：后训练量化会掩盖或擦除LLM遗忘更新，使量化模型恢复遗忘前行为。
- 方法要点：冻结基础模型，通过可训练适配器集中遗忘更新，确保量化后有效保留。
- 实验效果：在Llama-2-7B上，LoRA提升4位量化效用，减少隐私泄露，保持强遗忘性能。

## 摘要（原文）

> Large Language Model (LLM) unlearning aims to remove targeted knowledge from a trained model, but practical deployments often require post-training quantization (PTQ) for efficient inference. However, aggressive low-bit PTQ can mask or erase unlearning updates, causing quantized models to revert to pre-unlearning behavior. We show that standard full-parameter fine-tuning often induce parameter changes that are too small to survive 4-bit quantization. We propose quantization-robust unlearning via low-rank adaptation (LoRA): we freeze the base model and concentrate unlearning into trainable adapters so that the effective update is preserved after quantization. On Llama-2-7B evaluated with MUSE dataset (BOOKS and NEWS), LoRA improves 4-bit utility by up to 7.93 points (NPO+GDR on BOOKS: 50.17 to 58.10) and yields higher 4-bit utility on NEWS for GA+GDR (40.06 to 44.82, increase of 4.76). LoRA also substantially reduces privacy leakage under 4-bit PTQ, e.g., for GA+KLR on BOOKS, PrivLeak moves from -25.68 to -5.86 (closer to ideal 0), while maintaining strong forgetting (VerMem and KnowMem near 0). Thus, using LoRA for Machine Unlearning is beneficial for scenarios where quantization is necessary for model deployment.

