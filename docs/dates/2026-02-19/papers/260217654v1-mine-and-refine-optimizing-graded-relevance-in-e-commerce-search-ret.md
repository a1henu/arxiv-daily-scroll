---
layout: default
title: Mine and Refine: Optimizing Graded Relevance in E-commerce Search Retrieval
---

# Mine and Refine: Optimizing Graded Relevance in E-commerce Search Retrieval
**arXiv**：[2602.17654v1](https://arxiv.org/abs/2602.17654) · [PDF](https://arxiv.org/pdf/2602.17654.pdf)  
**作者**：Jiaqi Xi, Raghav Saboo, Luming Chen, Martin Wang, Sudeep Das  

**一句话要点**：提出两阶段对比训练框架以优化电商搜索中的分级相关性检索

**关键词**：电商搜索检索, 对比学习, 分级相关性, 语义嵌入, 两阶段训练, 多语言检索

## 3 点简述
- 核心问题：电商搜索需处理长尾噪声查询，并支持分级相关性以稳定混合排序
- 方法要点：先训练全局语义空间，再挖掘难样本并引入多类圆损失细化边界
- 实验或效果：离线评估与线上A/B测试显示检索相关性和业务指标显著提升

## 摘要（原文）

> We propose a two-stage "Mine and Refine" contrastive training framework for semantic text embeddings to enhance multi-category e-commerce search retrieval. Large scale e-commerce search demands embeddings that generalize to long tail, noisy queries while adhering to scalable supervision compatible with product and policy constraints. A practical challenge is that relevance is often graded: users accept substitutes or complements beyond exact matches, and production systems benefit from clear separation of similarity scores across these relevance strata for stable hybrid blending and thresholding. To obtain scalable policy consistent supervision, we fine-tune a lightweight LLM on human annotations under a three-level relevance guideline and further reduce residual noise via engagement driven auditing. In Stage 1, we train a multilingual Siamese two-tower retriever with a label aware supervised contrastive objective that shapes a robust global semantic space. In Stage 2, we mine hard samples via ANN and re-annotate them with the policy aligned LLM, and introduce a multi-class extension of circle loss that explicitly sharpens similarity boundaries between relevance levels, to further refine and enrich the embedding space. Robustness is additionally improved through additive spelling augmentation and synthetic query generation. Extensive offline evaluations and production A/B tests show that our framework improves retrieval relevance and delivers statistically significant gains in engagement and business impact.

