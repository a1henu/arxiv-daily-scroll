---
layout: default
title: PARL: Position-Aware Relation Learning Network for Document Layout Analysis
---

# PARL: Position-Aware Relation Learning Network for Document Layout Analysis
**arXiv**：[2601.07620v1](https://arxiv.org/abs/2601.07620) · [PDF](https://arxiv.org/pdf/2601.07620.pdf)  
**作者**：Fuyuan Liu, Dianyu Yu, He Ren, Nayu Liu, Xiaomian Kang, Delai Qiu, Fa Zhang, Genpeng Zhen, Shengping Liu, Jiaen Liang, Wei Huang, Yining Wang, Junnan Zhu  

**一句话要点**：提出PARL以解决文档布局分析中依赖OCR导致的错误传播和计算开销问题，通过纯视觉方法建模位置感知关系。

**关键词**：文档布局分析, 纯视觉方法, 位置感知关系学习, 可变形注意力, 图神经网络, OCR-free

## 3 点简述
- 核心问题：现有方法依赖OCR，易传播文本识别错误且计算开销大，限制多模态方法的鲁棒性和实用性。
- 方法要点：引入双向空间位置引导可变形注意力模块嵌入位置依赖，设计图细化分类器通过动态布局图建模上下文关系。
- 实验或效果：在DocLayNet上创视觉方法新基准，在M6Doc上超越多模态模型，参数更少（65M vs 256M），效率更高。

## 摘要（原文）

> Document layout analysis aims to detect and categorize structural elements (e.g., titles, tables, figures) in scanned or digital documents. Popular methods often rely on high-quality Optical Character Recognition (OCR) to merge visual features with extracted text. This dependency introduces two major drawbacks: propagation of text recognition errors and substantial computational overhead, limiting the robustness and practical applicability of multimodal approaches. In contrast to the prevailing multimodal trend, we argue that effective layout analysis depends not on text-visual fusion, but on a deep understanding of documents' intrinsic visual structure. To this end, we propose PARL (Position-Aware Relation Learning Network), a novel OCR-free, vision-only framework that models layout through positional sensitivity and relational structure. Specifically, we first introduce a Bidirectional Spatial Position-Guided Deformable Attention module to embed explicit positional dependencies among layout elements directly into visual features. Second, we design a Graph Refinement Classifier (GRC) to refine predictions by modeling contextual relationships through a dynamically constructed layout graph. Extensive experiments show PARL achieves state-of-the-art results. It establishes a new benchmark for vision-only methods on DocLayNet and, notably, surpasses even strong multimodal models on M6Doc. Crucially, PARL (65M) is highly efficient, using roughly four times fewer parameters than large multimodal models (256M), demonstrating that sophisticated visual structure modeling can be both more efficient and robust than multimodal fusion.

