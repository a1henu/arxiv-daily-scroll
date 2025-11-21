---
layout: default
title: Beyond Visual Cues: Leveraging General Semantics as Support for Few-Shot Segmentation
---

# Beyond Visual Cues: Leveraging General Semantics as Support for Few-Shot Segmentation
**arXiv**：[2511.16435v1](https://arxiv.org/abs/2511.16435) · [PDF](https://arxiv.org/pdf/2511.16435.pdf)  
**作者**：Jin Wang, Bingfeng Zhang, Jian Pang, Mengyu Liu, Honglong Chen, Weifeng Liu  

**一句话要点**：提出语言驱动属性泛化架构以解决少样本分割中视觉支持偏差问题

**关键词**：少样本分割, 语言驱动属性泛化, 多模态匹配, 大语言模型应用, 跨模态对齐

## 3 点简述
- 核心问题：少样本分割中视觉支持样本因类内变化导致元指导不准确
- 方法要点：利用大语言模型生成多属性描述，通过多模态匹配构建鲁棒支持策略
- 实验或效果：方法在实验中显著优于现有方法，达到新最优性能

## 摘要（原文）

> Few-shot segmentation (FSS) aims to segment novel classes under the guidance of limited support samples by a meta-learning paradigm. Existing methods mainly mine references from support images as meta guidance. However, due to intra-class variations among visual representations, the meta information extracted from support images cannot produce accurate guidance to segment untrained classes. In this paper, we argue that the references from support images may not be essential, the key to the support role is to provide unbiased meta guidance for both trained and untrained classes. We then introduce a Language-Driven Attribute Generalization (LDAG) architecture to utilize inherent target property language descriptions to build robust support strategy. Specifically, to obtain an unbiased support representation, we design a Multi-attribute Enhancement (MaE) module, which produces multiple detailed attribute descriptions of the target class through Large Language Models (LLMs), and then builds refined visual-text prior guidance utilizing multi-modal matching. Meanwhile, due to text-vision modal shift, attribute text struggles to promote visual feature representation, we design a Multi-modal Attribute Alignment (MaA) to achieve cross-modal interaction between attribute texts and visual feature. Experiments show that our proposed method outperforms existing approaches by a clear margin and achieves the new state-of-the art performance. The code will be released.

