---
layout: default
title: Formally Explaining Decision Tree Models with Answer Set Programming
---

# Formally Explaining Decision Tree Models with Answer Set Programming
**arXiv**：[2601.03845v1](https://arxiv.org/abs/2601.03845) · [PDF](https://arxiv.org/pdf/2601.03845.pdf)  
**作者**：Akihiro Takemura, Masayuki Otani, Katsumi Inoue  

**一句话要点**：提出基于答案集编程的方法，为决策树模型生成形式化解释以增强可解释性。

**关键词**：决策树解释, 答案集编程, 形式化推理, 可解释机器学习, 模型验证

## 3 点简述
- 核心问题：决策树模型结构复杂，在安全关键应用中难以提供形式化决策依据。
- 方法要点：利用答案集编程生成充分、对比、多数和树特定解释，支持用户偏好编码和全枚举。
- 实验或效果：在多样化数据集上评估，与现有方法比较展示有效性和局限性。

## 摘要（原文）

> Decision tree models, including random forests and gradient-boosted decision trees, are widely used in machine learning due to their high predictive performance.  However, their complex structures often make them difficult to interpret, especially in safety-critical applications where model decisions require formal justification.  Recent work has demonstrated that logical and abductive explanations can be derived through automated reasoning techniques.  In this paper, we propose a method for generating various types of explanations, namely, sufficient, contrastive, majority, and tree-specific explanations, using Answer Set Programming (ASP).  Compared to SAT-based approaches, our ASP-based method offers greater flexibility in encoding user preferences and supports enumeration of all possible explanations.  We empirically evaluate the approach on a diverse set of datasets and demonstrate its effectiveness and limitations compared to existing methods.

