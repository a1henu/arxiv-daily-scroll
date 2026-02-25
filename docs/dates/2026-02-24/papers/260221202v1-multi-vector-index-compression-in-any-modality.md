---
layout: default
title: Multi-Vector Index Compression in Any Modality
---

# Multi-Vector Index Compression in Any Modality
**arXiv**：[2602.21202v1](https://arxiv.org/abs/2602.21202) · [PDF](https://arxiv.org/pdf/2602.21202.pdf)  
**作者**：Hanxiang Qin, Alexander Martin, Rohan Jha, Chunsheng Zuo, Reno Kriz, Benjamin Van Durme  

**一句话要点**：提出注意力引导聚类方法，以压缩多向量索引，解决跨模态检索中的计算与存储成本问题。

**关键词**：多模态检索, 索引压缩, 注意力机制, 聚类算法, 跨模态学习, 计算效率

## 3 点简述
- 研究多模态检索中多向量索引的计算与存储成本线性增长问题。
- 引入四种压缩方法，包括新颖的注意力引导聚类，用于在固定向量预算下压缩文档表示。
- 实验表明注意力引导聚类在文本、视觉文档和视频检索任务中优于其他方法，性能接近或优于未压缩索引。

## 摘要（原文）

> We study efficient multi-vector retrieval for late interaction in any modality. Late interaction has emerged as a dominant paradigm for information retrieval in text, images, visual documents, and videos, but its computation and storage costs grow linearly with document length, making it costly for image-, video-, and audio-rich corpora. To address this limitation, we explore query-agnostic methods for compressing multi-vector document representations under a constant vector budget. We introduce four approaches for index compression: sequence resizing, memory tokens, hierarchical pooling, and a novel attention-guided clustering (AGC). AGC uses an attention-guided mechanism to identify the most semantically salient regions of a document as cluster centroids and to weight token aggregation. Evaluating these methods on retrieval tasks spanning text (BEIR), visual-document (ViDoRe), and video (MSR-VTT, MultiVENT 2.0), we show that attention-guided clustering consistently outperforms other parameterized compression methods (sequence resizing and memory tokens), provides greater flexibility in index size than non-parametric hierarchical clustering, and achieves competitive or improved performance compared to a full, uncompressed index. The source code is available at: github.com/hanxiangqin/omni-col-press.

