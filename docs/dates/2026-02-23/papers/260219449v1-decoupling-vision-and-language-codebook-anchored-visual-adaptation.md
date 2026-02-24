---
layout: default
title: Decoupling Vision and Language: Codebook Anchored Visual Adaptation
---

# Decoupling Vision and Language: Codebook Anchored Visual Adaptation
**arXiv**：[2602.19449v1](https://arxiv.org/abs/2602.19449) · [PDF](https://arxiv.org/pdf/2602.19449.pdf)  
**作者**：Jason Wu, Tianchen Zhao, Chang Liu, Jiarui Cai, Zheng Zhang, Zhuowei Li, Aaditya Singh, Xiang Xu, Mani Srivastava, Jonathan Wu  

**一句话要点**：提出CRAFT方法，通过离散码本锚定视觉表示，实现大视觉语言模型在领域特定任务中的轻量级适应。

**关键词**：视觉语言模型, 领域适应, 离散码本, 轻量级微调, 视觉编码器, 令牌空间

## 3 点简述
- 核心问题：大视觉语言模型的视觉编码器在领域特定任务中表现不佳，导致错误在语言模型中传播。
- 方法要点：使用离散码本微调编码器，将视觉表示锚定到稳定令牌空间，无需修改模型其他部分。
- 实验或效果：在10个领域特定基准测试中平均提升13.51%，优于基于连续令牌的同类方法。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) use their vision encoders to translate images into representations for downstream reasoning, but the encoders often underperform in domain-specific visual tasks such as medical image diagnosis or fine-grained classification, where representation errors can cascade through the language model, leading to incorrect responses. Existing adaptation methods modify the continuous feature interface between encoder and language model through projector tuning or other parameter-efficient updates, which still couples the two components and requires re-alignment whenever the encoder changes. We introduce CRAFT (Codebook RegulAted Fine-Tuning), a lightweight method that fine-tunes the encoder using a discrete codebook that anchors visual representations to a stable token space, achieving domain adaptation without modifying other parts of the model. This decoupled design allows the adapted encoder to seamlessly boost the performance of LVLMs with different language architectures, as long as they share the same codebook. Empirically, CRAFT achieves an average gain of 13.51% across 10 domain-specific benchmarks such as VQARAD and PlantVillage, while preserving the LLM's linguistic capabilities and outperforming peer methods that operate on continuous tokens.

