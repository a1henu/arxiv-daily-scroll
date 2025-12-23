---
layout: default
title: Can abstract concepts from LLM improve SLM performance?
---

# Can abstract concepts from LLM improve SLM performance?
**arXiv**：[2512.19069v1](https://arxiv.org/abs/2512.19069) · [PDF](https://arxiv.org/pdf/2512.19069.pdf)  
**作者**：Siddharth Tandon  

**一句话要点**：提出从大模型提取抽象概念并转移至小模型，以提升资源受限设备上的性能。

**关键词**：抽象概念转移, 推理时优化, 小语言模型, 导向向量, 资源受限部署

## 3 点简述
- 核心问题：大模型在资源受限设备部署困难，现有方法需大量实验和设计。
- 方法要点：从大模型提取高层概念（导向向量），在推理时转移至小模型。
- 实验或效果：概念可跨模型家族转移，动态调整导向强度提升准确率7-15%。

## 摘要（原文）

> Large language models (LLMs) excel at diverse tasks, but their deployment on resource-constrained devices remains challenging. Existing methods like quantization, pruning, and distillation can reduce memory footprint but often demand extensive experimentation and careful infrastructure design. Leveraging existing techniques for extracting high-level concepts (represented as steering vectors) from larger models, we investigate their transferability to smaller language models (SLM) during inference. We demonstrate through extensive experimentation that these concepts can be effectively transferred to smaller models, irrespective of their family (e.g., Phi, Llama, Qwen), leading to performance improvements across a wide range of tasks. Furthermore, we introduce inference-time scaling to enhance performance by dynamically adjusting the steering intensity which has resulted in a 7-15\% of accuracy improvement for Qwen3-0.6B.

