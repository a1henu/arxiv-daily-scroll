---
layout: default
title: Decision Quality Evaluation Framework at Pinterest
---

# Decision Quality Evaluation Framework at Pinterest
**arXiv**：[2602.15809v1](https://arxiv.org/abs/2602.15809) · [PDF](https://arxiv.org/pdf/2602.15809.pdf)  
**作者**：Yuqi Tian, Robert Paine, Attila Dobi, Kevin O'Sullivan, Aravindh Manickavasagam, Faisal Farooq  

**一句话要点**：提出决策质量评估框架以解决在线平台内容安全策略执行中的评估挑战

**关键词**：内容安全, 决策质量评估, 黄金集, 智能采样, LLM基准测试, 策略管理

## 3 点简述
- 核心问题：在线平台内容安全决策评估面临成本、规模和可信度之间的权衡，以及策略演变的复杂性。
- 方法要点：基于专家构建的高可信度黄金集，结合自动化智能采样管道，利用倾向得分扩展数据集覆盖。
- 实验或效果：应用于LLM代理成本性能基准测试、数据驱动提示优化、策略演变管理和策略内容流行度指标验证。

## 摘要（原文）

> Online platforms require robust systems to enforce content safety policies at scale. A critical component of these systems is the ability to evaluate the quality of moderation decisions made by both human agents and Large Language Models (LLMs). However, this evaluation is challenging due to the inherent trade-offs between cost, scale, and trustworthiness, along with the complexity of evolving policies. To address this, we present a comprehensive Decision Quality Evaluation Framework developed and deployed at Pinterest. The framework is centered on a high-trust Golden Set (GDS) curated by subject matter experts (SMEs), which serves as a ground truth benchmark. We introduce an automated intelligent sampling pipeline that uses propensity scores to efficiently expand dataset coverage. We demonstrate the framework's practical application in several key areas: benchmarking the cost-performance trade-offs of various LLM agents, establishing a rigorous methodology for data-driven prompt optimization, managing complex policy evolution, and ensuring the integrity of policy content prevalence metrics via continuous validation. The framework enables a shift from subjective assessments to a data-driven and quantitative practice for managing content safety systems.

