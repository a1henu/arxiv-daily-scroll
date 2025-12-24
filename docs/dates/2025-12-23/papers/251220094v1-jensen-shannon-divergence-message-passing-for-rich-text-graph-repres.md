---
layout: default
title: Jensen-Shannon Divergence Message-Passing for Rich-Text Graph Representation Learning
---

# Jensen-Shannon Divergence Message-Passing for Rich-Text Graph Representation Learning
**arXiv**：[2512.20094v1](https://arxiv.org/abs/2512.20094) · [PDF](https://arxiv.org/pdf/2512.20094.pdf)  
**作者**：Zuo Wang, Ye Yuan  

**一句话要点**：提出Jensen-Shannon散度消息传递范式，以解决富文本图中上下文与结构差异对表示学习的影响。

**关键词**：富文本图表示学习, Jensen-Shannon散度, 消息传递, 图神经网络, 上下文与结构差异

## 3 点简述
- 核心问题：富文本图中广泛存在的上下文与结构差异可能影响表示学习。
- 方法要点：通过Jensen-Shannon散度捕获相似性与相异性，联合计算消息权重，增强相关文本节点的信息传递。
- 实验或效果：在多个基准数据集上，提出的DMPGCN和DMPPRG模型优于现有方法，验证了范式的有效性。

## 摘要（原文）

> In this paper, we investigate how the widely existing contextual and structural divergence may influence the representation learning in rich-text graphs. To this end, we propose Jensen-Shannon Divergence Message-Passing (JSDMP), a new learning paradigm for rich-text graph representation learning. Besides considering similarity regarding structure and text, JSDMP further captures their corresponding dissimilarity by Jensen-Shannon divergence. Similarity and dissimilarity are then jointly used to compute new message weights among text nodes, thus enabling representations to learn with contextual and structural information from truly correlated text nodes. With JSDMP, we propose two novel graph neural networks, namely Divergent message-passing graph convolutional network (DMPGCN) and Divergent message-passing Page-Rank graph neural networks (DMPPRG), for learning representations in rich-text graphs. DMPGCN and DMPPRG have been extensively texted on well-established rich-text datasets and compared with several state-of-the-art baselines. The experimental results show that DMPGCN and DMPPRG can outperform other baselines, demonstrating the effectiveness of the proposed Jensen-Shannon Divergence Message-Passing paradigm

