---
layout: default
title: HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs
---

# HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs
**arXiv**：[2601.20745v1](https://arxiv.org/abs/2601.20745) · [PDF](https://arxiv.org/pdf/2601.20745.pdf)  
**作者**：Guoan Wang, Feiyu Wang, Zongwei Lv, Yikun Zong, Tong Yang  

**一句话要点**：提出Hestia框架，通过Hessian引导的软量化训练解决极低比特大语言模型优化难题。

**关键词**：量化感知训练, 极低比特量化, Hessian引导, 大语言模型, 梯度优化, 软量化

## 3 点简述
- 核心问题：传统量化感知训练过早离散化，导致梯度不匹配，阻碍极低比特模型优化。
- 方法要点：使用温度控制软max松弛替代硬舍入，结合Hessian迹指导细粒度温度退火。
- 实验或效果：在Llama-3.2上优于现有三元量化基线，1B和3B模型零样本性能平均提升约5%和4%。

## 摘要（原文）

> As large language models (LLMs) continue to scale, deployment is increasingly bottlenecked by the memory wall, motivating a shift toward extremely low-bit quantization. However, most quantization-aware training (QAT) methods apply hard rounding and the straight-through estimator (STE) from the beginning of the training, which prematurely discretizes the optimization landscape and induces persistent gradient mismatch between latent weights and quantized weights, hindering effective optimization of quantized models. To address this, we propose Hestia, a Hessian-guided differentiable QAT framework for extremely low-bit LLMs, which replaces the rigid step function with a temperature-controlled softmax relaxation to maintain gradient flow early in training while progressively hardening quantization. Furthermore, Hestia leverages a tensor-wise Hessian trace metric as a lightweight curvature signal to drive fine-grained temperature annealing, enabling sensitivity-aware discretization across the model. Evaluations on Llama-3.2 show that Hestia consistently outperforms existing ternary QAT baselines, yielding average zero-shot improvements of 5.39% and 4.34% for the 1B and 3B models. These results indicate that Hessian-guided relaxation effectively recovers representational capacity, establishing a more robust training path for 1.58-bit LLMs. The code is available at https://github.com/hestia2026/Hestia.

