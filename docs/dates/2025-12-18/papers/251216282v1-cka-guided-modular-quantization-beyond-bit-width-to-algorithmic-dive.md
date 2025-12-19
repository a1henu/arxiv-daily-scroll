---
layout: default
title: CKA-Guided Modular Quantization: Beyond Bit-Width to Algorithmic Diversity
---

# CKA-Guided Modular Quantization: Beyond Bit-Width to Algorithmic Diversity
**arXiv**：[2512.16282v1](https://arxiv.org/abs/2512.16282) · [PDF](https://arxiv.org/pdf/2512.16282.pdf)  
**作者**：Jinhao Zhang, Yunquan Zhang, Daning Chen  

**一句话要点**：提出CKA引导的模块化量化方法，以解决大语言模型后训练量化中算法异质性不足的问题。

**关键词**：后训练量化, 算法异质性, 线性中心核对齐, 大语言模型, 模块化量化

## 3 点简述
- 核心问题：主流后训练量化方法采用统一策略，忽略网络层间算法适用性差异。
- 方法要点：基于线性中心核对齐评估各层多算法，自动选择最优量化策略构建混合模型。
- 实验或效果：在LLaMA和Qwen等模型上，困惑度和下游任务性能优于均匀量化和先进混合精度方法。

## 摘要（原文）

> Current mainstream post-training quantization methods for large language models typically apply a uniform quantization strategy across all network layers, overlooking the substantial differences in algorithmic suitability among layers. To address this limitation, we propose CKA Guided Modular Quantization, a fine-tuning-free, plug-and-play framework for algorithmic heterogeneous quantization. Our method independently evaluates multiple PTQ algorithms on each layer and employs Linear Centered Kernel Alignment (CKA) as a metric to automatically select the optimal quantization strategy per layer. The individually optimized strategies are then integrated to construct a hybrid quantized model. Experiments demonstrate that our approach consistently outperforms both uniform quantization baselines and state-of-the-art mixed-precision methods across mainstream LLMs including LLaMA and Qwen ,in terms of perplexity (PPL) and downstream task performance.

