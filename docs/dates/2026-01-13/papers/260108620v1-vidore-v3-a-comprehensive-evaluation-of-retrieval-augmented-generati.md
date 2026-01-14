---
layout: default
title: ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios
---

# ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios
**arXiv**：[2601.08620v1](https://arxiv.org/abs/2601.08620) · [PDF](https://arxiv.org/pdf/2601.08620.pdf)  
**作者**：António Loison, Quentin Macé, Antoine Edy, Victor Xing, Tom Balough, Gabriel Moreira, Bo Liu, Manuel Faysse, Céline Hudelot, Gautier Viaud  

**一句话要点**：提出ViDoRe v3基准以评估复杂现实场景中的检索增强生成系统

**关键词**：检索增强生成, 多模态基准, 视觉文档理解, 源定位, 跨语言评估

## 3 点简述
- 现有基准未能捕捉多模态文档中视觉元素、跨文档合成和源定位的复杂性
- ViDoRe v3包含多类型查询、视觉丰富文档和高质量人工标注，覆盖10个专业领域
- 评估显示视觉检索器优于文本检索器，但模型在非文本元素和细粒度视觉定位方面仍有挑战

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) pipelines must address challenges beyond simple single-document retrieval, such as interpreting visual elements (tables, charts, images), synthesizing information across documents, and providing accurate source grounding. Existing benchmarks fail to capture this complexity, often focusing on textual data, single-document comprehension, or evaluating retrieval and generation in isolation. We introduce ViDoRe v3, a comprehensive multimodal RAG benchmark featuring multi-type queries over visually rich document corpora. It covers 10 datasets across diverse professional domains, comprising ~26,000 document pages paired with 3,099 human-verified queries, each available in 6 languages. Through 12,000 hours of human annotation effort, we provide high-quality annotations for retrieval relevance, bounding box localization, and verified reference answers. Our evaluation of state-of-the-art RAG pipelines reveals that visual retrievers outperform textual ones, late-interaction models and textual reranking substantially improve performance, and hybrid or purely visual contexts enhance answer generation quality. However, current models still struggle with non-textual elements, open-ended queries, and fine-grained visual grounding. To encourage progress in addressing these challenges, the benchmark is released under a commercially permissive license at https://hf.co/vidore.

