---
layout: default
title: Evaluating Human and Machine Confidence in Phishing Email Detection: A Comparative Study
---

# Evaluating Human and Machine Confidence in Phishing Email Detection: A Comparative Study
**arXiv**：[2601.04610v1](https://arxiv.org/abs/2601.04610) · [PDF](https://arxiv.org/pdf/2601.04610.pdf)  
**作者**：Paras Jain, Khushi Dhar, Olyemi E. Amujo, Esa M. Rantanen  

**一句话要点**：比较人类与机器学习在钓鱼邮件检测中的置信度，以提升人机协作透明度

**关键词**：钓鱼邮件检测, 置信度评估, 人机协作, 可解释机器学习, TF-IDF特征, 语义嵌入

## 3 点简述
- 核心问题：钓鱼邮件检测需结合模式识别与置信评估，人类与机器协作机制尚不明确。
- 方法要点：使用逻辑回归、决策树和随机森林，结合TF-IDF和语义嵌入特征，对比人类评估的置信度与语言观察。
- 实验或效果：机器学习准确率高但置信度波动大，人类置信更一致且语言特征多样，年龄影响检测性能。

## 摘要（原文）

> Identifying deceptive content like phishing emails demands sophisticated cognitive processes that combine pattern recognition, confidence assessment, and contextual analysis. This research examines how human cognition and machine learning models work together to distinguish phishing emails from legitimate ones. We employed three interpretable algorithms Logistic Regression, Decision Trees, and Random Forests training them on both TF-IDF features and semantic embeddings, then compared their predictions against human evaluations that captured confidence ratings and linguistic observations. Our results show that machine learning models provide good accuracy rates, but their confidence levels vary significantly. Human evaluators, on the other hand, use a greater variety of language signs and retain more consistent confidence. We also found that while language proficiency has minimal effect on detection performance, aging does. These findings offer helpful direction for creating transparent AI systems that complement human cognitive functions, ultimately improving human-AI cooperation in challenging content analysis tasks.

