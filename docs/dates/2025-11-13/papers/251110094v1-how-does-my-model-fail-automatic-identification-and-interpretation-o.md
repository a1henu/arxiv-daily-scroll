---
layout: default
title: How does My Model Fail? Automatic Identification and Interpretation of Physical Plausibility Failure Modes with Matryoshka Transcoders
---

# How does My Model Fail? Automatic Identification and Interpretation of Physical Plausibility Failure Modes with Matryoshka Transcoders
**arXiv**：[2511.10094v1](https://arxiv.org/abs/2511.10094) · [PDF](https://arxiv.org/pdf/2511.10094.pdf)  
**作者**：Yiming Tang, Abhijeet Sinha, Dianbo Liu  

**一句话要点**：提出Matryoshka Transcoders框架，自动识别和解释生成模型的物理合理性失败模式

**关键词**：物理合理性, 生成模型, 特征学习, 失败模式识别, 多模态解释

## 3 点简述
- 生成模型常出现物理合理性错误，现有方法难以检测和解释
- 基于Matryoshka表示学习，构建分层稀疏特征学习框架，无需手动特征工程
- 在八个先进模型上分析，识别多种失败模式，建立评估基准

## 摘要（原文）

> Although recent generative models are remarkably capable of producing instruction-following and realistic outputs, they remain prone to notable physical plausibility failures. Though critical in applications, these physical plausibility errors often escape detection by existing evaluation methods. Furthermore, no framework exists for automatically identifying and interpreting specific physical error patterns in natural language, preventing targeted model improvements. We introduce Matryoshka Transcoders, a novel framework for the automatic discovery and interpretation of physical plausibility features in generative models. Our approach extends the Matryoshka representation learning paradigm to transcoder architectures, enabling hierarchical sparse feature learning at multiple granularity levels. By training on intermediate representations from a physical plausibility classifier and leveraging large multimodal models for interpretation, our method identifies diverse physics-related failure modes without manual feature engineering, achieving superior feature relevance and feature accuracy compared to existing approaches. We utilize the discovered visual patterns to establish a benchmark for evaluating physical plausibility in generative models. Our analysis of eight state-of-the-art generative models provides valuable insights into how these models fail to follow physical constraints, paving the way for further model improvements.

