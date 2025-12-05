---
layout: default
title: MASE: Interpretable NLP Models via Model-Agnostic Saliency Estimation
---

# MASE: Interpretable NLP Models via Model-Agnostic Saliency Estimation
**arXiv**：[2512.04386v1](https://arxiv.org/abs/2512.04386) · [PDF](https://arxiv.org/pdf/2512.04386.pdf)  
**作者**：Zhou Yang, Shunyan Luo, Jiazhen Zhu, Fang Jin  

**一句话要点**：提出MASE框架以解决NLP模型可解释性问题，通过模型无关的显著性估计提供局部解释。

**关键词**：自然语言处理, 模型可解释性, 显著性估计, 模型无关方法, 局部解释

## 3 点简述
- 核心问题：深度神经网络在NLP中决策过程不透明，传统方法难以直接应用于离散词数据。
- 方法要点：MASE利用嵌入层的归一化线性高斯扰动，无需模型内部知识，高效估计输入显著性。
- 实验或效果：MASE在Delta Accuracy上优于其他模型无关解释方法，适用于文本模型操作阐明。

## 摘要（原文）

> Deep neural networks (DNNs) have made significant strides in Natural Language Processing (NLP), yet their interpretability remains elusive, particularly when evaluating their intricate decision-making processes. Traditional methods often rely on post-hoc interpretations, such as saliency maps or feature visualization, which might not be directly applicable to the discrete nature of word data in NLP. Addressing this, we introduce the Model-agnostic Saliency Estimation (MASE) framework. MASE offers local explanations for text-based predictive models without necessitating in-depth knowledge of a model's internal architecture. By leveraging Normalized Linear Gaussian Perturbations (NLGP) on the embedding layer instead of raw word inputs, MASE efficiently estimates input saliency. Our results indicate MASE's superiority over other model-agnostic interpretation methods, especially in terms of Delta Accuracy, positioning it as a promising tool for elucidating the operations of text-based models in NLP.

