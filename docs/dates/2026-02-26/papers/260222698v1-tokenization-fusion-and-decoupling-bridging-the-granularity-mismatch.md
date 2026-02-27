---
layout: default
title: Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs
---

# Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs
**arXiv**：[2602.22698v1](https://arxiv.org/abs/2602.22698) · [PDF](https://arxiv.org/pdf/2602.22698.pdf)  
**作者**：Siyue Su, Jian Yang, Bo Li, Guanglin Niu  

**一句话要点**：提出KGT框架以解决大语言模型与知识图谱在粒度不匹配问题，实现高效全空间预测。

**关键词**：知识图谱补全, 大语言模型, 粒度不匹配, 实体分词, 特征融合, 解耦预测

## 3 点简述
- 核心问题：大语言模型基于分词序列，知识图谱基于实体单元，粒度不匹配阻碍知识图谱补全。
- 方法要点：通过专用实体分词、关系引导门控融合预训练特征、解耦预测头分离语义与结构推理。
- 实验或效果：在多个基准测试中，KGT一致优于现有最先进方法，验证其有效性。

## 摘要（原文）

> Leveraging Large Language Models (LLMs) for Knowledge Graph Completion (KGC) is promising but hindered by a fundamental granularity mismatch. LLMs operate on fragmented token sequences, whereas entities are the fundamental units in knowledge graphs (KGs) scenarios. Existing approaches typically constrain predictions to limited candidate sets or align entities with the LLM's vocabulary by pooling multiple tokens or decomposing entities into fixed-length token sequences, which fail to capture both the semantic meaning of the text and the structural integrity of the graph. To address this, we propose KGT, a novel framework that uses dedicated entity tokens to enable efficient, full-space prediction. Specifically, we first introduce specialized tokenization to construct feature representations at the level of dedicated entity tokens. We then fuse pre-trained structural and textual features into these unified embeddings via a relation-guided gating mechanism, avoiding training from scratch. Finally, we implement decoupled prediction by leveraging independent heads to separate and combine semantic and structural reasoning. Experimental results show that KGT consistently outperforms state-of-the-art methods across multiple benchmarks.

