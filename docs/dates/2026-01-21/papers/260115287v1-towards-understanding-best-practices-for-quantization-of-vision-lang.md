---
layout: default
title: Towards Understanding Best Practices for Quantization of Vision-Language Models
---

# Towards Understanding Best Practices for Quantization of Vision-Language Models
**arXiv**：[2601.15287v1](https://arxiv.org/abs/2601.15287) · [PDF](https://arxiv.org/pdf/2601.15287.pdf)  
**作者**：Gautom Das, Vincent La, Ethan Lau, Abhinav Shrivastava, Matthew Gwilliam  

**一句话要点**：研究视觉语言模型量化最佳实践，评估不同方法对多模态任务性能的影响

**关键词**：视觉语言模型量化, 多模态管道, GPTQ, AWQ, 性能评估, 高效部署

## 3 点简述
- 核心问题：量化如何有效应用于视觉模型、语言模型及其连接器的多模态管道，以降低内存和延迟
- 方法要点：应用GPTQ和AWQ等先进量化方法，分析比特宽度、量化方法及量化部分对性能的影响
- 实验或效果：发现ViT和LLM对性能重要性相当，LLM低比特量化在降低比特每权重时保持高准确率

## 摘要（原文）

> Large language models (LLMs) deliver impressive results for a variety of tasks, but state-of-the-art systems require fast GPUs with large amounts of memory. To reduce both the memory and latency of these systems, practitioners quantize their learned parameters, typically at half precision. A growing body of research focuses on preserving the model performance with more aggressive bit widths, and some work has been done to apply these strategies to other models, like vision transformers. In our study we investigate how a variety of quantization methods, including state-of-the-art GPTQ and AWQ, can be applied effectively to multimodal pipelines comprised of vision models, language models, and their connectors. We address how performance on captioning, retrieval, and question answering can be affected by bit width, quantization method, and which portion of the pipeline the quantization is used for. Results reveal that ViT and LLM exhibit comparable importance in model performance, despite significant differences in parameter size, and that lower-bit quantization of the LLM achieves high accuracy at reduced bits per weight (bpw). These findings provide practical insights for efficient deployment of MLLMs and highlight the value of exploration for understanding component sensitivities in multimodal models. Our code is available at https://github.com/gautomdas/mmq.

