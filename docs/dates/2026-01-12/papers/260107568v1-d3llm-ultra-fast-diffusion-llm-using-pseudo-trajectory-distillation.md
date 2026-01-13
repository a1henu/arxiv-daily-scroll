---
layout: default
title: d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation
---

# d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation
**arXiv**：[2601.07568v1](https://arxiv.org/abs/2601.07568) · [PDF](https://arxiv.org/pdf/2601.07568.pdf)  
**作者**：Yu-Yang Qian, Junda Su, Lanxiang Hu, Peiyuan Zhang, Zhijie Deng, Peng Zhao, Hao Zhang  

**一句话要点**：提出d3LLM，通过伪轨迹蒸馏和熵解码平衡扩散大语言模型的准确性与并行性。

**关键词**：扩散大语言模型, 伪轨迹蒸馏, 并行解码, 熵解码, KV缓存刷新, 准确性并行性权衡

## 3 点简述
- 扩散大语言模型面临准确性与并行性的权衡，现有方法常偏重单一方面。
- 训练时引入伪轨迹蒸馏，指导模型早期解码；推理时采用熵解码与KV缓存刷新。
- 实验显示d3LLM在保持准确性的同时，相比基线模型实现最高10倍加速。

## 摘要（原文）

> Diffusion large language models (dLLMs) offer capabilities beyond those of autoregressive (AR) LLMs, such as parallel decoding and random-order generation. However, realizing these benefits in practice is non-trivial, as dLLMs inherently face an accuracy-parallelism trade-off. Despite increasing interest, existing methods typically focus on only one-side of the coin, targeting either efficiency or performance. To address this limitation, we propose d3LLM (Pseudo-Distilled Diffusion Large Language Model), striking a balance between accuracy and parallelism: (i) during training, we introduce pseudo-trajectory distillation to teach the model which tokens can be decoded confidently at early steps, thereby improving parallelism; (ii) during inference, we employ entropy-based multi-block decoding with a KV-cache refresh mechanism to achieve high parallelism while maintaining accuracy. To better evaluate dLLMs, we also introduce AUP (Accuracy Under Parallelism), a new metric that jointly measures accuracy and parallelism. Experiments demonstrate that our d3LLM achieves up to 10$\times$ speedup over vanilla LLaDA/Dream and 5$\times$ speedup over AR models without much accuracy drop. Our code is available at https://github.com/hao-ai-lab/d3LLM.

