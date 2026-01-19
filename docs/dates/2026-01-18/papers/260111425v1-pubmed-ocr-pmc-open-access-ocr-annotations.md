---
layout: default
title: PubMed-OCR: PMC Open Access OCR Annotations
---

# PubMed-OCR: PMC Open Access OCR Annotations
**arXiv**：[2601.11425v1](https://arxiv.org/abs/2601.11425) · [PDF](https://arxiv.org/pdf/2601.11425.pdf)  
**作者**：Hunter Heidenreich, Yosheb Getachew, Olivia Dinica, Ben Elliott  

**一句话要点**：提出PubMed-OCR数据集以支持科学文献的OCR相关建模与评估

**关键词**：OCR数据集, 科学文献处理, 布局感知建模, 坐标基础问答, PubMed Central, 边界框标注

## 3 点简述
- 核心问题：缺乏大规模、标注精细的科学文献OCR数据集，限制布局感知模型和OCR依赖流程的研究。
- 方法要点：基于PubMed Central开放获取PDF，使用Google Cloud Vision进行OCR标注，提供词、行、段落级边界框的紧凑JSON格式。
- 实验或效果：数据集包含209.5K文章（1.5M页，约13亿词），分析期刊覆盖和布局特征，并讨论单OCR引擎依赖和启发式行重建等局限性。

## 摘要（原文）

> PubMed-OCR is an OCR-centric corpus of scientific articles derived from PubMed Central Open Access PDFs. Each page image is annotated with Google Cloud Vision and released in a compact JSON schema with word-, line-, and paragraph-level bounding boxes. The corpus spans 209.5K articles (1.5M pages; ~1.3B words) and supports layout-aware modeling, coordinate-grounded QA, and evaluation of OCR-dependent pipelines. We analyze corpus characteristics (e.g., journal coverage and detected layout features) and discuss limitations, including reliance on a single OCR engine and heuristic line reconstruction. We release the data and schema to facilitate downstream research and invite extensions.

