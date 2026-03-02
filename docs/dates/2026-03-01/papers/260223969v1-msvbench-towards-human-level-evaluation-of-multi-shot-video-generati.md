---
layout: default
title: MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation
---

# MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation
**arXiv**：[2602.23969v1](https://arxiv.org/abs/2602.23969) · [PDF](https://arxiv.org/pdf/2602.23969.pdf)  
**作者**：Haoyuan Shi, Yunxin Li, Nanhao Deng, Zhenran Xu, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang  

**一句话要点**：提出MSVBench基准以解决多镜头视频生成评估不足的问题

**关键词**：多镜头视频生成, 视频生成评估, 混合评估框架, 长视频连贯性, 基准数据集

## 3 点简述
- 当前视频生成评估方法局限于单镜头，缺乏多镜头叙事的长程连贯性评估
- 引入MSVBench，结合大模型语义推理与专家模型细粒度感知进行混合评估
- 实验显示现有模型多为视觉插值器，基准与人类判断相关性达94.4%

## 摘要（原文）

> The evolution of video generation toward complex, multi-shot narratives has exposed a critical deficit in current evaluation methods. Existing benchmarks remain anchored to single-shot paradigms, lacking the comprehensive story assets and cross-shot metrics required to assess long-form coherence and appeal. To bridge this gap, we introduce MSVBench, the first comprehensive benchmark featuring hierarchical scripts and reference images tailored for Multi-Shot Video generation. We propose a hybrid evaluation framework that synergizes the high-level semantic reasoning of Large Multimodal Models (LMMs) with the fine-grained perceptual rigor of domain-specific expert models. Evaluating 20 video generation methods across diverse paradigms, we find that current models--despite strong visual fidelity--primarily behave as visual interpolators rather than true world models. We further validate the reliability of our benchmark by demonstrating a state-of-the-art Spearman's rank correlation of 94.4% with human judgments. Finally, MSVBench extends beyond evaluation by providing a scalable supervisory signal. Fine-tuning a lightweight model on its pipeline-refined reasoning traces yields human-aligned performance comparable to commercial models like Gemini-2.5-Flash.

