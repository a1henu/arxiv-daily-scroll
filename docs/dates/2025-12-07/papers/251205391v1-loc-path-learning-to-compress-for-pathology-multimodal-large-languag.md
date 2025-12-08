---
layout: default
title: LoC-Path: Learning to Compress for Pathology Multimodal Large Language Models
---

# LoC-Path: Learning to Compress for Pathology Multimodal Large Language Models
**arXiv**：[2512.05391v1](https://arxiv.org/abs/2512.05391) · [PDF](https://arxiv.org/pdf/2512.05391.pdf)  
**作者**：Qingqiao Hu, Weimin Lyu, Meilong Xu, Kehan Qi, Xiaoling Hu, Saumya Gupta, Jiawei Zhou, Chao Chen  

**一句话要点**：提出LoC-Path框架以降低病理学多模态大语言模型的计算成本

**关键词**：全切片图像理解, 多模态大语言模型, 令牌压缩, 计算效率, 病理学分析

## 3 点简述
- 核心问题：全切片图像理解因像素规模大和诊断相关区域稀疏导致计算成本高。
- 方法要点：设计稀疏令牌合并器和MAE预训练重采样器压缩冗余令牌，结合交叉注意力路由适配器高效集成视觉与语言模型。
- 实验或效果：在性能可比现有方法的同时，显著减少计算和内存需求。

## 摘要（原文）

> Whole Slide Image (WSI) understanding is fundamentally challenging due to its gigapixel scale and the extreme sparsity of diagnostically relevant regions. Unlike human experts who primarily rely on key areas to arrive at a diagnosis, existing slide-level multimodal large language models (MLLMs) for pathology rely on heavy slide-level encoders that process thousands of patch features in a brute-force manner, resulting in excessive computational cost. In this work, we revisit the WSI-language modeling paradigm and show that tile-level features exhibit strong global and local redundancy, whereas only a small subset of tiles are truly task-relevant. Motivated by this observation, we introduce an efficient MLLM framework, called LoC-Path, that replaces the expensive slide-level encoder with redundancy-reducing modules. We first design a Sparse Token Merger (STM) and an MAE-pretrained resampler to remove local redundancy and compress globally redundant tile tokens into a compact slide-level representation set. We then propose a Cross-Attention Routing Adapter (CARA) and a Token Importance Scorer (TIS) to integrate the compressed visual representation with the language model in a computation-efficient manner. Extensive experiments demonstrate that our approach achieves performance comparable to existing state-of-the-art whole-slide MLLMs, while requiring significantly lower computation and memory.

