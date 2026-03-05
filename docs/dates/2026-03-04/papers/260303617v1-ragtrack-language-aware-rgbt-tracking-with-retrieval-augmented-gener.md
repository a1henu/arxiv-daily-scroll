---
layout: default
title: RAGTrack: Language-aware RGBT Tracking with Retrieval-Augmented Generation
---

# RAGTrack: Language-aware RGBT Tracking with Retrieval-Augmented Generation
**arXiv**：[2603.03617v1](https://arxiv.org/abs/2603.03617) · [PDF](https://arxiv.org/pdf/2603.03617.pdf)  
**作者**：Hao Li, Yuhao Wang, Wenning Hao, Pingping Zhang, Dong Wang, Huchuan Lu  

**一句话要点**：提出RAGTrack框架，通过检索增强生成解决RGBT跟踪中语言缺失和模态差异问题。

**关键词**：RGBT跟踪, 检索增强生成, 多模态融合, 语言引导, 自适应令牌融合, 动态知识库

## 3 点简述
- 现有RGBT跟踪器仅依赖初始帧视觉信息，缺乏语言指导，难以适应目标外观变化。
- 引入多模态Transformer编码器和自适应令牌融合，减少搜索冗余和模态差异，提升跟踪鲁棒性。
- 在四个RGBT基准测试中实现最优性能，代码已开源，验证了框架的有效性。

## 摘要（原文）

> RGB-Thermal (RGBT) tracking aims to achieve robust object localization across diverse environmental conditions by fusing visible and thermal infrared modalities. However, existing RGBT trackers rely solely on initial-frame visual information for target modeling, failing to adapt to appearance variations due to the absence of language guidance. Furthermore, current methods suffer from redundant search regions and heterogeneous modality gaps, causing background distraction. To address these issues, we first introduce textual descriptions into RGBT tracking benchmarks. This is accomplished through a pipeline that leverages Multi-modal Large Language Models (MLLMs) to automatically produce texual annotations. Afterwards, we propose RAGTrack, a novel Retrieval-Augmented Generation framework for robust RGBT tracking. To this end, we introduce a Multi-modal Transformer Encoder (MTE) for unified visual-language modeling. Then, we design an Adaptive Token Fusion (ATF) to select target-relevant tokens and perform channel exchanges based on cross-modal correlations, mitigating search redundancies and modality gaps. Finally, we propose a Context-aware Reasoning Module (CRM) to maintain a dynamic knowledge base and employ a Retrieval-Augmented Generation (RAG) to enable temporal linguistic reasoning for robust target modeling. Extensive experiments on four RGBT benchmarks demonstrate that our framework achieves state-of-the-art performance across various challenging scenarios. The source code is available https://github.com/IdolLab/RAGTrack.

