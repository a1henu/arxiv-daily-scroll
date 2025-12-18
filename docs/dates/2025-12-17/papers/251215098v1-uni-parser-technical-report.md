---
layout: default
title: Uni-Parser Technical Report
---

# Uni-Parser Technical Report
**arXiv**：[2512.15098v1](https://arxiv.org/abs/2512.15098) · [PDF](https://arxiv.org/pdf/2512.15098.pdf)  
**作者**：Xi Fang, Haoyi Tao, Shuwen Yang, Suyang Zhong, Haocheng Lu, Han Lyu, Chaozheng Huang, Xinyu Li, Linfeng Zhang, Guolin Ke  

**一句话要点**：提出Uni-Parser工业级文档解析引擎，针对科学文献与专利实现高吞吐、高精度和低成本解析。

**关键词**：文档解析, 多模态对齐, 工业级系统, 科学文献处理, 专利解析, GPU优化

## 3 点简述
- 核心问题：传统流水线方法难以保持跨模态对齐，且扩展性有限。
- 方法要点：采用模块化多专家架构，支持文本、公式、表格等跨模态对齐，易于扩展。
- 实验或效果：在8 x NVIDIA RTX 4090D GPU上达到每秒20页处理速度，支持大规模云部署。

## 摘要（原文）

> This technical report introduces Uni-Parser, an industrial-grade document parsing engine tailored for scientific literature and patents, delivering high throughput, robust accuracy, and cost efficiency. Unlike pipeline-based document parsing methods, Uni-Parser employs a modular, loosely coupled multi-expert architecture that preserves fine-grained cross-modal alignments across text, equations, tables, figures, and chemical structures, while remaining easily extensible to emerging modalities. The system incorporates adaptive GPU load balancing, distributed inference, dynamic module orchestration, and configurable modes that support either holistic or modality-specific parsing. Optimized for large-scale cloud deployment, Uni-Parser achieves a processing rate of up to 20 PDF pages per second on 8 x NVIDIA RTX 4090D GPUs, enabling cost-efficient inference across billions of pages. This level of scalability facilitates a broad spectrum of downstream applications, ranging from literature retrieval and summarization to the extraction of chemical structures, reaction schemes, and bioactivity data, as well as the curation of large-scale corpora for training next-generation large language models and AI4Science models.

