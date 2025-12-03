---
layout: default
title: Q-BERT4Rec: Quantized Semantic-ID Representation Learning for Multimodal Recommendation
---

# Q-BERT4Rec: Quantized Semantic-ID Representation Learning for Multimodal Recommendation
**arXiv**：[2512.02474v1](https://arxiv.org/abs/2512.02474) · [PDF](https://arxiv.org/pdf/2512.02474.pdf)  
**作者**：Haofeng Huang, Ling Gai  

**一句话要点**：提出Q-BERT4Rec，通过量化语义ID表示学习解决多模态序列推荐中的泛化与可解释性问题。

**关键词**：序列推荐, 多模态学习, 语义量化, Transformer模型, 预训练策略, 推荐系统

## 3 点简述
- 核心问题：传统序列推荐方法依赖离散物品ID，缺乏语义信息，忽略多模态数据，导致泛化弱和可解释性差。
- 方法要点：采用三阶段框架，包括跨模态语义注入、语义量化和多掩码预训练，融合文本、视觉和结构特征。
- 实验或效果：在Amazon基准测试中显著优于现有方法，验证了语义量化在多模态序列推荐中的有效性。

## 摘要（原文）

> Sequential recommendation plays a critical role in modern online platforms such as e-commerce, advertising, and content streaming, where accurately predicting users' next interactions is essential for personalization. Recent Transformer-based methods like BERT4Rec have shown strong modeling capability, yet they still rely on discrete item IDs that lack semantic meaning and ignore rich multimodal information (e.g., text and image). This leads to weak generalization and limited interpretability. To address these challenges, we propose Q-Bert4Rec, a multimodal sequential recommendation framework that unifies semantic representation and quantized modeling. Specifically, Q-Bert4Rec consists of three stages: (1) cross-modal semantic injection, which enriches randomly initialized ID embeddings through a dynamic transformer that fuses textual, visual, and structural features; (2) semantic quantization, which discretizes fused representations into meaningful tokens via residual vector quantization; and (3) multi-mask pretraining and fine-tuning, which leverage diverse masking strategies -- span, tail, and multi-region -- to improve sequential understanding. We validate our model on public Amazon benchmarks and demonstrate that Q-Bert4Rec significantly outperforms many strong existing methods, confirming the effectiveness of semantic tokenization for multimodal sequential recommendation. Our source code will be publicly available on GitHub after publishing.

