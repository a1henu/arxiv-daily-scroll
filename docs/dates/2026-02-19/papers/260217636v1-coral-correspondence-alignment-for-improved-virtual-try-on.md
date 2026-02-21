---
layout: default
title: CORAL: Correspondence Alignment for Improved Virtual Try-On
---

# CORAL: Correspondence Alignment for Improved Virtual Try-On
**arXiv**：[2602.17636v1](https://arxiv.org/abs/2602.17636) · [PDF](https://arxiv.org/pdf/2602.17636.pdf)  
**作者**：Jiyoung Kim, Youngjin Shin, Siyoon Jin, Dahyun Chung, Jisu Nam, Tongmin Kim, Jongjae Park, Hyeonwoo Kang, Seungryong Kim  

**一句话要点**：提出CORAL框架以解决虚拟试衣中细节保留问题，通过显式对齐查询-键匹配提升对应关系。

**关键词**：虚拟试衣, 扩散变换器, 对应关系对齐, 注意力机制, 细节保留

## 3 点简述
- 现有虚拟试衣方法在非配对设置下难以保持服装细节，缺乏显式的人-服装对应关系。
- CORAL基于DiT架构，通过全3D注意力分析，引入对应蒸馏损失和熵最小化损失来对齐查询-键匹配。
- 实验表明CORAL在全局形状转移和局部细节保留上优于基线，并提出了基于VLM的评估协议。

## 摘要（原文）

> Existing methods for Virtual Try-On (VTON) often struggle to preserve fine garment details, especially in unpaired settings where accurate person-garment correspondence is required. These methods do not explicitly enforce person-garment alignment and fail to explain how correspondence emerges within Diffusion Transformers (DiTs). In this paper, we first analyze full 3D attention in DiT-based architecture and reveal that the person-garment correspondence critically depends on precise person-garment query-key matching within the full 3D attention. Building on this insight, we then introduce CORrespondence ALignment (CORAL), a DiT-based framework that explicitly aligns query-key matching with robust external correspondences. CORAL integrates two complementary components: a correspondence distillation loss that aligns reliable matches with person-garment attention, and an entropy minimization loss that sharpens the attention distribution. We further propose a VLM-based evaluation protocol to better reflect human preference. CORAL consistently improves over the baseline, enhancing both global shape transfer and local detail preservation. Extensive ablations validate our design choices.

