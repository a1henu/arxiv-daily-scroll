---
layout: default
title: LinkedOut: Linking World Knowledge Representation Out of Video LLM for Next-Generation Video Recommendation
---

# LinkedOut: Linking World Knowledge Representation Out of Video LLM for Next-Generation Video Recommendation
**arXiv**：[2512.16891v1](https://arxiv.org/abs/2512.16891) · [PDF](https://arxiv.org/pdf/2512.16891.pdf)  
**作者**：Haichao Zhang, Yao Lu, Lichen Wang, Yunzhe Li, Daiwei Chen, Yunpeng Xu, Yun Fu  

**一句话要点**：提出LinkedOut表示法，从视频中提取VLLM世界知识以支持快速、多视频输入的推荐系统。

**关键词**：视频大语言模型, 世界知识表示, 跨层知识融合, 视频推荐系统, 低延迟推理, 多视频输入

## 3 点简述
- 核心问题：VLLM在视频推荐中面临高延迟、不支持多视频输入和语言输出瓶颈。
- 方法要点：通过可提示查询从原始帧提取语义基础、知识感知的令牌，并引入跨层知识融合MoE选择抽象级别。
- 实验或效果：在标准基准上实现最先进结果，无需手工标签，支持个性化、可解释和低延迟推荐。

## 摘要（原文）

> Video Large Language Models (VLLMs) unlock world-knowledge-aware video understanding through pretraining on internet-scale data and have already shown promise on tasks such as movie analysis and video question answering. However, deploying VLLMs for downstream tasks such as video recommendation remains challenging, since real systems require multi-video inputs, lightweight backbones, low-latency sequential inference, and rapid response. In practice, (1) decode-only generation yields high latency for sequential inference, (2) typical interfaces do not support multi-video inputs, and (3) constraining outputs to language discards fine-grained visual details that matter for downstream vision tasks. We argue that these limitations stem from the absence of a representation that preserves pixel-level detail while leveraging world knowledge. We present LinkedOut, a representation that extracts VLLM world knowledge directly from video to enable fast inference, supports multi-video histories, and removes the language bottleneck. LinkedOut extracts semantically grounded, knowledge-aware tokens from raw frames using VLLMs, guided by promptable queries and optional auxiliary modalities. We introduce a cross-layer knowledge fusion MoE that selects the appropriate level of abstraction from the rich VLLM features, enabling personalized, interpretable, and low-latency recommendation. To our knowledge, LinkedOut is the first VLLM-based video recommendation method that operates on raw frames without handcrafted labels, achieving state-of-the-art results on standard benchmarks. Interpretability studies and ablations confirm the benefits of layer diversity and layer-wise fusion, pointing to a practical path that fully leverages VLLM world-knowledge priors and visual reasoning for downstream vision tasks such as recommendation.

