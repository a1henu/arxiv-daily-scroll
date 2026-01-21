---
layout: default
title: Learning to Explain: Supervised Token Attribution from Transformer Attention Patterns
---

# Learning to Explain: Supervised Token Attribution from Transformer Attention Patterns
**arXiv**：[2601.14112v1](https://arxiv.org/abs/2601.14112) · [PDF](https://arxiv.org/pdf/2601.14112.pdf)  
**作者**：George Mihaila  

**一句话要点**：提出Explanation Network以从Transformer注意力模式学习可解释的令牌重要性分数

**关键词**：可解释AI, Transformer注意力, 令牌重要性, 神经网络解释, 跨任务评估

## 3 点简述
- 核心问题：现有注意力解释方法依赖手动规则，模型无关方法计算成本高
- 方法要点：ExpNet通过轻量神经网络自动学习注意力特征到重要性分数的映射
- 实验或效果：在跨任务设置中评估，对比多种模型无关和注意力方法

## 摘要（原文）

> Explainable AI (XAI) has become critical as transformer-based models are deployed in high-stakes applications including healthcare, legal systems, and financial services, where opacity hinders trust and accountability. Transformers self-attention mechanisms have proven valuable for model interpretability, with attention weights successfully used to understand model focus and behavior (Xu et al., 2015); (Wiegreffe and Pinter, 2019). However, existing attention-based explanation methods rely on manually defined aggregation strategies and fixed attribution rules (Abnar and Zuidema, 2020a); (Chefer et al., 2021), while model-agnostic approaches (LIME, SHAP) treat the model as a black box and incur significant computational costs through input perturbation. We introduce Explanation Network (ExpNet), a lightweight neural network that learns an explicit mapping from transformer attention patterns to token-level importance scores. Unlike prior methods, ExpNet discovers optimal attention feature combinations automatically rather than relying on predetermined rules. We evaluate ExpNet in a challenging cross-task setting and benchmark it against a broad spectrum of model-agnostic methods and attention-based techniques spanning four methodological families.

