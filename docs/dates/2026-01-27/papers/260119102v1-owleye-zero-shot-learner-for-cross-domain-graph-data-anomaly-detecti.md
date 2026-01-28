---
layout: default
title: OWLEYE: Zero-Shot Learner for Cross-Domain Graph Data Anomaly Detection
---

# OWLEYE: Zero-Shot Learner for Cross-Domain Graph Data Anomaly Detection
**arXiv**：[2601.19102v1](https://arxiv.org/abs/2601.19102) · [PDF](https://arxiv.org/pdf/2601.19102.pdf)  
**作者**：Lecheng Zheng, Dongqi Fu, Zihao Li, Jingrui He  

**一句话要点**：提出OWLEYE零-shot框架以解决跨域图数据异常检测中的特征语义差异问题

**关键词**：图异常检测, 零-shot学习, 跨域特征对齐, 字典学习, 注意力机制, 持续学习

## 3 点简述
- 核心问题：跨域图数据特征语义和维度差异阻碍通用模型开发，影响持续学习和推理能力
- 方法要点：设计跨域特征对齐模块、多域多模式字典学习和基于截断注意力的重建模块
- 实验或效果：在真实数据集上验证了优越性能和泛化能力，支持可扩展和标签高效的异常检测

## 摘要（原文）

> Graph data is informative to represent complex relationships such as transactions between accounts, communications between devices, and dependencies among machines or processes. Correspondingly, graph anomaly detection (GAD) plays a critical role in identifying anomalies across various domains, including finance, cybersecurity, manufacturing, etc. Facing the large-volume and multi-domain graph data, nascent efforts attempt to develop foundational generalist models capable of detecting anomalies in unseen graphs without retraining. To the best of our knowledge, the different feature semantics and dimensions of cross-domain graph data heavily hinder the development of the graph foundation model, leaving further in-depth continual learning and inference capabilities a quite open problem. Hence, we propose OWLEYE, a novel zero-shot GAD framework that learns transferable patterns of normal behavior from multiple graphs, with a threefold contribution. First, OWLEYE proposes a cross-domain feature alignment module to harmonize feature distributions, which preserves domain-specific semantics during alignment. Second, with aligned features, to enable continuous learning capabilities, OWLEYE designs the multi-domain multi-pattern dictionary learning to encode shared structural and attribute-based patterns. Third, for achieving the in-context learning ability, OWLEYE develops a truncated attention-based reconstruction module to robustly detect anomalies without requiring labeled data for unseen graph-structured data. Extensive experiments on real-world datasets demonstrate that OWLEYE achieves superior performance and generalizability compared to state-of-the-art baselines, establishing a strong foundation for scalable and label-efficient anomaly detection.

