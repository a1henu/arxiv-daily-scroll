---
layout: default
title: MRC-GAT: A Meta-Relational Copula-Based Graph Attention Network for Interpretable Multimodal Alzheimer's Disease Diagnosis
---

# MRC-GAT: A Meta-Relational Copula-Based Graph Attention Network for Interpretable Multimodal Alzheimer's Disease Diagnosis
**arXiv**：[2602.15740v1](https://arxiv.org/abs/2602.15740) · [PDF](https://arxiv.org/pdf/2602.15740.pdf)  
**作者**：Fatemeh Khalvandi, Saadat Izadi, Abdolah Chalechale  

**一句话要点**：提出基于元关系Copula的图注意力网络，用于可解释的多模态阿尔茨海默病诊断。

**关键词**：阿尔茨海默病诊断, 图注意力网络, 多模态学习, 元学习, 可解释性

## 3 点简述
- 核心问题：现有图方法依赖固定结构，限制灵活性和泛化能力。
- 方法要点：集成Copula相似性对齐、关系注意力和节点融合，通过元学习处理多模态特征。
- 实验或效果：在TADPOLE和NACC数据集上分别达到96.87%和92.31%的准确率，优于现有模型。

## 摘要（原文）

> Alzheimer's disease (AD) is a progressive neurodegenerative condition necessitating early and precise diagnosis to provide prompt clinical management. Given the paramount importance of early diagnosis, recent studies have increasingly focused on computer-aided diagnostic models to enhance precision and reliability. However, most graph-based approaches still rely on fixed structural designs, which restrict their flexibility and limit generalization across heterogeneous patient data. To overcome these limitations, the Meta-Relational Copula-Based Graph Attention Network (MRC-GAT) is proposed as an efficient multimodal model for AD classification tasks. The proposed architecture, copula-based similarity alignment, relational attention, and node fusion are integrated as the core components of episodic meta-learning, such that the multimodal features, including risk factors (RF), Cognitive test scores, and MRI attributes, are first aligned via a copula-based transformation in a common statistical space and then combined by a multi-relational attention mechanism. According to evaluations performed on the TADPOLE and NACC datasets, the MRC-GAT model achieved accuracies of 96.87% and 92.31%, respectively, demonstrating state-of-the-art performance compared to existing diagnostic models. Finally, the proposed model confirms the robustness and applicability of the proposed method by providing interpretability at various stages of disease diagnosis.

