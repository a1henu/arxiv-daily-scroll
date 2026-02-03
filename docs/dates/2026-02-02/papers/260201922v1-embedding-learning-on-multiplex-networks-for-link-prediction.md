---
layout: default
title: Embedding Learning on Multiplex Networks for Link Prediction
---

# Embedding Learning on Multiplex Networks for Link Prediction
**arXiv**：[2602.01922v1](https://arxiv.org/abs/2602.01922) · [PDF](https://arxiv.org/pdf/2602.01922.pdf)  
**作者**：Orell Trautmann, Olaf Wolkenhauer, Clémence Réda  

**一句话要点**：综述多路网络嵌入学习用于链路预测，提出分类法和公平评估方法

**关键词**：多路网络嵌入, 链路预测, 嵌入学习分类, 公平评估, 知识图谱表示

## 3 点简述
- 核心问题：多路网络复杂性增加，嵌入学习在链路预测中面临挑战
- 方法要点：基于嵌入类型和技术，提出细化分类法以比较模型
- 实验或效果：提出公平测试程序，解决多路网络评估的可重复性和方向性问题

## 摘要（原文）

> Over the past years, embedding learning on networks has shown tremendous results in link prediction tasks for complex systems, with a wide range of real-life applications. Learning a representation for each node in a knowledge graph allows us to capture topological and semantic information, which can be processed in downstream analyses later. In the link prediction task, high-dimensional network information is encoded into low-dimensional vectors, which are then fed to a predictor to infer new connections between nodes in the network. As the network complexity (that is, the numbers of connections and types of interactions) grows, embedding learning turns out increasingly challenging. This review covers published models on embedding learning on multiplex networks for link prediction. First, we propose refined taxonomies to classify and compare models, depending on the type of embeddings and embedding techniques. Second, we review and address the problem of reproducible and fair evaluation of embedding learning on multiplex networks for the link prediction task. Finally, we tackle evaluation on directed multiplex networks by proposing a novel and fair testing procedure. This review constitutes a crucial step towards the development of more performant and tractable embedding learning approaches for multiplex networks and their fair evaluation for the link prediction task. We also suggest guidelines on the evaluation of models, and provide an informed perspective on the challenges and tools currently available to address downstream analyses applied to multiplex networks.

