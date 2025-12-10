---
layout: default
title: Protein Secondary Structure Prediction Using Transformers
---

# Protein Secondary Structure Prediction Using Transformers
**arXiv**：[2512.08613v1](https://arxiv.org/abs/2512.08613) · [PDF](https://arxiv.org/pdf/2512.08613.pdf)  
**作者**：Manzi Kevin Maxime  

**一句话要点**：提出基于Transformer的模型，利用注意力机制预测蛋白质二级结构，以解决序列到结构映射问题。

**关键词**：蛋白质二级结构预测, Transformer模型, 注意力机制, 滑动窗口数据增强, CB513数据集, 序列泛化

## 3 点简述
- 核心问题：从氨基酸序列预测蛋白质二级结构（如α螺旋、β折叠、卷曲），对理解蛋白质功能至关重要。
- 方法要点：应用Transformer的注意力机制处理蛋白质序列数据，捕捉局部和长程残基相互作用，并采用滑动窗口数据增强技术扩展训练样本。
- 实验或效果：在CB513数据集上，模型展现出对变长序列的强泛化能力，有效预测结构基序。

## 摘要（原文）

> Predicting protein secondary structures such as alpha helices, beta sheets, and coils from amino acid sequences is essential for understanding protein function. This work presents a transformer-based model that applies attention mechanisms to protein sequence data to predict structural motifs. A sliding-window data augmentation technique is used on the CB513 dataset to expand the training samples. The transformer shows strong ability to generalize across variable-length sequences while effectively capturing both local and long-range residue interactions.

