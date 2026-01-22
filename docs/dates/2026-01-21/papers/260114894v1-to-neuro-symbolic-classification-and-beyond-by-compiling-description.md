---
layout: default
title: To Neuro-Symbolic Classification and Beyond by Compiling Description Logic Ontologies to Probabilistic Circuits
---

# To Neuro-Symbolic Classification and Beyond by Compiling Description Logic Ontologies to Probabilistic Circuits
**arXiv**：[2601.14894v1](https://arxiv.org/abs/2601.14894) · [PDF](https://arxiv.org/pdf/2601.14894.pdf)  
**作者**：Nicolas Lazzari, Valentina Presutti, Antonio Vergari  

**一句话要点**：提出编译描述逻辑本体为概率电路的方法，以增强神经符号分类的可靠性和可扩展性。

**关键词**：神经符号分类, 描述逻辑本体, 概率电路, 可微推理, 知识表示, 深度学习集成

## 3 点简述
- 核心问题：神经符号方法缺乏对描述逻辑本体的原生支持，限制了分类器与领域知识的整合。
- 方法要点：将描述逻辑本体编码为可微电路，支持高效推理和神经符号模型构建。
- 实验或效果：电路生成的数据集挑战性强，推理速度提升三个数量级，分类器预测一致性优于基线。

## 摘要（原文）

> Background: Neuro-symbolic methods enhance the reliability of neural network classifiers through logical constraints, but they lack native support for ontologies.
>   Objectives: We aim to develop a neuro-symbolic method that reliably outputs predictions consistent with a Description Logic ontology that formalizes domain-specific knowledge.
>   Methods: We encode a Description Logic ontology as a circuit, a feed-forward differentiable computational graph that supports tractable execution of queries and transformations. We show that the circuit can be used to (i) generate synthetic datasets that capture the semantics of the ontology; (ii) efficiently perform deductive reasoning on a GPU; (iii) implement neuro-symbolic models whose predictions are approximately or provably consistent with the knowledge defined in the ontology.
>   Results We show that the synthetic dataset generated using the circuit qualitatively captures the semantics of the ontology while being challenging for Machine Learning classifiers, including neural networks. Moreover, we show that compiling the ontology into a circuit is a promising approach for scalable deductive reasoning, with runtimes up to three orders of magnitude faster than available reasoners. Finally, we show that our neuro-symbolic classifiers reliably produce consistent predictions when compared to neural network baselines, maintaining competitive performances or even outperforming them.
>   Conclusions By compiling Description Logic ontologies into circuits, we obtain a tighter integration between the Deep Learning and Knowledge Representation fields. We show that a single circuit representation can be used to tackle different challenging tasks closely related to real-world applications.

