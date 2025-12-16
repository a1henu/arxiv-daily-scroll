---
layout: default
title: Learning to Retrieve with Weakened Labels: Robust Training under Label Noise
---

# Learning to Retrieve with Weakened Labels: Robust Training under Label Noise
**arXiv**：[2512.13237v1](https://arxiv.org/abs/2512.13237) · [PDF](https://arxiv.org/pdf/2512.13237.pdf)  
**作者**：Arnab Sharma  

**一句话要点**：提出标签弱化方法以在标签噪声下训练鲁棒检索模型

**关键词**：密集检索, 标签噪声, 神经编码器, 鲁棒训练, 标签弱化

## 3 点简述
- 核心问题：训练数据稀疏标注和标签噪声阻碍神经编码器在密集检索任务中的训练
- 方法要点：采用标签弱化，基于监督和模型置信度生成一组可能标签，避免强制单一错误标签
- 实验或效果：在四个排名数据集上评估，使用语义感知噪声生成，相比10种先进损失函数提升性能

## 摘要（原文）

> Neural Encoders are frequently used in the NLP domain to perform dense retrieval tasks, for instance, to generate the candidate documents for a given query in question-answering tasks. However, sparse annotation and label noise in the training data make it challenging to train or fine-tune such retrieval models. Although existing works have attempted to mitigate these problems by incorporating modified loss functions or data cleaning, these approaches either require some hyperparameters to tune during training or add substantial complexity to the training setup. In this work, we consider a label weakening approach to generate robust retrieval models in the presence of label noise. Instead of enforcing a single, potentially erroneous label for each query document pair, we allow for a set of plausible labels derived from both the observed supervision and the model's confidence scores. We perform an extensive evaluation considering two retrieval models, one re-ranking model, considering four diverse ranking datasets. To this end, we also consider a realistic noisy setting by using a semantic-aware noise generation technique to generate different ratios of noise. Our initial results show that label weakening can improve the performance of the retrieval tasks in comparison to 10 different state-of-the-art loss functions.

