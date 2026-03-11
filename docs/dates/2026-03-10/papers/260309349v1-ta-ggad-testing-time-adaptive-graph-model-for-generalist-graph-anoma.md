---
layout: default
title: TA-GGAD: Testing-time Adaptive Graph Model for Generalist Graph Anomaly Detection
---

# TA-GGAD: Testing-time Adaptive Graph Model for Generalist Graph Anomaly Detection
**arXiv**：[2603.09349v1](https://arxiv.org/abs/2603.09349) · [PDF](https://arxiv.org/pdf/2603.09349.pdf)  
**作者**：Xiong Zhang, Hong Peng, Changlong Fu, Xin Jin, Yun Yang, Cheng Xie  

**一句话要点**：提出TA-GGAD图基础模型以解决跨域图异常检测中的异常非配性问题

**关键词**：图异常检测, 跨域泛化, 异常非配性, 图基础模型, 测试时适应

## 3 点简述
- 核心问题：跨域图异常检测存在特征不匹配的异常非配性问题，限制模型泛化能力
- 方法要点：基于异常非配性建模，设计单次训练即可跨域适应的图基础模型
- 实验或效果：在14个真实图数据上验证，检测准确率实现突破性SOTA水平

## 摘要（原文）

> A significant number of anomalous nodes in the real world, such as fake news, noncompliant users, malicious transactions, and malicious posts, severely compromises the health of the graph data ecosystem and urgently requires effective identification and processing. With anomalies that span multiple data domains yet exhibit vast differences in features, cross-domain detection models face severe domain shift issues, which limit their generalizability across all domains. This study identifies and quantitatively analyzes a specific feature mismatch pattern exhibited by domain shift in graph anomaly detection, which we define as the \emph{Anomaly Disassortativity} issue ($\mathcal{AD}$). Based on the modeling of the issue $\mathcal{AD}$, we introduce a novel graph foundation model for anomaly detection. It achieves cross-domain generalization in different graphs, requiring only a single training phase to perform effectively across diverse domains. The experimental findings, based on fourteen diverse real-world graphs, confirm a breakthrough in the model's cross-domain adaptation, achieving a pioneering state-of-the-art (SOTA) level in terms of detection accuracy. In summary, the proposed theory of $\mathcal{AD}$ provides a novel theoretical perspective and a practical route for future research in generalist graph anomaly detection (GGAD). The code is available at https://anonymous.4open.science/r/Anonymization-TA-GGAD/.

