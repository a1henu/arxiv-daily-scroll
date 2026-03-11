---
layout: default
title: VIVID-Med: LLM-Supervised Structured Pretraining for Deployable Medical ViTs
---

# VIVID-Med: LLM-Supervised Structured Pretraining for Deployable Medical ViTs
**arXiv**：[2603.09109v1](https://arxiv.org/abs/2603.09109) · [PDF](https://arxiv.org/pdf/2603.09109.pdf)  
**作者**：Xiyao Wang, Xiaoyu Tan, Yang Dai, Yuxuan Fu, Shuo Li, Xihe Qiu  

**一句话要点**：提出VIVID-Med框架，利用冻结LLM作为结构化语义教师预训练医疗ViT，以解决临床语义关系捕获不足问题。

**关键词**：医疗视觉预训练, 结构化语义监督, 视觉Transformer, 跨模态泛化, 轻量级部署

## 3 点简述
- 当前医疗视觉预训练方法使用one-hot标签或自由文本，难以有效捕捉复杂临床语义关系。
- VIVID-Med通过统一医疗模式将临床发现转换为JSON字段-状态对，并采用结构化预测分解优化跨注意力机制。
- 在CheXpert线性探测中达到0.8588宏AUC，优于BiomedCLIP 6.65点，且数据使用量减少500倍。

## 摘要（原文）

> Vision-language pretraining has driven significant progress in medical image analysis. However, current methods typically supervise visual encoders using one-hot labels or free-form text, neither of which effectively captures the complex semantic relationships among clinical findings. In this study, we introduce VIVID-Med, a novel framework that leverages a frozen large language model (LLM) as a structured semantic teacher to pretrain medical vision transformers (ViTs). VIVID-Med translates clinical findings into verifiable JSON field-state pairs via a Unified Medical Schema (UMS), utilizing answerability-aware masking to focus optimization. It then employs Structured Prediction Decomposition (SPD) to partition cross-attention into orthogonality-regularized query groups, extracting complementary visual aspects. Crucially, the LLM is discarded post-training, yielding a lightweight, deployable ViT-only backbone. We evaluated VIVID-Med across multiple settings: on CheXpert linear probing, it achieves a macro-AUC of 0.8588, outperforming BiomedCLIP by +6.65 points while using 500x less data. It also demonstrates robust zero-shot cross-domain transfer to NIH ChestX-ray14 (0.7225 macro-AUC) and strong cross-modality generalization to CT, achieving 0.8413 AUC on LIDC-IDRI lung nodule classification and 0.9969 macro-AUC on OrganAMNIST 11-organ classification. VIVID-Med offers a highly efficient, scalable alternative to deploying resource-heavy vision-language models in clinical settings.

