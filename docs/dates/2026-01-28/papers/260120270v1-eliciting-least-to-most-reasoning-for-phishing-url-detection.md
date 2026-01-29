---
layout: default
title: Eliciting Least-to-Most Reasoning for Phishing URL Detection
---

# Eliciting Least-to-Most Reasoning for Phishing URL Detection
**arXiv**：[2601.20270v1](https://arxiv.org/abs/2601.20270) · [PDF](https://arxiv.org/pdf/2601.20270.pdf)  
**作者**：Holly Trikilis, Pasindu Marasinghe, Fariza Rashid, Suranga Seneviratne  

**一句话要点**：提出Least-to-Most提示框架以提升钓鱼URL检测的推理能力与准确性

**关键词**：钓鱼URL检测, 大语言模型, Least-to-Most提示, 答案敏感性机制, 迭代推理, 少样本学习

## 3 点简述
- 钓鱼URL检测是网络安全的关键问题，现有LLMs推理能力未充分探索
- 引入答案敏感性机制，指导Least-to-Most迭代推理，增强预测性能
- 在三个数据集和四个LLMs上评估，性能优于单次提示，接近监督模型

## 摘要（原文）

> Phishing continues to be one of the most prevalent attack vectors, making accurate classification of phishing URLs essential. Recently, large language models (LLMs) have demonstrated promising results in phishing URL detection. However, their reasoning capabilities that enabled such performance remain underexplored. To this end, in this paper, we propose a Least-to-Most prompting framework for phishing URL detection. In particular, we introduce an "answer sensitivity" mechanism that guides Least-to-Most's iterative approach to enhance reasoning and yield higher prediction accuracy. We evaluate our framework using three URL datasets and four state-of-the-art LLMs, comparing against a one-shot approach and a supervised model. We demonstrate that our framework outperforms the one-shot baseline while achieving performance comparable to that of the supervised model, despite requiring significantly less training data. Furthermore, our in-depth analysis highlights how the iterative reasoning enabled by Least-to-Most, and reinforced by our answer sensitivity mechanism, drives these performance gains. Overall, we show that this simple yet powerful prompting strategy consistently outperforms both one-shot and supervised approaches, despite requiring minimal training or few-shot guidance. Our experimental setup can be found in our Github repository github.sydney.edu.au/htri0928/least-to-most-phishing-detection.

