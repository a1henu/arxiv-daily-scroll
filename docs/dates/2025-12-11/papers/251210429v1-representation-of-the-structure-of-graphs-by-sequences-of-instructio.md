---
layout: default
title: Representation of the structure of graphs by sequences of instructions
---

# Representation of the structure of graphs by sequences of instructions
**arXiv**：[2512.10429v1](https://arxiv.org/abs/2512.10429) · [PDF](https://arxiv.org/pdf/2512.10429.pdf)  
**作者**：Ezequiel Lopez-Rubio  

**一句话要点**：提出基于指令序列的图表示方法，以适配深度学习语言模型处理图结构。

**关键词**：图表示, 邻接矩阵转换, 指令序列, 深度学习语言模型, 图处理

## 3 点简述
- 核心问题：传统图表示（如邻接矩阵）不适用于深度学习语言模型处理文本的特性。
- 方法要点：将邻接矩阵转换为可逆的指令序列，逐步构建矩阵，保持图局部结构模式。
- 实验或效果：初步计算实验显示有利结果，有望提升深度学习模型对图的处理能力。

## 摘要（原文）

> The representation of graphs is commonly based on the adjacency matrix concept. This formulation is the foundation of most algebraic and computational approaches to graph processing. The advent of deep learning language models offers a wide range of powerful computational models that are specialized in the processing of text. However, current procedures to represent graphs are not amenable to processing by these models. In this work, a new method to represent graphs is proposed. It represents the adjacency matrix of a graph by a string of simple instructions. The instructions build the adjacency matrix step by step. The transformation is reversible, i.e. given a graph the string can be produced and vice versa. The proposed representation is compact and it maintains the local structural patterns of the graph. Therefore, it is envisaged that it could be useful to boost the processing of graphs by deep learning models. A tentative computational experiment is reported, with favorable results.

