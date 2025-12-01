---
layout: default
title: Identification of Malicious Posts on the Dark Web Using Supervised Machine Learning
---

# Identification of Malicious Posts on the Dark Web Using Supervised Machine Learning
**arXiv**：[2511.23183v1](https://arxiv.org/abs/2511.23183) · [PDF](https://arxiv.org/pdf/2511.23183.pdf)  
**作者**：Sebastião Alves de Jesus Filho, Gustavo Di Giovanni Bernardo, Paulo Henrique Ribeiro Gabriel, Bruno Bogaz Zarpelão, Rodrigo Sanches Miani  

**一句话要点**：提出基于机器学习的多阶段标注方法，用于识别暗网论坛中的恶意帖子。

**关键词**：恶意帖子检测, 暗网论坛分析, 文本挖掘, 机器学习, 巴西葡萄牙语, 威胁情报

## 3 点简述
- 核心问题：传统网络安全技术不足以应对日益复杂的网络攻击，需主动检测威胁。
- 方法要点：结合文本挖掘与机器学习，创建数据集并采用多阶段标注流程。
- 实验或效果：LightGBM与TF-IDF模型表现最佳，并通过主题建模验证鲁棒性。

## 摘要（原文）

> Given the constant growth and increasing sophistication of cyberattacks, cybersecurity can no longer rely solely on traditional defense techniques and tools. Proactive detection of cyber threats has become essential to help security teams identify potential risks and implement effective mitigation measures. Cyber Threat Intelligence (CTI) plays a key role by providing security analysts with evidence-based knowledge about cyber threats. CTI information can be extracted using various techniques and data sources; however, machine learning has proven promising. As for data sources, social networks and online discussion forums are commonly explored. In this study, we apply text mining techniques and machine learning to data collected from Dark Web forums in Brazilian Portuguese to identify malicious posts. Our contributions include the creation of three original datasets, a novel multi-stage labeling process combining indicators of compromise (IoCs), contextual keywords, and manual analysis, and a comprehensive evaluation of text representations and classifiers. To our knowledge, this is the first study to focus specifically on Brazilian Portuguese content in this domain. The best-performing model, using LightGBM and TF-IDF, was able to detect relevant posts with high accuracy. We also applied topic modeling to validate the model's outputs on unlabeled data, confirming its robustness in real-world scenarios.

