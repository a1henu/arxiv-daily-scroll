---
layout: default
title: What You Read is What You Classify: Highlighting Attributions to Text and Text-Like Inputs
---

# What You Read is What You Classify: Highlighting Attributions to Text and Text-Like Inputs
**arXiv**：[2602.24149v1](https://arxiv.org/abs/2602.24149) · [PDF](https://arxiv.org/pdf/2602.24149.pdf)  
**作者**：Daniel S. Berman, Brian Merritt, Stanley Ta, Dana Udwin, Amanda Ernlund, Jeremy Ratcliff, Vijay Narayan  

**一句话要点**：提出基于掩码的可解释AI方法，用于文本和类文本输入的分类器解释，聚焦于整体令牌重要性。

**关键词**：可解释人工智能, 文本分类, 令牌序列, 掩码解释, 嵌入层, 核苷酸序列

## 3 点简述
- 核心问题：现有可解释AI方法不适用于离散令牌输入，如文本，常导致重要性分配不当。
- 方法要点：通过训练解释器网络生成掩码，隐藏分类无关信息，保持嵌入向量方向不变以评估令牌整体重要性。
- 实验或效果：应用于核苷酸序列分类器，验证掩码段对分类相关性较低，生成人类可读解释。

## 摘要（原文）

> At present, there are no easily understood explainable artificial intelligence (AI) methods for discrete token inputs, like text. Most explainable AI techniques do not extend well to token sequences, where both local and global features matter, because state-of-the-art models, like transformers, tend to focus on global connections. Therefore, existing explainable AI algorithms fail by (i) identifying disparate tokens of importance, or (ii) assigning a large number of tokens a low value of importance. This method for explainable AI for tokens-based classifiers generalizes a mask-based explainable AI algorithm for images. It starts with an Explainer neural network that is trained to create masks to hide information not relevant for classification. Then, the Hadamard product of the mask and the continuous values of the classifier's embedding layer is taken and passed through the classifier, changing the magnitude of the embedding vector but keeping the orientation unchanged. The Explainer is trained for a taxonomic classifier for nucleotide sequences and it is shown that the masked segments are less relevant to classification than the unmasked ones. This method focused on the importance the token as a whole (i.e., a segment of the input sequence), producing a human-readable explanation.

