---
layout: default
title: Adaptive Protein Tokenization
---

# Adaptive Protein Tokenization
**arXiv**：[2602.06418v1](https://arxiv.org/abs/2602.06418) · [PDF](https://arxiv.org/pdf/2602.06418.pdf)  
**作者**：Rohit Dilip, Ayush Varshney, David Van Valen  

**一句话要点**：提出自适应蛋白质全局标记化方法，以解决局部标记化在生成和表示任务中的限制。

**关键词**：蛋白质结构标记化, 全局表示, 自适应标记, 生成模型, 表示学习, 零样本任务

## 3 点简述
- 核心问题：现有蛋白质结构标记化方法基于局部邻域信息池化，限制了生成和表示任务的性能。
- 方法要点：采用全局标记化，连续标记逐步增加细节到全局表示，避免序列缩减操作并支持任务自适应。
- 实验或效果：在重建、生成和表示任务中匹配或超越现有模型，提升可设计性并支持零样本蛋白质缩小和亲和力成熟。

## 摘要（原文）

> Tokenization is a promising path to multi-modal models capable of jointly understanding protein sequences, structure, and function. Existing protein structure tokenizers create tokens by pooling information from local neighborhoods, an approach that limits their performance on generative and representation tasks. In this work, we present a method for global tokenization of protein structures in which successive tokens contribute increasing levels of detail to a global representation. This change resolves several issues with generative models based on local protein tokenization: it mitigates error accumulation, provides embeddings without sequence-reduction operations, and allows task-specific adaptation of a tokenized sequence's information content. We validate our method on reconstruction, generative, and representation tasks and demonstrate that it matches or outperforms existing models based on local protein structure tokenizers. We show how adaptive tokens enable inference criteria based on information content, which boosts designability. We validate representations generated from our tokenizer on CATH classification tasks and demonstrate that non-linear probing on our tokenized sequences outperforms equivalent probing on representations from other tokenizers. Finally, we demonstrate how our method supports zero-shot protein shrinking and affinity maturation.

