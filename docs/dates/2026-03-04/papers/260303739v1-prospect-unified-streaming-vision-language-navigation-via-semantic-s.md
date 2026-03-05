---
layout: default
title: PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation
---

# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation
**arXiv**：[2603.03739v1](https://arxiv.org/abs/2603.03739) · [PDF](https://arxiv.org/pdf/2603.03739.pdf)  
**作者**：Zehua Fan, Wenqi Lyu, Wenxuan Song, Linge Zhao, Yifei Yang, Xi Wang, Junjie He, Lida Huang, Haiyan Liu, Bingchuan Sun, Guangjun Bao, Xuanyao Mao, Liang Xu, Yan Wang, Feng Gao  

**一句话要点**：提出PROSPECT，通过语义-空间融合与潜在预测表示实现统一流式视觉语言导航

**关键词**：视觉语言导航, 流式导航, 语义-空间融合, 潜在预测表示, 多模态大语言模型, 机器人部署

## 3 点简述
- 核心问题：MLLMs在零样本端到端VLN中缺乏对环境动态和空间结构的预测建模，影响导航鲁棒性。
- 方法要点：结合流式VLA策略与潜在预测表示学习，使用CUT3R和SigLIP编码器融合语义-空间特征，通过可学习查询令牌预测潜在特征。
- 实验或效果：在VLN-CE基准和真实机器人部署中实现SOTA性能，提升长时程鲁棒性和光照适应性。

## 摘要（原文）

> Multimodal large language models (MLLMs) have advanced zero-shot end-to-end Vision-Language Navigation (VLN), yet robust navigation requires not only semantic understanding but also predictive modeling of environment dynamics and spatial structure. We propose PROSPECT, a unified streaming navigation agent that couples a streaming Vision-Language-Action (VLA) policy with latent predictive representation learning. PROSPECT uses CUT3R as a streaming 3D foundation spatial encoder to produce long-context, absolute-scale spatial features, and fuses them with SigLIP semantic features via cross-attention. During training, we introduce learnable stream query tokens that query the streaming context and predict next-step 2D and 3D latent features (rather than pixels or explicit modalities), supervised in the latent spaces of frozen SigLIP and CUT3R teachers. The predictive branch shapes internal representations without inference overhead. Experiments on VLN-CE benchmarks and real-robot deployment demonstrate state-of-the-art performance and improved long-horizon robustness under diverse lighting. We will release code for the community soon.

