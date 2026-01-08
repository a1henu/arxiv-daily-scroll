---
layout: default
title: Learning from Limited Labels: Transductive Graph Label Propagation for Indian Music Analysis
---

# Learning from Limited Labels: Transductive Graph Label Propagation for Indian Music Analysis
**arXiv**：[2601.03626v1](https://arxiv.org/abs/2601.03626) · [PDF](https://arxiv.org/pdf/2601.03626.pdf)  
**作者**：Parampreet Singh, Akshay Raina, Sayeedul Islam Sheikh, Vipul Arora  

**一句话要点**：提出基于标签传播的图半监督学习方法，以解决印度艺术音乐分析中标注数据稀缺的问题。

**关键词**：标签传播, 图半监督学习, 音频分析, 音乐信息检索, 印度艺术音乐

## 3 点简述
- 核心问题：音频和音乐领域缺乏大规模标注数据集，标注成本高且需专业知识。
- 方法要点：构建音频嵌入相似图，在转导半监督设置下传播有限标签信息至未标注数据。
- 实验或效果：应用于拉格识别和乐器分类任务，相比基线方法显著减少标注开销并提升标注质量。

## 摘要（原文）

> Supervised machine learning frameworks rely on extensive labeled datasets for robust performance on real-world tasks. However, there is a lack of large annotated datasets in audio and music domains, as annotating such recordings is resource-intensive, laborious, and often require expert domain knowledge. In this work, we explore the use of label propagation (LP), a graph-based semi-supervised learning technique, for automatically labeling the unlabeled set in an unsupervised manner. By constructing a similarity graph over audio embeddings, we propagate limited label information from a small annotated subset to a larger unlabeled corpus in a transductive, semi-supervised setting. We apply this method to two tasks in Indian Art Music (IAM): Raga identification and Instrument classification. For both these tasks, we integrate multiple public datasets along with additional recordings we acquire from Prasar Bharati Archives to perform LP. Our experiments demonstrate that LP significantly reduces labeling overhead and produces higher-quality annotations compared to conventional baseline methods, including those based on pretrained inductive models. These results highlight the potential of graph-based semi-supervised learning to democratize data annotation and accelerate progress in music information retrieval.

