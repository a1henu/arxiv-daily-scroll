---
layout: default
title: An introductory Generalization of the standard SVMs loss and its applications to Shallow and Deep Neural Networks
---

# An introductory Generalization of the standard SVMs loss and its applications to Shallow and Deep Neural Networks
**arXiv**：[2601.21331v1](https://arxiv.org/abs/2601.21331) · [PDF](https://arxiv.org/pdf/2601.21331.pdf)  
**作者**：Filippo Portera  

**一句话要点**：提出一种新的SVM凸损失函数，用于提升二元分类和回归模型的泛化性能。

**关键词**：SVM损失函数, 凸优化, 泛化性能, 神经网络, 二元分类, 回归模型

## 3 点简述
- 核心问题：标准SVM损失函数可能未充分利用模式相关性，影响泛化能力。
- 方法要点：通过数学推导新凸损失函数，并应用于浅层和深层神经网络。
- 实验或效果：在小数据集上测试，泛化指标不差于标准损失，有时更优。

## 摘要（原文）

> We propose a new convex loss for SVMs, both for the binary classification and for the regression models. Therefore, we show the mathematical derivation of the dual problems and we experiment them with several small data-sets. The minimal dimension of those data-sets is due to the difficult scalability of the SVM method to bigger instances. This preliminary study should prove that using pattern correlations inside the loss function could enhance the generalisation performances. Coherently, results show that generalisation measures are never worse than the standard losses and several times they are better. In our opinion, it should be considered a careful study of this loss, coupled with shallow and deep neural networks. In fact, we present some novel results obtained with those architectures.

