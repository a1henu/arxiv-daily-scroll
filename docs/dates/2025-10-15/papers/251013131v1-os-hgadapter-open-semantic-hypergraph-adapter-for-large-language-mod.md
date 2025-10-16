---
layout: default
title: OS-HGAdapter: Open Semantic Hypergraph Adapter for Large Language Models Assisted Entropy-Enhanced Image-Text Alignment
---

# OS-HGAdapter: Open Semantic Hypergraph Adapter for Large Language Models Assisted Entropy-Enhanced Image-Text Alignment
**arXiv**：[2510.13131v1](https://arxiv.org/abs/2510.13131) · [PDF](https://arxiv.org/pdf/2510.13131.pdf)  
**作者**：Rongjun Chen, Chengsi Yao, Jinchang Ren, Xianxian Zeng, Peixian Wang, Jun Yuan, Jiawen Li, Huimin Zhao, Xu Lu  

**一句话要点**：提出OS-HGAdapter，利用LLM增强文本熵和超图适配器解决图文对齐不平衡问题

**关键词**：图文对齐, 跨模态检索, 信息熵增强, 超图适配器, 大语言模型, 语义匹配

## 3 点简述
- 核心问题：图文模态信息熵差异导致跨模态检索不平衡，影响语义对齐性能。
- 方法要点：设计LLM提示模板增强文本多义性，使用超图适配器构建多边连接纠正匹配错误。
- 实验效果：在Flickr30K和MS-COCO基准上，图文检索性能显著提升，达到新SOTA。

## 摘要（原文）

> Text-image alignment constitutes a foundational challenge in multimedia
> content understanding, where effective modeling of cross-modal semantic
> correspondences critically enhances retrieval system performance through joint
> embedding space optimization. Given the inherent difference in information
> entropy between texts and images, conventional approaches often show an
> imbalance in the mutual retrieval of these two modalities. To address this
> particular challenge, we propose to use the open semantic knowledge of Large
> Language Model (LLM) to fill for the entropy gap and reproduce the alignment
> ability of humans in these tasks. Our entropy-enhancing alignment is achieved
> through a two-step process: 1) a new prompt template that does not rely on
> explicit knowledge in the task domain is designed to use LLM to enhance the
> polysemy description of the text modality. By analogy, the information entropy
> of the text modality relative to the visual modality is increased; 2) A
> hypergraph adapter is used to construct multilateral connections between the
> text and image modalities, which can correct the positive and negative matching
> errors for synonymous semantics in the same fixed embedding space, whilst
> reducing the noise caused by open semantic entropy by mapping the reduced
> dimensions back to the original dimensions. Comprehensive evaluations on the
> Flickr30K and MS-COCO benchmarks validate the superiority of our Open Semantic
> Hypergraph Adapter (OS-HGAdapter), showcasing 16.8\% (text-to-image) and 40.1\%
> (image-to-text) cross-modal retrieval gains over existing methods while
> establishing new state-of-the-art performance in semantic alignment tasks.

