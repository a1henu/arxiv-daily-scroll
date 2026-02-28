---
layout: default
title: PRIMA: Pre-training with Risk-integrated Image-Metadata Alignment for Medical Diagnosis via LLM
---

# PRIMA: Pre-training with Risk-integrated Image-Metadata Alignment for Medical Diagnosis via LLM
**arXiv**：[2602.23297v1](https://arxiv.org/abs/2602.23297) · [PDF](https://arxiv.org/pdf/2602.23297.pdf)  
**作者**：Yiqing Wang, Chunming He, Ming-Chen Lu, Mercy Pawar, Leslie Niziol, Maria Woodward, Sina Farsiu  

**一句话要点**：提出PRIMA框架，通过风险集成图像-元数据对齐预训练，提升医学诊断的多模态表示学习。

**关键词**：医学诊断, 多模态学习, 预训练框架, 图像-元数据对齐, 风险集成, 鲁棒性

## 3 点简述
- 医学诊断需融合视觉特征与临床元数据，现有方法常将元数据视为孤立标签，忽略其语义知识。
- PRIMA利用RAG构建风险-疾病关联专家语料，优化文本编码器，并采用双编码器预训练策略，通过四种损失函数实现多粒度语义对齐。
- 实验表明PRIMA在疾病分类上显著优于现有方法，无需大量数据或计算资源，具有优越鲁棒性。

## 摘要（原文）

> Medical diagnosis requires the effective synthesis of visual manifestations and clinical metadata. However, existing methods often treat metadata as isolated tags, failing to exploit the rich semantic knowledge embedded in clinical descriptions. We propose PRIMA (Pre-training with Risk-integrated Image-Metadata Alignment), a framework that integrates domain-specific knowledge into multi-modal representation learning. We first curate an expert corpus of risk-disease correlations via Retrieval-Augmented Generation (RAG) to refine Clinical ModernBERT, embedding diagnostic priors into the text encoder. To bridge the modality gap, we introduce a dual-encoder pre-training strategy utilizing DINOv3 and our refined BERT, optimized by a suite of four complementary loss functions. These losses are designed to capture multi-granular semantic alignment and handle the ambiguity of clinical correlations through soft labels. Finally, we leverage Qwen-3 to fuse these aligned features for precise disease classification. Extensive experiments demonstrate that PRIMA effectively harmonizes pixel-level features with abstract clinical expertise, significantly outperforming other state-of-the-art methods. Notably, our framework achieves superior robustness without the need for massive data collection or exhaustive computational resources. Our code will be made public upon acceptance.

