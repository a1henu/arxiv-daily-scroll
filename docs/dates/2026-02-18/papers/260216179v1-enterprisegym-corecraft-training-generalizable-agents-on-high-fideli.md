---
layout: default
title: EnterpriseGym Corecraft: Training Generalizable Agents on High-Fidelity RL Environments
---

# EnterpriseGym Corecraft: Training Generalizable Agents on High-Fidelity RL Environments
**arXiv**：[2602.16179v1](https://arxiv.org/abs/2602.16179) · [PDF](https://arxiv.org/pdf/2602.16179.pdf)  
**作者**：Sushant Mehta, Logan Ritchie, Suhaas Garre, Nick Heiner, Edwin Chen  

**一句话要点**：提出EnterpriseGym Corecraft高保真RL环境，训练可泛化AI代理以解决企业任务。

**关键词**：高保真强化学习环境, 企业任务模拟, 代理泛化能力, Group Relative Policy Optimization, 自适应裁剪, 任务中心化世界构建

## 3 点简述
- 核心问题：现有AI代理在复杂企业任务中泛化能力不足，如GPT-5.2和Claude Opus 4.6任务通过率低于30%。
- 方法要点：构建Corecraft环境，模拟客户支持组织，含2500+实体和23种工具，使用GRPO和自适应裁剪训练GLM 4.6。
- 实验效果：单轮训练后，任务通过率从25.37%提升至36.76%，在多个分布外基准上泛化性能提升4.5%-7.4%。

## 摘要（原文）

> We show that training AI agents on high-fidelity reinforcement learning environments produces capabilities that generalize beyond the training distribution. We introduce \corecraft{}, the first environment in \textsc{EnterpriseGym}, Surge AI's suite of agentic RL environments. \corecraft{} is a fully operational enterprise simulation of a customer support organization, comprising over 2,500 entities across 14 entity types with 23 unique tools, designed to measure whether AI agents can perform the multi-step, domain-specific work that real jobs demand. Frontier models such as GPT-5.2 and Claude Opus 4.6 solve fewer than 30\% of tasks when all expert-authored rubric criteria must be satisfied. Using this environment, we train GLM~4.6 with Group Relative Policy Optimization (GRPO) and adaptive clipping. After a single epoch of training, the model improves from 25.37\% to 36.76\% task pass rate on held-out evaluation tasks. More importantly, these gains transfer to out-of-distribution benchmarks: +4.5\% on BFCL Parallel, +7.4\% on $τ^2$-Bench Retail, and +6.8\% on Toolathlon (Pass@1). We believe three environment properties are consistent with the observed transfer: task-centric world building that optimizes for diverse, challenging tasks; expert-authored rubrics enabling reliable reward computation; and enterprise workflows that reflect realistic professional patterns. Our results suggest that environment quality, diversity, and realism are key factors enabling generalizable agent capabilities.

