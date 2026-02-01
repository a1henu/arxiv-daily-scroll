---
layout: default
title: Thinking Broad, Acting Fast: Latent Reasoning Distillation from Multi-Perspective Chain-of-Thought for E-Commerce Relevance
---

# Thinking Broad, Acting Fast: Latent Reasoning Distillation from Multi-Perspective Chain-of-Thought for E-Commerce Relevance
**arXiv**：[2601.21611v1](https://arxiv.org/abs/2601.21611) · [PDF](https://arxiv.org/pdf/2601.21611.pdf)  
**作者**：Baopu Qiu, Hao Chen, Yuanrong Wu, Changtong Zan, Chao Wei, Weiru Zhang, Xiaoyi Zeng  

**一句话要点**：提出多视角思维链与潜在推理蒸馏框架，以提升电商搜索相关性建模的准确性与实时性。

**关键词**：电商搜索相关性, 思维链推理, 知识蒸馏, 多视角建模, 实时推理, 大语言模型应用

## 3 点简述
- 核心问题：现有方法依赖单视角思维链推理，无法捕捉电商相关性的多面性，且推理延迟高阻碍实时部署。
- 方法要点：教师模型采用多视角思维链结合监督微调与直接偏好优化，学生模型通过潜在推理知识蒸馏实现高效推理。
- 实验或效果：在日活千万级电商平台进行离线与在线测试，显著提升商业性能与用户体验。

## 摘要（原文）

> Effective relevance modeling is crucial for e-commerce search, as it aligns search results with user intent and enhances customer experience. Recent work has leveraged large language models (LLMs) to address the limitations of traditional relevance models, especially for long-tail and ambiguous queries. By incorporating Chain-of-Thought (CoT) reasoning, these approaches improve both accuracy and interpretability through multi-step reasoning. However, two key limitations remain: (1) most existing approaches rely on single-perspective CoT reasoning, which fails to capture the multifaceted nature of e-commerce relevance (e.g., user intent vs. attribute-level matching vs. business-specific rules); and (2) although CoT-enhanced LLM's offer rich reasoning capabilities, their high inference latency necessitates knowledge distillation for real-time deployment, yet current distillation methods discard the CoT rationale structure at inference, using it as a transient auxiliary signal and forfeiting its reasoning utility. To address these challenges, we propose a novel framework that better exploits CoT semantics throughout the optimization pipeline. Specifically, the teacher model leverages Multi-Perspective CoT (MPCoT) to generate diverse rationales and combines Supervised Fine-Tuning (SFT) with Direct Preference Optimization (DPO) to construct a more robust reasoner. For distillation, we introduce Latent Reasoning Knowledge Distillation (LRKD), which endows a student model with a lightweight inference-time latent reasoning extractor, allowing efficient and low-latency internalization of the LLM's sophisticated reasoning capabilities. Evaluated in offline experiments and online A/B tests on an e-commerce search advertising platform serving tens of millions of users daily, our method delivers significant offline gains, showing clear benefits in both commercial performance and user experience.

