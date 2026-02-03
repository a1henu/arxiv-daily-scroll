---
layout: default
title: Privacy Amplification by Missing Data
---

# Privacy Amplification by Missing Data
**arXiv**：[2602.01928v1](https://arxiv.org/abs/2602.01928) · [PDF](https://arxiv.org/pdf/2602.01928.pdf)  
**作者**：Simon Roburin, Rafaël Pinot, Erwan Scornet  

**一句话要点**：提出缺失数据作为隐私放大机制，增强差分隐私算法在医学和金融等领域的隐私保护。

**关键词**：隐私保护, 缺失数据, 差分隐私, 隐私放大, 数据匿名化

## 3 点简述
- 核心问题：传统视缺失数据为限制，本文从隐私角度研究其潜在保护作用。
- 方法要点：在差分隐私框架下，形式化缺失数据作为隐私放大机制，首次证明其有效性。
- 实验或效果：未知具体实验，但理论分析表明缺失数据可增强隐私保护。

## 摘要（原文）

> Privacy preservation is a fundamental requirement in many high-stakes domains such as medicine and finance, where sensitive personal data must be analyzed without compromising individual confidentiality. At the same time, these applications often involve datasets with missing values due to non-response, data corruption, or deliberate anonymization. Missing data is traditionally viewed as a limitation because it reduces the information available to analysts and can degrade model performance. In this work, we take an alternative perspective and study missing data from a privacy preservation standpoint. Intuitively, when features are missing, less information is revealed about individuals, suggesting that missingness could inherently enhance privacy. We formalize this intuition by analyzing missing data as a privacy amplification mechanism within the framework of differential privacy. We show, for the first time, that incomplete data can yield privacy amplification for differentially private algorithms.

