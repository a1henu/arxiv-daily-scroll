---
layout: default
title: LLM-Assisted Logic Rule Learning: Scaling Human Expertise for Time Series Anomaly Detection
---

# LLM-Assisted Logic Rule Learning: Scaling Human Expertise for Time Series Anomaly Detection
**arXiv**：[2601.19255v1](https://arxiv.org/abs/2601.19255) · [PDF](https://arxiv.org/pdf/2601.19255.pdf)  
**作者**：Haoting Zhang, Shekhar Jain  

**一句话要点**：提出LLM辅助逻辑规则学习框架，以解决供应链时间序列异常检测中自动化与专家知识不匹配的问题。

**关键词**：时间序列异常检测, 逻辑规则学习, 大语言模型辅助, 供应链管理, 可解释性增强, 自动化优化

## 3 点简述
- 核心问题：传统无监督检测方法结果与业务需求不符，专家分析难以扩展到海量产品。
- 方法要点：利用LLM分阶段编码专家知识，生成可解释的逻辑规则，包括数据标注、规则优化和类别增强。
- 实验或效果：在检测准确性和可解释性上优于无监督方法，且比直接LLM部署更高效、低成本，适合生产环境。

## 摘要（原文）

> Time series anomaly detection is critical for supply chain management to take proactive operations, but faces challenges: classical unsupervised anomaly detection based on exploiting data patterns often yields results misaligned with business requirements and domain knowledge, while manual expert analysis cannot scale to millions of products in the supply chain. We propose a framework that leverages large language models (LLMs) to systematically encode human expertise into interpretable, logic-based rules for detecting anomaly patterns in supply chain time series data. Our approach operates in three stages: 1) LLM-based labeling of training data instructed by domain knowledge, 2) automated generation and iterative improvements of symbolic rules through LLM-driven optimization, and 3) rule augmentation with business-relevant anomaly categories supported by LLMs to enhance interpretability. The experiment results showcase that our approach outperforms the unsupervised learning methods in both detection accuracy and interpretability. Furthermore, compared to direct LLM deployment for time series anomaly detection, our approach provides consistent, deterministic results with low computational latency and cost, making it ideal for production deployment. The proposed framework thus demonstrates how LLMs can bridge the gap between scalable automation and expert-driven decision-making in operational settings.

