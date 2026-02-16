---
layout: default
title: Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning
---

# Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning
**arXiv**：[2602.13069v1](https://arxiv.org/abs/2602.13069) · [PDF](https://arxiv.org/pdf/2602.13069.pdf)  
**作者**：Juneyoung Park, Yuri Hong, Seongwan Kim, Jaeho Lee  

**一句话要点**：提出MeSP方法以解决设备端LLM微调中的内存限制问题

**关键词**：设备端微调, 内存优化, LoRA结构, 反向传播, 大语言模型, 梯度计算

## 3 点简述
- 核心问题：设备端微调面临内存限制，现有方法在精确梯度与低内存间存在权衡
- 方法要点：利用LoRA低秩结构手动推导反向传播，通过重计算中间投影减少内存占用
- 实验或效果：在Qwen2.5模型上实现49%内存降低，梯度与MeBP数学相同，提升设备可行性

## 摘要（原文）

> On-device fine-tuning enables privacy-preserving personalization of large language models, but mobile devices impose severe memory constraints, typically 6--12GB shared across all workloads. Existing approaches force a trade-off between exact gradients with high memory (MeBP) and low memory with noisy estimates (MeZO). We propose Memory-efficient Structured Backpropagation (MeSP), which bridges this gap by manually deriving backward passes that exploit LoRA's low-rank structure. Our key insight is that the intermediate projection $h = xA$ can be recomputed during backward at minimal cost since rank $r \ll d_{in}$, eliminating the need to store it. MeSP achieves 49\% average memory reduction compared to MeBP on Qwen2.5 models (0.5B--3B) while computing mathematically identical gradients. Our analysis also reveals that MeZO's gradient estimates show near-zero correlation with true gradients (cosine similarity $\approx$0.001), explaining its slow convergence. MeSP reduces peak memory from 361MB to 136MB for Qwen2.5-0.5B, enabling fine-tuning scenarios previously infeasible on memory-constrained devices.

