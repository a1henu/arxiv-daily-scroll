---
layout: default
title: EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment
---

# EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment
**arXiv**：[2512.14019v1](https://arxiv.org/abs/2512.14019) · [PDF](https://arxiv.org/pdf/2512.14019.pdf)  
**作者**：Juseung Yun, Sunwoo Yu, Sumin Ha, Jonghyun Kim, Janghyeon Lee, Jongseong Jang, Soonyoung Lee  

**一句话要点**：提出EXAONE Path 2.5病理基础模型，通过多组学对齐整合癌症多模态数据以提升肿瘤生物学表征。

**关键词**：病理基础模型, 多组学对齐, 多模态学习, 癌症表征, SigLIP损失, F-RoPE模块

## 3 点简述
- 核心问题：癌症进展涉及形态学和分子层交互，仅图像模型无法捕捉分子信息。
- 方法要点：采用多模态SigLIP损失、F-RoPE模块和领域专用基础模型，实现多组学对齐。
- 实验或效果：在Patho-Bench和内部临床数据集上评估，显示高数据效率和适应性。

## 摘要（原文）

> Cancer progression arises from interactions across multiple biological layers, especially beyond morphological and across molecular layers that remain invisible to image-only models. To capture this broader biological landscape, we present EXAONE Path 2.5, a pathology foundation model that jointly models histologic, genomic, epigenetic and transcriptomic modalities, producing an integrated patient representation that reflects tumor biology more comprehensively. Our approach incorporates three key components: (1) multimodal SigLIP loss enabling all-pairwise contrastive learning across heterogeneous modalities, (2) a fragment-aware rotary positional encoding (F-RoPE) module that preserves spatial structure and tissue-fragment topology in WSI, and (3) domain-specialized internal foundation models for both WSI and RNA-seq to provide biologically grounded embeddings for robust multimodal alignment. We evaluate EXAONE Path 2.5 against six leading pathology foundation models across two complementary benchmarks: an internal real-world clinical dataset and the Patho-Bench benchmark covering 80 tasks. Our framework demonstrates high data and parameter efficiency, achieving on-par performance with state-of-the-art foundation models on Patho-Bench while exhibiting the highest adaptability in the internal clinical setting. These results highlight the value of biologically informed multimodal design and underscore the potential of integrated genotype-to-phenotype modeling for next-generation precision oncology.

