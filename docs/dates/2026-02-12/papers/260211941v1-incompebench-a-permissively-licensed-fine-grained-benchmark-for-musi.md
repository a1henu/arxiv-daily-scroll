---
layout: default
title: IncompeBench: A Permissively Licensed, Fine-Grained Benchmark for Music Information Retrieval
---

# IncompeBench: A Permissively Licensed, Fine-Grained Benchmark for Music Information Retrieval
**arXiv**：[2602.11941v1](https://arxiv.org/abs/2602.11941) · [PDF](https://arxiv.org/pdf/2602.11941.pdf)  
**作者**：Benjamin Clavié, Atoof Shakir, Jonah Turner, Sean Lee, Aamir Shakir, Makoto P. Kato  

**一句话要点**：提出IncompeBench基准以解决音乐信息检索领域缺乏高质量评估数据集的问题。

**关键词**：音乐信息检索, 基准数据集, 多模态检索, 相关性标注, 许可音乐

## 3 点简述
- 核心问题：音乐信息检索领域缺乏高质量、细粒度的基准数据集，影响模型评估与进展。
- 方法要点：构建包含1,574个许可音乐片段、500个查询和125,000个相关性标注的基准，采用多阶段标注流程确保数据质量。
- 实验或效果：数据集公开可用，标注者间一致性高，支持严格和宽松两种评估模式。

## 摘要（原文）

> Multimodal Information Retrieval has made significant progress in recent years, leveraging the increasingly strong multimodal abilities of deep pre-trained models to represent information across modalities. Music Information Retrieval (MIR), in particular, has considerably increased in quality, with neural representations of music even making its way into everyday life products. However, there is a lack of high-quality benchmarks for evaluating music retrieval performance. To address this issue, we introduce \textbf{IncompeBench}, a carefully annotated benchmark comprising $1,574$ permissively licensed, high-quality music snippets, $500$ diverse queries, and over $125,000$ individual relevance judgements. These annotations were created through the use of a multi-stage pipeline, resulting in high agreement between human annotators and the generated data. The resulting datasets are publicly available at https://huggingface.co/datasets/mixedbread-ai/incompebench-strict and https://huggingface.co/datasets/mixedbread-ai/incompebench-lenient with the prompts available at https://github.com/mixedbread-ai/incompebench-programs.

