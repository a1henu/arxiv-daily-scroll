---
layout: default
title: Magic-MM-Embedding: Towards Visual-Token-Efficient Universal Multimodal Embedding with MLLMs
---

# Magic-MM-Embedding: Towards Visual-Token-Efficient Universal Multimodal Embedding with MLLMs
**arXiv**：[2602.05275v1](https://arxiv.org/abs/2602.05275) · [PDF](https://arxiv.org/pdf/2602.05275.pdf)  
**作者**：Qi Li, Yanzhe Zhao, Yongxin Zhou, Yameng Wang, Yandong Yang, Yuanjia Zhou, Jue Wang, Zuojian Wang, Jinxiang Liu  

**一句话要点**：提出Magic-MM-Embedding，通过视觉令牌压缩和多阶段训练，实现高效且高性能的通用多模态嵌入。

**关键词**：多模态大语言模型, 视觉令牌压缩, 多阶段训练, 通用多模态嵌入, 推理效率

## 3 点简述
- 核心问题：MLLMs在通用多模态检索中因视觉令牌处理导致计算成本高，阻碍实际应用。
- 方法要点：采用视觉令牌压缩减少推理延迟和内存占用，结合多阶段渐进训练策略提升性能。
- 实验或效果：模型在实验中大幅超越现有方法，同时推理效率更高。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown immense promise in universal multimodal retrieval, which aims to find relevant items of various modalities for a given query. But their practical application is often hindered by the substantial computational cost incurred from processing a large number of tokens from visual inputs. In this paper, we propose Magic-MM-Embedding, a series of novel models that achieve both high efficiency and state-of-the-art performance in universal multimodal embedding. Our approach is built on two synergistic pillars: (1) a highly efficient MLLM architecture incorporating visual token compression to drastically reduce inference latency and memory footprint, and (2) a multi-stage progressive training strategy designed to not only recover but significantly boost performance. This coarse-to-fine training paradigm begins with extensive continue pretraining to restore multimodal understanding and generation capabilities, progresses to large-scale contrastive pretraining and hard negative mining to enhance discriminative power, and culminates in a task-aware fine-tuning stage guided by an MLLM-as-a-Judge for precise data curation. Comprehensive experiments show that our model outperforms existing methods by a large margin while being more inference-efficient.

