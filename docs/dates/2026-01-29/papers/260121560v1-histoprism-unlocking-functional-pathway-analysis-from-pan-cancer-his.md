---
layout: default
title: HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction
---

# HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction
**arXiv**：[2601.21560v1](https://arxiv.org/abs/2601.21560) · [PDF](https://arxiv.org/pdf/2601.21560.pdf)  
**作者**：Susu Hu, Qinghe Zeng, Nithya Bhasker, Jakob Nicolas Kather, Stefanie Speidel  

**一句话要点**：提出HistoPrism以从全癌种组织学预测基因表达，实现功能通路分析

**关键词**：基因表达预测, 全癌种组织学, 功能通路分析, Transformer架构, 临床转录组建模

## 3 点简述
- 核心问题：现有方法局限于单癌种和基于方差的评估，功能相关性不足
- 方法要点：基于Transformer的高效架构，支持全癌种基因表达预测
- 实验或效果：在通路级预测上显著提升，展示生物一致性转录组模式恢复能力

## 摘要（原文）

> Predicting spatial gene expression from H&E histology offers a scalable and clinically accessible alternative to sequencing, but realizing clinical impact requires models that generalize across cancer types and capture biologically coherent signals. Prior work is often limited to per-cancer settings and variance-based evaluation, leaving functional relevance underexplored. We introduce HistoPrism, an efficient transformer-based architecture for pan-cancer prediction of gene expression from histology. To evaluate biological meaning, we introduce a pathway-level benchmark, shifting assessment from isolated gene-level variance to coherent functional pathways. HistoPrism not only surpasses prior state-of-the-art models on highly variable genes , but also more importantly, achieves substantial gains on pathway-level prediction, demonstrating its ability to recover biologically coherent transcriptomic patterns. With strong pan-cancer generalization and improved efficiency, HistoPrism establishes a new standard for clinically relevant transcriptomic modeling from routinely available histology.

