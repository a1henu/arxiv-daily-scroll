---
layout: default
title: Automating Supply Chain Disruption Monitoring via an Agentic AI Approach
---

# Automating Supply Chain Disruption Monitoring via an Agentic AI Approach
**arXiv**：[2601.09680v1](https://arxiv.org/abs/2601.09680) · [PDF](https://arxiv.org/pdf/2601.09680.pdf)  
**作者**：Sara AlMahri, Liming Xu, Alexandra Brintrup  

**一句话要点**：提出基于代理AI的框架以自动化监控供应链深层网络中断

**关键词**：供应链中断监控, 代理AI框架, 大语言模型应用, 多层网络分析, 自动化风险评估

## 3 点简述
- 核心问题：供应链缺乏对一级以上供应商的可见性，导致上游中断难以及时发现。
- 方法要点：采用七个由大语言模型和确定性工具驱动的专业代理，从非结构化新闻中检测中断信号并映射到多层网络。
- 实验或效果：在30个合成场景中实现高准确率（F1分数0.962-0.991），端到端分析平均耗时3.83分钟，成本每中断0.0836美元。

## 摘要（原文）

> Modern supply chains are increasingly exposed to disruptions from geopolitical events, demand shocks, trade restrictions, to natural disasters. While many of these disruptions originate deep in the supply network, most companies still lack visibility beyond Tier-1 suppliers, leaving upstream vulnerabilities undetected until the impact cascades downstream. To overcome this blind-spot and move from reactive recovery to proactive resilience, we introduce a minimally supervised agentic AI framework that autonomously monitors, analyses, and responds to disruptions across extended supply networks. The architecture comprises seven specialised agents powered by large language models and deterministic tools that jointly detect disruption signals from unstructured news, map them to multi-tier supplier networks, evaluate exposure based on network structure, and recommend mitigations such as alternative sourcing options. \rev{We evaluate the framework across 30 synthesised scenarios covering three automotive manufacturers and five disruption classes. The system achieves high accuracy across core tasks, with F1 scores between 0.962 and 0.991, and performs full end-to-end analyses in a mean of 3.83 minutes at a cost of \$0.0836 per disruption. Relative to industry benchmarks of multi-day, analyst-driven assessments, this represents a reduction of more than three orders of magnitude in response time. A real-world case study of the 2022 Russia-Ukraine conflict further demonstrates operational applicability. This work establishes a foundational step toward building resilient, proactive, and autonomous supply chains capable of managing disruptions across deep-tier networks.

