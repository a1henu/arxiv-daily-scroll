---
layout: default
title: Dual Refinement Cycle Learning: Unsupervised Text Classification of Mamba and Community Detection on Text Attributed Graph
---

# Dual Refinement Cycle Learning: Unsupervised Text Classification of Mamba and Community Detection on Text Attributed Graph
**arXiv**：[2512.07100v1](https://arxiv.org/abs/2512.07100) · [PDF](https://arxiv.org/pdf/2512.07100.pdf)  
**作者**：Hong Wang, Yinglong Zhang, Hanhan Guo, Xuewen Xia, Xing Xu  

**一句话要点**：提出双循环精炼学习框架，以无监督方式整合结构与语义信息于文本属性图。

**关键词**：无监督学习, 文本属性图, 社区检测, 语义建模, 伪标签交换, Mamba分类器

## 3 点简述
- 核心问题：预训练语言模型依赖标注数据，社区检测方法忽略文本语义，限制在文本属性网络中的应用。
- 方法要点：通过GCN社区检测模块与文本语义建模模块的双向循环精炼，迭代交换伪标签，实现无监督整合。
- 实验或效果：在多个数据集上提升社区质量，基于Mamba的分类器达到接近监督模型的准确度，适用于标注稀缺场景。

## 摘要（原文）

> Pretrained language models offer strong text understanding capabilities but remain difficult to deploy in real-world text-attributed networks due to their heavy dependence on labeled data. Meanwhile, community detection methods typically ignore textual semantics, limiting their usefulness in downstream applications such as content organization, recommendation, and risk monitoring. To overcome these limitations, we present Dual Refinement Cycle Learning (DRCL), a fully unsupervised framework designed for practical scenarios where no labels or category definitions are available.
>   DRCL integrates structural and semantic information through a warm-start initialization and a bidirectional refinement cycle between a GCN-based Community Detection Module (GCN-CDM) and a Text Semantic Modeling Module (TSMM). The two modules iteratively exchange pseudo-labels, allowing semantic cues to enhance structural clustering and structural patterns to guide text representation learning without manual supervision.
>   Across several text-attributed graph datasets, DRCL consistently improves the structural and semantic quality of discovered communities. Moreover, a Mamba-based classifier trained solely from DRCL's community signals achieves accuracy comparable to supervised models, demonstrating its potential for deployment in large-scale systems where labeled data are scarce or costly.

