---
layout: default
title: Prompt Tuning without Labeled Samples for Zero-Shot Node Classification in Text-Attributed Graphs
---

# Prompt Tuning without Labeled Samples for Zero-Shot Node Classification in Text-Attributed Graphs
**arXiv**：[2601.03793v1](https://arxiv.org/abs/2601.03793) · [PDF](https://arxiv.org/pdf/2601.03793.pdf)  
**作者**：Sethupathy Parameswaran, Suresh Sundaram, Yuan Fang  

**一句话要点**：提出零样本提示调优框架以解决文本属性图中无标签节点分类问题

**关键词**：零样本学习, 文本属性图, 节点分类, 提示调优, 双模态生成

## 3 点简述
- 核心问题：文本属性图中零样本节点分类因缺乏标注数据而具挑战性
- 方法要点：利用双模态条件生成器生成合成样本，进行连续提示调优
- 实验或效果：在多个基准数据集上优于现有方法，并通过消融研究验证生成器贡献

## 摘要（原文）

> Node classification is a fundamental problem in information retrieval with many real-world applications, such as community detection in social networks, grouping articles published online and product categorization in e-commerce. Zero-shot node classification in text-attributed graphs (TAGs) presents a significant challenge, particularly due to the absence of labeled data. In this paper, we propose a novel Zero-shot Prompt Tuning (ZPT) framework to address this problem by leveraging a Universal Bimodal Conditional Generator (UBCG). Our approach begins with pre-training a graph-language model to capture both the graph structure and the associated textual descriptions of each node. Following this, a conditional generative model is trained to learn the joint distribution of nodes in both graph and text modalities, enabling the generation of synthetic samples for each class based solely on the class name. These synthetic node and text embeddings are subsequently used to perform continuous prompt tuning, facilitating effective node classification in a zero-shot setting. Furthermore, we conduct extensive experiments on multiple benchmark datasets, demonstrating that our framework performs better than existing state-of-the-art baselines. We also provide ablation studies to validate the contribution of the bimodal generator. The code is provided at: https://github.com/Sethup123/ZPT.

