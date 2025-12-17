---
layout: default
title: SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models
---

# SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models
**arXiv**：[2512.14481v1](https://arxiv.org/abs/2512.14481) · [PDF](https://arxiv.org/pdf/2512.14481.pdf)  
**作者**：Shizhuo Mao, Song Chen, Yi Kang  

**一句话要点**：提出SASQ框架以解决大语言模型激活量化中的静态精度与部署效率权衡问题。

**关键词**：大语言模型, 量化感知训练, 激活量化, 静态推理, 部署效率

## 3 点简述
- 核心问题：大语言模型量化面临动态量化计算开销高与静态量化精度损失的根本权衡。
- 方法要点：SASQ仅优化量化因子，不改变预训练权重，通过自适应截断异常值实现高精度静态推理。
- 实验或效果：在LLaMA2-7B上，SASQ的困惑度低于QuaRot 5.2%，且优于FP16模型4.7%。

## 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but face deployment challenges due to their growing size outpacing GPU memory advancements. Model quantization mitigates this issue by lowering weight and activation precision, but existing solutions face fundamental trade-offs: dynamic quantization incurs high computational overhead and poses deployment challenges on edge devices, while static quantization sacrifices accuracy. Existing approaches of quantization-aware training (QAT) further suffer from weight training costs. We propose SASQ: a lightweight QAT framework specifically tailored for activation quantization factors. SASQ exclusively optimizes only the quantization factors (without changing pre-trained weights), enabling static inference with high accuracy while maintaining deployment efficiency. SASQ adaptively truncates some outliers, thereby reducing the difficulty of quantization while preserving the distributional characteristics of the activations. SASQ not only surpasses existing SOTA quantization schemes but also outperforms the corresponding FP16 models. On LLaMA2-7B, it achieves 5.2% lower perplexity than QuaRot and 4.7% lower perplexity than the FP16 model on WikiText2.

