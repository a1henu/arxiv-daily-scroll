---
layout: default
title: On the Rate-Distortion-Complexity Tradeoff for Semantic Communication
---

# On the Rate-Distortion-Complexity Tradeoff for Semantic Communication
**arXiv**：[2602.14481v1](https://arxiv.org/abs/2602.14481) · [PDF](https://arxiv.org/pdf/2602.14481.pdf)  
**作者**：Jingxuan Chai, Yong Xiao, Guangming Shi  

**一句话要点**：提出率失真复杂度框架以解决语义通信中计算复杂度高的问题

**关键词**：语义通信, 率失真复杂度, 信息瓶颈, 计算复杂度, 深度学习编码

## 3 点简述
- 核心问题：现有语义通信方法忽视深度学习编码解码的高计算复杂度
- 方法要点：扩展经典率失真理论，引入语义距离约束和复杂度度量
- 实验或效果：理论推导高斯和二元语义源的最小可达率，实验验证三向权衡

## 摘要（原文）

> Semantic communication is a novel communication paradigm that focuses on conveying the user's intended meaning rather than the bit-wise transmission of source signals. One of the key challenges is to effectively represent and extract the semantic meaning of any given source signals. While deep learning (DL)-based solutions have shown promising results in extracting implicit semantic information from a wide range of sources, existing work often overlooks the high computational complexity inherent in both model training and inference for the DL-based encoder and decoder. To bridge this gap, this paper proposes a rate-distortion-complexity (RDC) framework which extends the classical rate-distortion theory by incorporating the constraints on semantic distance, including both the traditional bit-wise distortion metric and statistical difference-based divergence metric, and complexity measure, adopted from the theory of minimum description length and information bottleneck. We derive the closed-form theoretical results of the minimum achievable rate under given constraints on semantic distance and complexity for both Gaussian and binary semantic sources. Our theoretical results show a fundamental three-way tradeoff among achievable rate, semantic distance, and model complexity. Extensive experiments on real-world image and video datasets validate this tradeoff and further demonstrate that our information-theoretic complexity measure effectively correlates with practical computational costs, guiding efficient system design in resource-constrained scenarios.

