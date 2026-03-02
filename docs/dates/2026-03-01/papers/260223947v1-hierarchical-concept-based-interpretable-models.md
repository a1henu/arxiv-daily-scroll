---
layout: default
title: Hierarchical Concept-based Interpretable Models
---

# Hierarchical Concept-based Interpretable Models
**arXiv**：[2602.23947v1](https://arxiv.org/abs/2602.23947) · [PDF](https://arxiv.org/pdf/2602.23947.pdf)  
**作者**：Oscar Hill, Mateo Espinosa Zarlenga, Mateja Jamnik  

**一句话要点**：提出分层概念嵌入模型以解决概念间关系建模和细粒度概念发现的问题

**关键词**：概念嵌入模型, 分层结构, 概念分割, 可解释性, 细粒度概念, 任务干预

## 3 点简述
- 现代深度神经网络因潜在表示不透明而难以解释，概念嵌入模型通过映射到可解释概念表示来预测任务，但无法建模概念间关系且需要多粒度标注
- 引入分层概念嵌入模型，通过分层结构显式建模概念关系，并提出概念分割方法，从预训练模型嵌入空间自动发现细粒度子概念，无需额外标注
- 评估包括用户研究和PseudoKitchens数据集实验，显示概念分割能发现训练中未见的可解释子概念，分层模型支持多粒度概念干预，提升任务准确性

## 摘要（原文）

> Modern deep neural networks remain challenging to interpret due to the opacity of their latent representations, impeding model understanding, debugging, and debiasing. Concept Embedding Models (CEMs) address this by mapping inputs to human-interpretable concept representations from which tasks can be predicted. Yet, CEMs fail to represent inter-concept relationships and require concept annotations at different granularities during training, limiting their applicability. In this paper, we introduce Hierarchical Concept Embedding Models (HiCEMs), a new family of CEMs that explicitly model concept relationships through hierarchical structures. To enable HiCEMs in real-world settings, we propose Concept Splitting, a method for automatically discovering finer-grained sub-concepts from a pretrained CEM's embedding space without requiring additional annotations. This allows HiCEMs to generate fine-grained explanations from limited concept labels, reducing annotation burdens. Our evaluation across multiple datasets, including a user study and experiments on PseudoKitchens, a newly proposed concept-based dataset of 3D kitchen renders, demonstrates that (1) Concept Splitting discovers human-interpretable sub-concepts absent during training that can be used to train highly accurate HiCEMs, and (2) HiCEMs enable powerful test-time concept interventions at different granularities, leading to improved task accuracy.

