---
layout: default
title: Differentially Private Synthetic Data Generation Using Context-Aware GANs
---

# Differentially Private Synthetic Data Generation Using Context-Aware GANs
**arXiv**：[2512.08869v1](https://arxiv.org/abs/2512.08869) · [PDF](https://arxiv.org/pdf/2512.08869.pdf)  
**作者**：Anantaa Kotal, Anupam Joshi  

**一句话要点**：提出ContextGAN以解决隐私保护下合成数据忽略领域隐式规则的问题

**关键词**：差分隐私, 生成对抗网络, 合成数据生成, 领域约束, 隐私保护, 数据效用

## 3 点简述
- 核心问题：传统合成数据方法难以捕捉领域隐式规则，导致数据不现实或无效
- 方法要点：集成约束矩阵编码领域知识，通过约束感知判别器确保数据遵循规则
- 实验或效果：在医疗、安全、金融领域验证，生成高质量合成数据，提升真实性和实用性

## 摘要（原文）

> The widespread use of big data across sectors has raised major privacy concerns, especially when sensitive information is shared or analyzed. Regulations such as GDPR and HIPAA impose strict controls on data handling, making it difficult to balance the need for insights with privacy requirements. Synthetic data offers a promising solution by creating artificial datasets that reflect real patterns without exposing sensitive information. However, traditional synthetic data methods often fail to capture complex, implicit rules that link different elements of the data and are essential in domains like healthcare. They may reproduce explicit patterns but overlook domain-specific constraints that are not directly stated yet crucial for realism and utility. For example, prescription guidelines that restrict certain medications for specific conditions or prevent harmful drug interactions may not appear explicitly in the original data. Synthetic data generated without these implicit rules can lead to medically inappropriate or unrealistic profiles. To address this gap, we propose ContextGAN, a Context-Aware Differentially Private Generative Adversarial Network that integrates domain-specific rules through a constraint matrix encoding both explicit and implicit knowledge. The constraint-aware discriminator evaluates synthetic data against these rules to ensure adherence to domain constraints, while differential privacy protects sensitive details from the original data. We validate ContextGAN across healthcare, security, and finance, showing that it produces high-quality synthetic data that respects domain rules and preserves privacy. Our results demonstrate that ContextGAN improves realism and utility by enforcing domain constraints, making it suitable for applications that require compliance with both explicit patterns and implicit rules under strict privacy guarantees.

