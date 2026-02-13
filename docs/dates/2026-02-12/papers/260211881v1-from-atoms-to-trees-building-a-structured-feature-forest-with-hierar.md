---
layout: default
title: From Atoms to Trees: Building a Structured Feature Forest with Hierarchical Sparse Autoencoders
---

# From Atoms to Trees: Building a Structured Feature Forest with Hierarchical Sparse Autoencoders
**arXiv**：[2602.11881v1](https://arxiv.org/abs/2602.11881) · [PDF](https://arxiv.org/pdf/2602.11881.pdf)  
**作者**：Yifan Luo, Yang Zhan, Jiedong Jiang, Tianyang Liu, Mingrui Wu, Zhennan Zhou, Bin Dong  

**一句话要点**：提出分层稀疏自编码器以从大语言模型中提取层次化特征结构

**关键词**：稀疏自编码器, 特征层次, 大语言模型, 结构学习, 可解释性

## 3 点简述
- 稀疏自编码器提取孤立特征，但大语言模型隐含自然语言的层次结构
- HSAE联合学习多个稀疏自编码器及其特征间的父子关系，通过结构约束损失和随机扰动增强对齐
- 实验表明HSAE能恢复语义层次，保持重构保真度和可解释性

## 摘要（原文）

> Sparse autoencoders (SAEs) have proven effective for extracting monosemantic features from large language models (LLMs), yet these features are typically identified in isolation. However, broad evidence suggests that LLMs capture the intrinsic structure of natural language, where the phenomenon of "feature splitting" in particular indicates that such structure is hierarchical. To capture this, we propose the Hierarchical Sparse Autoencoder (HSAE), which jointly learns a series of SAEs and the parent-child relationships between their features. HSAE strengthens the alignment between parent and child features through two novel mechanisms: a structural constraint loss and a random feature perturbation mechanism. Extensive experiments across various LLMs and layers demonstrate that HSAE consistently recovers semantically meaningful hierarchies, supported by both qualitative case studies and rigorous quantitative metrics. At the same time, HSAE preserves the reconstruction fidelity and interpretability of standard SAEs across different dictionary sizes. Our work provides a powerful, scalable tool for discovering and analyzing the multi-scale conceptual structures embedded in LLM representations.

