---
layout: default
title: LLMAC: A Global and Explainable Access Control Framework with Large Language Model
---

# LLMAC: A Global and Explainable Access Control Framework with Large Language Model
**arXiv**：[2602.09392v1](https://arxiv.org/abs/2602.09392) · [PDF](https://arxiv.org/pdf/2602.09392.pdf)  
**作者**：Sharif Noor Zisad, Ragib Hasan  

**一句话要点**：提出LLMAC框架，利用大语言模型统一传统访问控制方法以应对动态复杂场景。

**关键词**：访问控制框架, 大语言模型应用, 可解释性系统, 动态策略管理, 合成数据集评估

## 3 点简述
- 传统访问控制方法如RBAC、ABAC和DAC难以处理现代系统的动态、情境依赖工作流。
- LLMAC基于大语言模型整合多种访问控制方法，提供全局、可解释的决策系统。
- 实验显示，在合成数据集上，LLMAC准确率达98.5%，显著优于传统方法，且具备实用部署性能。

## 摘要（原文）

> Today's business organizations need access control systems that can handle complex, changing security requirements that go beyond what traditional methods can manage. Current approaches, such as Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), and Discretionary Access Control (DAC), were designed for specific purposes. They cannot effectively manage the dynamic, situation-dependent workflows that modern systems require. In this research, we introduce LLMAC, a new unified approach using Large Language Models (LLMs) to combine these different access control methods into one comprehensive, understandable system. We used an extensive synthetic dataset that represents complex real-world scenarios, including policies for ownership verification, version management, workflow processes, and dynamic role separation. Using Mistral 7B, our trained LLM model achieved outstanding results with 98.5% accuracy, significantly outperforming traditional methods (RBAC: 14.5%, ABAC: 58.5%, DAC: 27.5%) while providing clear, human readable explanations for each decision. Performance testing shows that the system can be practically deployed with reasonable response times and computing resources.

