---
layout: default
title: Billion-Scale Graph Foundation Models
---

# Billion-Scale Graph Foundation Models
**arXiv**：[2602.04768v1](https://arxiv.org/abs/2602.04768) · [PDF](https://arxiv.org/pdf/2602.04768.pdf)  
**作者**：Maya Bechler-Speicher, Yoel Gottlieb, Andrey Isakov, David Abensur, Ami Tavory, Daniel Haimovich, Ido Guy, Udi Weinsberg  

**一句话要点**：提出GraphBFF框架以构建适用于任意异构十亿级图的图基础模型

**关键词**：图基础模型, 十亿级图, Transformer架构, 神经缩放定律, 零样本学习, 异构图学习

## 3 点简述
- 核心问题：将基础模型范式扩展到通用、真实世界的图数据面临挑战
- 方法要点：设计GraphBFF Transformer架构，提供数据批处理、预训练和微调的具体方法
- 实验或效果：在十亿样本上预训练的14亿参数模型，在未见图的十个下游任务中实现显著零样本和探测性能

## 摘要（原文）

> Graph-structured data underpins many critical applications. While foundation models have transformed language and vision via large-scale pretraining and lightweight adaptation, extending this paradigm to general, real-world graphs is challenging. In this work, we present Graph Billion- Foundation-Fusion (GraphBFF): the first end-to-end recipe for building billion-parameter Graph Foundation Models (GFMs) for arbitrary heterogeneous, billion-scale graphs. Central to the recipe is the GraphBFF Transformer, a flexible and scalable architecture designed for practical billion-scale GFMs. Using the GraphBFF, we present the first neural scaling laws for general graphs and show that loss decreases predictably as either model capacity or training data scales, depending on which factor is the bottleneck. The GraphBFF framework provides concrete methodologies for data batching, pretraining, and fine-tuning for building GFMs at scale. We demonstrate the effectiveness of the framework with an evaluation of a 1.4 billion-parameter GraphBFF Transformer pretrained on one billion samples. Across ten diverse, real-world downstream tasks on graphs unseen during training, spanning node- and link-level classification and regression, GraphBFF achieves remarkable zero-shot and probing performance, including in few-shot settings, with large margins of up to 31 PRAUC points. Finally, we discuss key challenges and open opportunities for making GFMs a practical and principled foundation for graph learning at industrial scale.

