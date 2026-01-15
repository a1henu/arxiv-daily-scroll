---
layout: default
title: Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing
---

# Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing
**arXiv**：[2601.09282v1](https://arxiv.org/abs/2601.09282) · [PDF](https://arxiv.org/pdf/2601.09282.pdf)  
**作者**：Leszek Sliwko, Jolanta Mizeria-Pietraszko  

**一句话要点**：提出基于自然语言处理的语义软亲和性调度方法，以简化集群工作负载分配配置。

**关键词**：集群调度, 自然语言处理, 语义软亲和性, 大型语言模型, Kubernetes扩展

## 3 点简述
- 集群工作负载分配配置复杂，存在可用性差距。
- 使用大型语言模型解析自然语言提示，实现意图驱动的软亲和性调度。
- 原型系统在解析准确性和调度质量上优于基线，验证了语义方法的可行性。

## 摘要（原文）

> Cluster workload allocation often requires complex configurations, creating a usability gap. This paper introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural Language Processing. The system employs a Large Language Model (LLM) integrated via a Kubernetes scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences. A prototype featuring a cluster state cache and an intent analyzer (using AWS Bedrock) was developed. Empirical evaluation demonstrated high LLM parsing accuracy (>95% Subset Accuracy on an evaluation ground-truth dataset) for top-tier models like Amazon Nova Pro/Premier and Mistral Pixtral Large, significantly outperforming a baseline engine. Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations, particularly excelling in complex and quantitative scenarios and handling conflicting soft preferences. The results validate using LLMs for accessible scheduling but highlight limitations like synchronous LLM latency, suggesting asynchronous processing for production readiness. This work confirms the viability of semantic soft affinity for simplifying workload orchestration.

