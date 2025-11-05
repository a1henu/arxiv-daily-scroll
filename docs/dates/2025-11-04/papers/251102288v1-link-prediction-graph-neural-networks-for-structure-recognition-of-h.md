---
layout: default
title: Link prediction Graph Neural Networks for structure recognition of Handwritten Mathematical Expressions
---

# Link prediction Graph Neural Networks for structure recognition of Handwritten Mathematical Expressions
**arXiv**：[2511.02288v1](https://arxiv.org/abs/2511.02288) · [PDF](https://arxiv.org/pdf/2511.02288.pdf)  
**作者**：Cuong Tuan Nguyen, Ngoc Tuan Nguyen, Triet Hoang Minh Dao, Huy Minh Nhat, Huy Truong Dinh  

**一句话要点**：提出基于图神经网络的链接预测方法，用于手写数学表达式的结构识别。

**关键词**：手写数学表达式识别, 图神经网络, 链接预测, 符号分割, 空间关系分类, 符号标签图

## 3 点简述
- 核心问题：手写数学表达式结构识别，需建模符号间空间依赖关系。
- 方法要点：使用BLSTM分割识别符号，GNN链接预测优化图结构。
- 实验或效果：实验显示方法有效，在手写数学表达式结构识别中表现良好。

## 摘要（原文）

> We propose a Graph Neural Network (GNN)-based approach for Handwritten
> Mathematical Expression (HME) recognition by modeling HMEs as graphs, where
> nodes represent symbols and edges capture spatial dependencies. A deep BLSTM
> network is used for symbol segmentation, recognition, and spatial relation
> classification, forming an initial primitive graph. A 2D-CFG parser then
> generates all possible spatial relations, while the GNN-based link prediction
> model refines the structure by removing unnecessary connections, ultimately
> forming the Symbol Label Graph. Experimental results demonstrate the
> effectiveness of our approach, showing promising performance in HME structure
> recognition.

