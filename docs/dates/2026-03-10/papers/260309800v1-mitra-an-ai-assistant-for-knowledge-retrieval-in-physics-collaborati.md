---
layout: default
title: MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations
---

# MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations
**arXiv**：[2603.09800v1](https://arxiv.org/abs/2603.09800) · [PDF](https://arxiv.org/pdf/2603.09800.pdf)  
**作者**：Abhishikth Mallampalli, Sridhara Dasu  

**一句话要点**：提出MITRA系统以解决大型物理合作中内部文档检索的挑战

**关键词**：检索增强生成, 文档检索, 光学字符识别, 向量数据库, 物理分析, 数据隐私

## 3 点简述
- 核心问题：大型科学合作如CMS产生海量内部文档，阻碍知识共享和科研效率。
- 方法要点：基于RAG，采用自动化管道结合Selenium和OCR进行文档检索与文本提取，并部署本地化框架确保数据隐私。
- 实验或效果：通过双层向量数据库架构提升检索性能，在真实查询中优于基于关键词的基线方法。

## 摘要（原文）

> Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significant challenge for both new and experienced researchers, hindering knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a prototype of MITRA, a Retrieval-Augmented Generation (RAG) based system, designed to answer specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline using Selenium for document retrieval from internal databases and Optical Character Recognition (OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA's entire framework, from the embedding model to the Large Language Model (LLM), is hosted on-premise, ensuring that sensitive collaboration data remains private. We introduce a two-tiered vector database architecture that first identifies the relevant analysis from abstracts before focusing on the full documentation, resolving potential ambiguities between different analyses. We demonstrate the prototype's superior retrieval performance against a standard keyword-based baseline on realistic queries and discuss future work towards developing a comprehensive research agent for large experimental collaborations.

