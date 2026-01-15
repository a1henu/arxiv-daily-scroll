---
layout: default
title: Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models
---

# Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models
**arXiv**：[2601.09445v1](https://arxiv.org/abs/2601.09445) · [PDF](https://arxiv.org/pdf/2601.09445.pdf)  
**作者**：Minh Vu Pham, Hsuvas Borkakoty, Yufang Hou  

**一句话要点**：提出基于机制可解释性方法的框架，以定位语言模型预训练中内部知识冲突的编码位置与方式

**关键词**：语言模型, 知识冲突, 机制可解释性, 预训练, 内部表示, 因果干预

## 3 点简述
- 核心问题：语言模型内部参数化知识中同一事件的不一致信息编码导致的知识冲突，其定位问题尚未被探索
- 方法要点：设计基于机制可解释性方法的框架，识别预训练数据中冲突知识在模型内部的编码位置和机制
- 实验或效果：发现特定内部组件负责编码冲突知识，并展示如何因果干预以在推理时控制冲突知识

## 摘要（原文）

> In language models (LMs), intra-memory knowledge conflict largely arises when inconsistent information about the same event is encoded within the model's parametric knowledge. While prior work has primarily focused on resolving conflicts between a model's internal knowledge and external resources through approaches such as fine-tuning or knowledge editing, the problem of localizing conflicts that originate during pre-training within the model's internal representations remain unexplored. In this work, we design a framework based on mechanistic interpretability methods to identify where and how conflicting knowledge from the pre-training data is encoded within LMs. Our findings contribute to a growing body of evidence that specific internal components of a language model are responsible for encoding conflicting knowledge from pre-training, and we demonstrate how mechanistic interpretability methods can be leveraged to causally intervene in and control conflicting knowledge at inference time.

