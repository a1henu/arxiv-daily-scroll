---
layout: default
title: Reinforcement Learning of Large Language Models for Interpretable Credit Card Fraud Detection
---

# Reinforcement Learning of Large Language Models for Interpretable Credit Card Fraud Detection
**arXiv**：[2601.05578v1](https://arxiv.org/abs/2601.05578) · [PDF](https://arxiv.org/pdf/2601.05578.pdf)  
**作者**：Cooper Lin, Yanting Zhang, Maohao Ran, Wei Xue, Hongwei Fan, Yibo Xu, Zhenglin Wan, Sirui Han, Yike Guo, Jun Song  

**一句话要点**：提出基于强化学习的轻量语言模型后训练方法，用于可解释的信用卡欺诈检测。

**关键词**：信用卡欺诈检测, 强化学习, 语言模型后训练, 可解释性, 交易数据分析

## 3 点简述
- 问题：传统机器学习在欺诈检测中受限，大型语言模型在金融领域应用未经验证。
- 方法：使用GSPO算法和规则奖励系统，对语言模型进行后训练，探索交易文本中的风险信号。
- 效果：后训练模型在测试数据上F1分数显著提升，强化学习机制发现新欺诈指标。

## 摘要（原文）

> E-commerce platforms and payment solution providers face increasingly sophisticated fraud schemes, ranging from identity theft and account takeovers to complex money laundering operations that exploit the speed and anonymity of digital transactions. However, despite their theoretical promise, the application of Large Language Models (LLMs) to fraud detection in real-world financial contexts remains largely unexploited, and their practical effectiveness in handling domain-specific e-commerce transaction data has yet to be empirically validated. To bridge this gap between conventional machine learning limitations and the untapped potential of LLMs in fraud detection, this paper proposes a novel approach that employs Reinforcement Learning (RL) to post-train lightweight language models specifically for fraud detection tasks using only raw transaction data. We utilize the Group Sequence Policy Optimization (GSPO) algorithm combined with a rule-based reward system to fine-tune language models of various sizes on a real-life transaction dataset provided by a Chinese global payment solution company. Through this reinforcement learning framework, the language models are encouraged to explore diverse trust and risk signals embedded within the textual transaction data, including patterns in customer information, shipping details, product descriptions, and order history. Our experimental results demonstrate the effectiveness of this approach, with post-trained language models achieving substantial F1-score improvements on held-out test data. Our findings demonstrate that the observed performance improvements are primarily attributable to the exploration mechanism inherent in reinforcement learning, which allows models to discover novel fraud indicators beyond those captured by traditional engineered features.

