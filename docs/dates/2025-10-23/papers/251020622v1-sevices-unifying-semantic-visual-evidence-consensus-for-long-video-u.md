---
layout: default
title: SeViCES: Unifying Semantic-Visual Evidence Consensus for Long Video Understanding
---

# SeViCES: Unifying Semantic-Visual Evidence Consensus for Long Video Understanding
**arXiv**：[2510.20622v1](https://arxiv.org/abs/2510.20622) · [PDF](https://arxiv.org/pdf/2510.20622.pdf)  
**作者**：Yuan Sheng, Yanbin Hao, Chenxu Li, Shuo Wang, Xiangnan He  

**一句话要点**：提出SeViCES框架以解决长视频理解中的证据选择问题

**关键词**：长视频理解, 语义-视觉共识, 帧选择, 模型无关方法, 证据融合

## 3 点简述
- 长视频内容复杂多样，现有方法忽略时序依赖或依赖单模态证据
- 引入语义-视觉共识帧选择和答案共识精炼模块，无需训练且模型无关
- 在长视频基准测试中，准确性和鲁棒性优于现有方法

## 摘要（原文）

> Long video understanding remains challenging due to its complex, diverse, and
> temporally scattered content. Although video large language models (Video-LLMs)
> can process videos lasting tens of minutes, applying them to truly long
> sequences is computationally prohibitive and often leads to unfocused or
> inconsistent reasoning. A promising solution is to select only the most
> informative frames, yet existing approaches typically ignore temporal
> dependencies or rely on unimodal evidence, limiting their ability to provide
> complete and query-relevant context. We propose a Semantic-Visual Consensus
> Evidence Selection (SeViCES) framework for effective and reliable long video
> understanding. SeViCES is training-free and model-agnostic, and introduces two
> key components. The Semantic-Visual Consensus Frame Selection (SVCFS) module
> selects frames through (1) a temporal-aware semantic branch that leverages LLM
> reasoning over captions, and (2) a cluster-guided visual branch that aligns
> embeddings with semantic scores via mutual information. The Answer Consensus
> Refinement (ACR) module further resolves inconsistencies between semantic- and
> visual-based predictions by fusing evidence and constraining the answer space.
> Extensive experiments on long video understanding benchmarks show that SeViCES
> consistently outperforms state-of-the-art methods in both accuracy and
> robustness, demonstrating the importance of consensus-driven evidence selection
> for Video-LLMs.

