---
layout: default
title: SOMBRERO: Measuring and Steering Boundary Placement in End-to-End Hierarchical Sequence Models
---

# SOMBRERO: Measuring and Steering Boundary Placement in End-to-End Hierarchical Sequence Models
**arXiv**：[2601.22805v1](https://arxiv.org/abs/2601.22805) · [PDF](https://arxiv.org/pdf/2601.22805.pdf)  
**作者**：Pit Neitemeier, Alessio Serra, Jiaze Li, Sascha Wirges, Lukas Balles, Jan Hendrik Metzen  

**一句话要点**：提出SOMBRERO方法以优化分层序列模型中的边界放置，提升计算效率与预测准确性

**关键词**：分层序列模型, 边界放置优化, 计算效率, 端到端学习, 语言建模, 字节序列压缩

## 3 点简述
- 核心问题：分层序列模型难以量化评估和系统引导边界放置，影响计算效率
- 方法要点：引入边界富集度量B，结合置信对齐边界损失和输入级平滑，引导边界向预测困难位置
- 实验或效果：在1B规模多语种和代码数据上，SOMBRERO改善了准确性与效率的权衡

## 摘要（原文）

> Hierarchical sequence models replace fixed tokenization with learned segmentations that compress long byte sequences for efficient autoregressive modeling. While recent end-to-end methods can learn meaningful boundaries from the language-modeling objective alone, it remains difficult to quantitatively assess and systematically steer where compute is spent. We introduce a router-agnostic metric of boundary quality, boundary enrichment B, which measures how strongly chunk starts concentrate on positions with high next-byte surprisal. Guided by this metric, we propose Sombrero, which steers boundary placement toward predictive difficulty via a confidence-alignment boundary loss and stabilizes boundary learning by applying confidence-weighted smoothing at the input level rather than on realized chunks. On 1B scale, across UTF-8 corpora covering English and German text as well as code and mathematical content, Sombrero improves the accuracy-efficiency trade-off and yields boundaries that more consistently align compute with hard-to-predict positions.

