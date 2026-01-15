---
layout: default
title: Identifying Models Behind Text-to-Image Leaderboards
---

# Identifying Models Behind Text-to-Image Leaderboards
**arXiv**：[2601.09647v1](https://arxiv.org/abs/2601.09647) · [PDF](https://arxiv.org/pdf/2601.09647.pdf)  
**作者**：Ali Naseh, Yuefeng Peng, Anshuman Suri, Harsh Chaudhari, Alina Oprea, Amir Houmansadr  

**一句话要点**：提出基于图像嵌入聚类的中心化方法，以破解文本到图像排行榜的匿名性

**关键词**：文本到图像模型, 匿名化破解, 图像嵌入聚类, 排行榜安全, 去匿名化方法

## 3 点简述
- 核心问题：文本到图像模型在匿名化排行榜中存在安全漏洞，匿名性易被破坏
- 方法要点：利用图像嵌入空间中模型生成图像的聚类特性，通过中心化方法实现准确去匿名化
- 实验或效果：在22个模型和280个提示下，方法达到高准确率，揭示模型特定签名和提示可区分性

## 摘要（原文）

> Text-to-image (T2I) models are increasingly popular, producing a large share of AI-generated images online. To compare model quality, voting-based leaderboards have become the standard, relying on anonymized model outputs for fairness. In this work, we show that such anonymity can be easily broken. We find that generations from each T2I model form distinctive clusters in the image embedding space, enabling accurate deanonymization without prompt control or training data. Using 22 models and 280 prompts (150K images), our centroid-based method achieves high accuracy and reveals systematic model-specific signatures. We further introduce a prompt-level distinguishability metric and conduct large-scale analyses showing how certain prompts can lead to near-perfect distinguishability. Our findings expose fundamental security flaws in T2I leaderboards and motivate stronger anonymization defenses.

