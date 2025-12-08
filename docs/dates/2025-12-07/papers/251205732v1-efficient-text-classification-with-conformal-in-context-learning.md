---
layout: default
title: Efficient Text Classification with Conformal In-Context Learning
---

# Efficient Text Classification with Conformal In-Context Learning
**arXiv**：[2512.05732v1](https://arxiv.org/abs/2512.05732) · [PDF](https://arxiv.org/pdf/2512.05732.pdf)  
**作者**：Ippokratis Pantelidis, Korbinian Randl, Aron Henriksson  

**一句话要点**：提出CICLe框架以高效文本分类，结合轻量分类器与Conformal Prediction指导LLM提示。

**关键词**：文本分类, Conformal Prediction, 大语言模型, 提示工程, 计算效率, 类别不平衡

## 3 点简述
- 核心问题：LLM在文本分类中依赖提示设计且计算成本高，CICLe旨在提升效率与适用性。
- 方法要点：集成轻量基分类器与Conformal Prediction，自适应减少候选类别以优化LLM提示。
- 实验或效果：在多样NLP基准上评估，CICLe提升基分类器性能，减少提示长度与样本数，尤其适用于类别不平衡任务。

## 摘要（原文）

> Large Language Models (LLMs) demonstrate strong in-context learning abilities, yet their effectiveness in text classification depends heavily on prompt design and incurs substantial computational cost. Conformal In-Context Learning (CICLe) has been proposed as a resource-efficient framework that integrates a lightweight base classifier with Conformal Prediction to guide LLM prompting by adaptively reducing the set of candidate classes. However, its broader applicability and efficiency benefits beyond a single domain have not yet been systematically explored. In this paper, we present a comprehensive evaluation of CICLe across diverse NLP classification benchmarks. The results show that CICLe consistently improves over its base classifier and outperforms few-shot prompting baselines when the sample size is sufficient for training the base classifier, and performs comparably in low-data regimes. In terms of efficiency, CICLe reduces the number of shots and prompt length by up to 34.45% and 25.16%, respectively, and enables the use of smaller models with competitive performance. CICLe is furthermore particularly advantageous for text classification tasks with high class imbalance. These findings highlight CICLe as a practical and scalable approach for efficient text classification, combining the robustness of traditional classifiers with the adaptability of LLMs, and achieving substantial gains in data and computational efficiency.

