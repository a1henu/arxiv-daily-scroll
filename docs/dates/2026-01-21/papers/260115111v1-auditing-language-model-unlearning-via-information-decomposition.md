---
layout: default
title: Auditing Language Model Unlearning via Information Decomposition
---

# Auditing Language Model Unlearning via Information Decomposition
**arXiv**：[2601.15111v1](https://arxiv.org/abs/2601.15111) · [PDF](https://arxiv.org/pdf/2601.15111.pdf)  
**作者**：Anmol Goel, Alan Ritter, Iryna Gurevych  

**一句话要点**：提出基于信息分解的审计框架，以评估语言模型遗忘中的隐私泄露风险。

**关键词**：语言模型遗忘, 信息分解审计, 隐私泄露评估, 表示风险评分, 对抗重构攻击

## 3 点简述
- 揭示语言模型遗忘后，遗忘数据信息仍可从内部表示线性解码的局限性。
- 引入部分信息分解框架，形式化遗忘知识与残留知识，量化隐私泄露。
- 提出基于表示的风险评分，指导推理时对敏感输入的弃权，降低泄露风险。

## 摘要（原文）

> We expose a critical limitation in current approaches to machine unlearning in language models: despite the apparent success of unlearning algorithms, information about the forgotten data remains linearly decodable from internal representations. To systematically assess this discrepancy, we introduce an interpretable, information-theoretic framework for auditing unlearning using Partial Information Decomposition (PID). By comparing model representations before and after unlearning, we decompose the mutual information with the forgotten data into distinct components, formalizing the notions of unlearned and residual knowledge. Our analysis reveals that redundant information, shared across both models, constitutes residual knowledge that persists post-unlearning and correlates with susceptibility to known adversarial reconstruction attacks. Leveraging these insights, we propose a representation-based risk score that can guide abstention on sensitive inputs at inference time, providing a practical mechanism to mitigate privacy leakage. Our work introduces a principled, representation-level audit for unlearning, offering theoretical insight and actionable tools for safer deployment of language models.

