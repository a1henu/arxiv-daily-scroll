---
layout: default
title: Beyond Patch Aggregation: 3-Pass Pyramid Indexing for Vision-Enhanced Document Retrieval
---

# Beyond Patch Aggregation: 3-Pass Pyramid Indexing for Vision-Enhanced Document Retrieval
**arXiv**：[2511.21121v1](https://arxiv.org/abs/2511.21121) · [PDF](https://arxiv.org/pdf/2511.21121.pdf)  
**作者**：Anup Roy, Rishabh Gyanendra Upadhyay, Animesh Rameshbhai Panara, Robin Mills  

**一句话要点**：提出VisionRAG系统以解决视觉增强文档检索中的内存开销和模型依赖问题

**关键词**：视觉增强检索, 金字塔索引, 多模态系统, 文档图像处理, OCR自由方法

## 3 点简述
- 传统文档检索依赖OCR和启发式分块，易受布局变化影响且丢失空间线索
- 采用三遍金字塔索引框架，生成全局页面摘要、节标题等轻量级向量进行检索
- 在金融文档基准测试中，FinanceBench准确率达0.8051，TAT DQA召回率达0.9629

## 摘要（原文）

> Document centric RAG pipelines usually begin with OCR, followed by brittle heuristics for chunking, table parsing, and layout reconstruction. These text first workflows are costly to maintain, sensitive to small layout shifts, and often lose the spatial cues that contain the answer. Vision first retrieval has emerged as a strong alternative. By operating directly on page images, systems like ColPali and ColQwen preserve structure and reduce pipeline complexity while achieving strong benchmark performance. However, these late interaction models tie retrieval to a specific vision backbone and require storing hundreds of patch embeddings per page, creating high memory overhead and complicating large scale deployment.
>   We introduce VisionRAG, a multimodal retrieval system that is OCR free and model agnostic. VisionRAG indexes documents directly as images, preserving layout, tables, and spatial cues, and builds semantic vectors without committing to a specific extraction. Our three pass pyramid indexing framework creates vectors using global page summaries, section headers, visual hotspots, and fact level cues. These summaries act as lightweight retrieval surrogates. At query time, VisionRAG retrieves the most relevant pages using the pyramid index, then forwards the raw page image encoded as base64 to a multimodal LLM for final question answering. During retrieval, reciprocal rank fusion integrates signals across the pyramid to produce robust ranking.
>   VisionRAG stores only 17 to 27 vectors per page, matching the efficiency of patch based methods while staying flexible across multimodal encoders. On financial document benchmarks, it achieves 0.8051 accuracy at 10 on FinanceBench and 0.9629 recall at 100 on TAT DQA. These results show that OCR free, summary guided multimodal retrieval is a practical and scalable alternative to traditional text extraction pipelines.

