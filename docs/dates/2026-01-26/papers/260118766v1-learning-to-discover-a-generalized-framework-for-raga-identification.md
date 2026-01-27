---
layout: default
title: Learning to Discover: A Generalized Framework for Raga Identification without Forgetting
---

# Learning to Discover: A Generalized Framework for Raga Identification without Forgetting
**arXiv**：[2601.18766v1](https://arxiv.org/abs/2601.18766) · [PDF](https://arxiv.org/pdf/2601.18766.pdf)  
**作者**：Parampreet Singh, Somya Kumar, Chaitanya Shailendra Nitawe, Vipul Arora  

**一句话要点**：提出统一学习框架以解决印度艺术音乐拉格识别中未见拉格的发现与灾难性遗忘问题

**关键词**：拉格识别, 灾难性遗忘, 统一学习框架, 未见类别发现, 印度艺术音乐, 表示学习

## 3 点简述
- 核心问题：印度艺术音乐拉格识别因训练数据缺乏罕见拉格，传统分类模型无法处理未见类别且易遗忘已知知识。
- 方法要点：采用统一学习框架，结合有标签和无标签音频，使模型能发现未见拉格的连贯类别并保留已知拉格知识。
- 实验或效果：在基准数据集上测试，模型在已知、未见及所有拉格类别分类中表现优异，超越先前NCD方法。

## 摘要（原文）

> Raga identification in Indian Art Music (IAM) remains challenging due to the presence of numerous rarely performed Ragas that are not represented in available training datasets. Traditional classification models struggle in this setting, as they assume a closed set of known categories and therefore fail to recognise or meaningfully group previously unseen Ragas. Recent works have tried categorizing unseen Ragas, but they run into a problem of catastrophic forgetting, where the knowledge of previously seen Ragas is diminished. To address this problem, we adopt a unified learning framework that leverages both labeled and unlabeled audio, enabling the model to discover coherent categories corresponding to the unseen Ragas, while retaining the knowledge of previously known ones. We test our model on benchmark Raga Identification datasets and demonstrate its performance in categorizing previously seen, unseen, and all Raga classes. The proposed approach surpasses the previous NCD-based pipeline even in discovering the unseen Raga categories, offering new insights into representation learning for IAM tasks.

