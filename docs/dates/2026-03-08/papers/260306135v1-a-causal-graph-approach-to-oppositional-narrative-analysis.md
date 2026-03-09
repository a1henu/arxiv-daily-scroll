---
layout: default
title: A Causal Graph Approach to Oppositional Narrative Analysis
---

# A Causal Graph Approach to Oppositional Narrative Analysis
**arXiv**：[2603.06135v1](https://arxiv.org/abs/2603.06135) · [PDF](https://arxiv.org/pdf/2603.06135.pdf)  
**作者**：Diego Revilla, Martin Fernandez-de-Retana, Lingfeng Chen, Aritz Bilbao-Jayo, Miguel Fernandez-de-Retana  

**一句话要点**：提出基于因果图的框架以检测和分析对立叙事，通过实体交互图建模结构化交互。

**关键词**：对立叙事分析, 因果图, 实体交互图, 文本分类, 结构化建模

## 3 点简述
- 当前文本分析方法依赖预定义本体标注，易嵌入人类偏见，且未建模实体间结构化交互。
- 方法将叙事表示为实体交互图，结合节点级因果估计，提取最小因果子图以解释分类贡献。
- 分类流程在未知数据集上优于现有对立思维分类方法，具体性能指标未知。

## 摘要（原文）

> Current methods for textual analysis rely on data annotated within predefined ontologies, often embedding human bias within black-box models. Despite achieving near-perfect performance, these approaches exploit unstructured, linear pattern recognition rather than modeling the structured interactions between entities that naturally emerge in discourse. In this work, we propose a graph-based framework for the detection, analysis, and classification of oppositional narratives and their underlying entities by representing narratives as entity-interaction graphs. Moreover, by incorporating causal estimation at the node level, our approach derives a causal representation of each contribution to the final classification by distilling the constructed sentence graph into a minimal causal subgraph. Building upon this representation, we introduce a classification pipeline that outperforms existing approaches to oppositional thinking classification task.

