---
layout: default
title: Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders
---

# Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders
**arXiv**：[2603.06569v1](https://arxiv.org/abs/2603.06569) · [PDF](https://arxiv.org/pdf/2603.06569.pdf)  
**作者**：Boqiang Zhang, Lei Ke, Ruihan Yang, Qi Gao, Tianyuan Qu, Rossell Chen, Dong Yu, Leoweiliang  

**一句话要点**：提出Penguin-VL，基于LLM初始化视觉编码器以提升紧凑VLM性能，适用于资源受限设备。

**关键词**：视觉语言模型, 紧凑模型, 视觉编码器, 细粒度感知, 资源受限部署, 多模态理解

## 3 点简述
- 核心问题：传统VLM依赖对比预训练视觉编码器，抑制细粒度视觉线索，影响密集感知和复杂推理。
- 方法要点：使用文本LLM初始化视觉编码器，解决目标不匹配，提高视觉保真度和数据效率。
- 实验或效果：在图像和视频基准测试中，性能媲美领先VLM，在文档理解等任务中超越，轻量架构实现高效部署。

## 摘要（原文）

> Vision Language Model (VLM) development has largely relied on scaling model size, which hinders deployment on compute-constrained mobile and edge devices such as smartphones and robots. In this work, we explore the performance limits of compact (e.g., 2B and 8B) VLMs. We challenge the prevailing practice that state-of-the-art VLMs must rely on vision encoders initialized via massive contrastive pretraining (e.g., CLIP/SigLIP). We identify an objective mismatch: contrastive learning, optimized for discrimination, enforces coarse and category-level invariances that suppress fine-grained visual cues needed for dense captioning and complex VLM reasoning. To address this issue, we present Penguin-VL, whose vision encoder is initialized from a text-only LLM. Our experiments reveal that Penguin-Encoder serves as a superior alternative to traditional contrastive pretraining, unlocking a higher degree of visual fidelity and data efficiency for multimodal understanding. Across various image and video benchmarks, Penguin-VL achieves performance comparable to leading VLMs (e.g., Qwen3-VL) in mathematical reasoning and surpasses them in tasks such as document understanding, visual knowledge, and multi-perspective video understanding. Notably, these gains are achieved with a lightweight architecture, demonstrating that improved visual representation rather than model scaling is the primary driver of performance. Our ablations show that Penguin-Encoder consistently outperforms contrastive-pretrained encoders, preserving fine-grained spatial and temporal cues that are critical for dense perception and complex reasoning. This makes it a strong drop-in alternative for compute-efficient VLMs and enables high performance in resource-constrained settings. Code: https://github.com/tencent-ailab/Penguin-VL

