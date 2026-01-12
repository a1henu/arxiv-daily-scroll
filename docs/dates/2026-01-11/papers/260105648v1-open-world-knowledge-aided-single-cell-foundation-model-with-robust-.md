---
layout: default
title: Open World Knowledge Aided Single-Cell Foundation Model with Robust Cross-Modal Cell-Language Pre-training
---

# Open World Knowledge Aided Single-Cell Foundation Model with Robust Cross-Modal Cell-Language Pre-training
**arXiv**：[2601.05648v1](https://arxiv.org/abs/2601.05648) · [PDF](https://arxiv.org/pdf/2601.05648.pdf)  
**作者**：Haoran Wang, Xuanyi Zhang, Shuangsang Fang, Longke Ran, Ziqing Deng, Yong Zhang, Yuxiang Li, Shaoshuai Li  

**一句话要点**：提出OKR-CELL模型，通过开放世界知识增强和跨模态鲁棒对齐，提升单细胞基础模型的性能与抗噪能力。

**关键词**：单细胞多组学, 跨模态预训练, 检索增强生成, 鲁棒对齐, 细胞类型注释, 零样本学习

## 3 点简述
- 核心问题：单细胞基础模型在整合深度个体谱系和处理多模态数据噪声方面存在不足。
- 方法要点：利用LLM和RAG丰富细胞文本描述，设计跨模态鲁棒对齐目标以增强抗噪性。
- 实验或效果：在32M细胞-文本对上预训练后，在6个评估任务中取得先进结果，包括零样本细胞类型注释。

## 摘要（原文）

> Recent advancements in single-cell multi-omics, particularly RNA-seq, have provided profound insights into cellular heterogeneity and gene regulation. While pre-trained language model (PLM) paradigm based single-cell foundation models have shown promise, they remain constrained by insufficient integration of in-depth individual profiles and neglecting the influence of noise within multi-modal data. To address both issues, we propose an Open-world Language Knowledge-Aided Robust Single-Cell Foundation Model (OKR-CELL). It is built based on a cross-modal Cell-Language pre-training framework, which comprises two key innovations: (1) leveraging Large Language Models (LLMs) based workflow with retrieval-augmented generation (RAG) enriches cell textual descriptions using open-world knowledge; (2) devising a Cross-modal Robust Alignment (CRA) objective that incorporates sample reliability assessment, curriculum learning, and coupled momentum contrastive learning to strengthen the model's resistance to noisy data. After pretraining on 32M cell-text pairs, OKR-CELL obtains cutting-edge results across 6 evaluation tasks. Beyond standard benchmarks such as cell clustering, cell-type annotation, batch-effect correction, and few-shot annotation, the model also demonstrates superior performance in broader multi-modal applications, including zero-shot cell-type annotation and bidirectional cell-text retrieval.

