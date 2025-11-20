---
layout: default
title: Physics-Based Benchmarking Metrics for Multimodal Synthetic Images
---

# Physics-Based Benchmarking Metrics for Multimodal Synthetic Images
**arXiv**：[2511.15204v1](https://arxiv.org/abs/2511.15204) · [PDF](https://arxiv.org/pdf/2511.15204.pdf)  
**作者**：Kishor Datta Gupta, Marufa Kamal, Md. Mahfuzur Rahman, Fahad Rahman, Mohd Ariful Haque, Sunzida Siddique  

**一句话要点**：提出物理约束多模态数据评估指标以解决现有度量在语义和结构准确性上的不足

**关键词**：多模态图像评估, 物理约束推理, 大语言模型集成, 视觉语言模型, 语义准确性度量

## 3 点简述
- 现有度量如BLEU和CLIPScore难以捕捉语义或结构准确性，尤其在领域特定场景
- 方法结合大语言模型与视觉语言模型，通过特征提取、置信加权融合和物理引导推理
- 未知实验效果，但强调对结构约束如对齐和一致性的增强验证

## 摘要（原文）

> Current state of the art measures like BLEU, CIDEr, VQA score, SigLIP-2 and CLIPScore are often unable to capture semantic or structural accuracy, especially for domain-specific or context-dependent scenarios. For this, this paper proposes a Physics-Constrained Multimodal Data Evaluation (PCMDE) metric combining large language models with reasoning, knowledge based mapping and vision-language models to overcome these limitations. The architecture is comprised of three main stages: (1) feature extraction of spatial and semantic information with multimodal features through object detection and VLMs; (2) Confidence-Weighted Component Fusion for adaptive component-level validation; and (3) physics-guided reasoning using large language models for structural and relational constraints (e.g., alignment, position, consistency) enforcement.

