---
layout: default
title: An Empirical Study on Preference Tuning Generalization and Diversity Under Domain Shift
---

# An Empirical Study on Preference Tuning Generalization and Diversity Under Domain Shift
**arXiv**：[2601.05882v1](https://arxiv.org/abs/2601.05882) · [PDF](https://arxiv.org/pdf/2601.05882.pdf)  
**作者**：Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras  

**一句话要点**：比较偏好调优目标与适应策略在领域转移下的泛化性能

**关键词**：偏好调优, 领域转移, 泛化性能, 伪标注, 语言模型对齐

## 3 点简述
- 研究偏好调优在领域转移时性能下降的问题
- 比较五种对齐目标和多种适应策略，包括伪标注
- 发现伪标注策略能显著减少领域转移导致的性能退化

## 摘要（原文）

> Preference tuning aligns pretrained language models to human judgments of quality, helpfulness, or safety by optimizing over explicit preference signals rather than likelihood alone. Prior work has shown that preference-tuning degrades performance and reduces helpfulness when evaluated outside the training domain. However, the extent to which adaptation strategies mitigate this domain shift remains unexplored. We address this challenge by conducting a comprehensive and systematic study of alignment generalization under domain shift. We compare five popular alignment objectives and various adaptation strategies from source to target, including target-domain supervised fine-tuning and pseudo-labeling, across summarization and question-answering helpfulness tasks. Our findings reveal systematic differences in generalization across alignment objectives under domain shift. We show that adaptation strategies based on pseudo-labeling can substantially reduce domain-shift degradation

