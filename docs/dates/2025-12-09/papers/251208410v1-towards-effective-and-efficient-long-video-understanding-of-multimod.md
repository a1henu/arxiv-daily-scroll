---
layout: default
title: Towards Effective and Efficient Long Video Understanding of Multimodal Large Language Models via One-shot Clip Retrieval
---

# Towards Effective and Efficient Long Video Understanding of Multimodal Large Language Models via One-shot Clip Retrieval
**arXiv**：[2512.08410v1](https://arxiv.org/abs/2512.08410) · [PDF](https://arxiv.org/pdf/2512.08410.pdf)  
**作者**：Tao Chen, Shaobo Ju, Qiong Wu, Chenxin Fang, Kun Zhang, Jun Peng, Hui Li, Yiyi Zhou, Rongrong Ji  

**一句话要点**：提出OneClip-RAG范式以解决多模态大语言模型处理长视频时内存开销过大的问题

**关键词**：长视频理解, 多模态大语言模型, 检索增强生成, 视频分块算法, 高效计算

## 3 点简述
- 核心问题：多模态大语言模型因内存开销大，只能处理有限帧视频，限制长视频理解能力
- 方法要点：基于单次视频片段检索增强，结合查询引导的视频分块算法，提升知识完整性和语义连贯性
- 实验或效果：在多个MLLMs上验证，显著提升性能，如InternLV2 8B和Qwen2-VL 7B在MLVU基准上达到GPT-4o水平，并在单GPU上高效处理长达一小时视频

## 摘要（原文）

> Due to excessive memory overhead, most Multimodal Large Language Models (MLLMs) can only process videos of limited frames. In this paper, we propose an effective and efficient paradigm to remedy this shortcoming, termed One-shot video-Clip based Retrieval AuGmentation (OneClip-RAG). Compared with existing video RAG methods, OneClip-RAG makes full use of the merits of video clips for augmented video understanding in terms of both knowledge integrity and semantic coherence. Besides, it is also equipped with a novel query-guided video chunking algorithm that can unify clip chunking and cross-modal retrieval in one processing step, avoiding redundant computations. To improve instruction following, we further propose a new dataset called SynLongVideo and design a progressive training regime for OneClip-RAG. OneClip-RAG is plugged into five recent MLLMs and validated on a set of long-video benchmarks. Experimental results not only show the obvious performance gains by OneClip-RAG over MLLMs, e.g., boosting InternLV2 8B and Qwen2-VL 7B to the level of GPT-4o on MLVU, but also show its superior efficiency in handling long videos. e.g., enabling LLaVA-Video understand up to an hour of videos in less than 2.2 minutes on a single 4090 GPU.

