---
layout: default
title: How does My Model Fail? Automatic Identification and Interpretation of Physical Plausibility Failure Modes with Matryoshka Transcoders
---

# How does My Model Fail? Automatic Identification and Interpretation of Physical Plausibility Failure Modes with Matryoshka Transcoders
**arXiv**：[2511.10094v1](https://arxiv.org/abs/2511.10094) · [PDF](https://arxiv.org/pdf/2511.10094.pdf)  
**作者**：Yiming Tang, Abhijeet Sinha, Dianbo Liu  

**一句话要点**：提出Matryoshka Transcoders框架，自动发现和解释生成模型的物理合理性失败模式

**关键词**：物理合理性, 特征学习, 生成模型评估, 多模态解释, 失败模式分析

## 3 点简述
- 生成模型常出现物理合理性错误，现有评估方法难以检测，且缺乏自动识别框架
- 扩展Matryoshka表示学习至transcoder架构，实现多粒度层次稀疏特征学习
- 在八个先进生成模型上分析，提供失败模式洞察，并建立评估基准

## 摘要（原文）

> Although recent generative models are remarkably capable of producing instruction-following and realistic outputs, they remain prone to notable physical plausibility failures. Though critical in applications, these physical plausibility errors often escape detection by existing evaluation methods. Furthermore, no framework exists for automatically identifying and interpreting specific physical error patterns in natural language, preventing targeted model improvements. We introduce Matryoshka Transcoders, a novel framework for the automatic discovery and interpretation of physical plausibility features in generative models. Our approach extends the Matryoshka representation learning paradigm to transcoder architectures, enabling hierarchical sparse feature learning at multiple granularity levels. By training on intermediate representations from a physical plausibility classifier and leveraging large multimodal models for interpretation, our method identifies diverse physics-related failure modes without manual feature engineering, achieving superior feature relevance and feature accuracy compared to existing approaches. We utilize the discovered visual patterns to establish a benchmark for evaluating physical plausibility in generative models. Our analysis of eight state-of-the-art generative models provides valuable insights into how these models fail to follow physical constraints, paving the way for further model improvements.

