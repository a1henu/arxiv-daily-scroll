---
layout: default
title: RANGER: Sparsely-Gated Mixture-of-Experts with Adaptive Retrieval Re-ranking for Pathology Report Generation
---

# RANGER: Sparsely-Gated Mixture-of-Experts with Adaptive Retrieval Re-ranking for Pathology Report Generation
**arXiv**：[2603.04348v1](https://arxiv.org/abs/2603.04348) · [PDF](https://arxiv.org/pdf/2603.04348.pdf)  
**作者**：Yixin Chen, Ziyu Su, Hikmat Khan, Muhammad Khalid Khan Niazi  

**一句话要点**：提出RANGER框架，通过稀疏门控专家混合与自适应检索重排序解决病理报告生成中的噪声与专业化不足问题。

**关键词**：病理报告生成, 稀疏门控专家混合, 自适应检索重排序, 全切片图像, 自然语言生成, 知识库整合

## 3 点简述
- 核心问题：病理报告生成任务因全切片图像复杂性和静态知识检索引入噪声而受限。
- 方法要点：集成稀疏门控MoE解码器实现动态专家专业化，并引入自适应检索重排序模块优化知识整合。
- 实验或效果：在PathText-BRCA数据集上验证，RANGER在BLEU、METEOR和ROUGE-L等指标上优于现有方法。

## 摘要（原文）

> Pathology report generation remains a relatively under-explored downstream task, primarily due to the gigapixel scale and complex morphological heterogeneity of Whole Slide Images (WSIs). Existing pathology report generation frameworks typically employ transformer architectures, relying on a homogeneous decoder architecture and static knowledge retrieval integration. Such architectures limit generative specialization and may introduce noisy external guidance during the report generation process. To address these limitations, we propose RANGER, a sparsely-gated Mixture-of-Experts (MoE) framework with adaptive retrieval re-ranking for pathology report generation. Specifically, we integrate a sparsely gated MoE into the decoder, along with noisy top-$k$ routing and load-balancing regularization, to enable dynamic expert specialization across various diagnostic patterns. Additionally, we introduce an adaptive retrieval re-ranking module that selectively refines retrieved memory from a knowledge base before integration, reducing noise and improving semantic alignment based on visual feature representations. We perform extensive experiments on the PathText-BRCA dataset and demonstrate consistent improvements over existing approaches across standard natural language generation metrics. Our full RANGER model achieves optimal performance on PathText dataset, reaching BLEU-1 to BLEU-4 scores of 0.4598, 0.3044, 0.2036, and 0.1435, respectively, with METEOR of 0.1883, and ROUGE-L of 0.3038, validating the effectiveness of dynamic expert routing and adaptive knowledge refinement for semantically grounded pathology report generation.

