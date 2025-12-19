---
layout: default
title: Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation
---

# Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation
**arXiv**：[2512.16310v1](https://arxiv.org/abs/2512.16310) · [PDF](https://arxiv.org/pdf/2512.16310.pdf)  
**作者**：Yuxuan Qiao, Dongqin Liu, Hongchang Yang, Wei Zhou, Songlin Hu  

**一句话要点**：提出工具编排隐私风险（TOP-R）框架与缓解方法，以应对智能代理隐私泄露问题

**关键词**：工具编排隐私风险, 智能代理安全, 隐私增强原则, TOP-Bench数据集, H-Score评估

## 3 点简述
- 核心问题：单代理多工具架构因目标函数错位，导致工具编排隐私风险（TOP-R），即代理聚合信息片段推理出敏感信息
- 方法要点：建立TOP-R形式化框架，构建TOP-Bench数据集，并提出隐私增强原则（PEP）方法进行缓解
- 实验或效果：评估显示TOP-R风险严重，PEP方法将风险泄露率降至46.58%，H-Score提升至0.624

## 摘要（原文）

> Driven by Large Language Models, the single-agent, multi-tool architecture has become a popular paradigm for autonomous agents due to its simplicity and effectiveness. However, this architecture also introduces a new and severe privacy risk, which we term Tools Orchestration Privacy Risk (TOP-R), where an agent, to achieve a benign user goal, autonomously aggregates information fragments across multiple tools and leverages its reasoning capabilities to synthesize unexpected sensitive information. We provide the first systematic study of this risk. First, we establish a formal framework, attributing the risk's root cause to the agent's misaligned objective function: an overoptimization for helpfulness while neglecting privacy awareness. Second, we construct TOP-Bench, comprising paired leakage and benign scenarios, to comprehensively evaluate this risk. To quantify the trade-off between safety and robustness, we introduce the H-Score as a holistic metric. The evaluation results reveal that TOP-R is a severe risk: the average Risk Leakage Rate (RLR) of eight representative models reaches 90.24%, while the average H-Score is merely 0.167, with no model exceeding 0.3. Finally, we propose the Privacy Enhancement Principle (PEP) method, which effectively mitigates TOP-R, reducing the Risk Leakage Rate to 46.58% and significantly improving the H-Score to 0.624. Our work reveals both a new class of risk and inherent structural limitations in current agent architectures, while also offering feasible mitigation strategies.

