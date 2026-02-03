---
layout: default
title: DCoPilot: Generative AI-Empowered Policy Adaptation for Dynamic Data Center Operations
---

# DCoPilot: Generative AI-Empowered Policy Adaptation for Dynamic Data Center Operations
**arXiv**：[2602.02137v1](https://arxiv.org/abs/2602.02137) · [PDF](https://arxiv.org/pdf/2602.02137.pdf)  
**作者**：Minghao Li, Ruihang Wang, Rui Tan, Yonggang Wen  

**一句话要点**：提出DCoPilot框架，通过生成式AI实现动态数据中心操作中的策略自适应

**关键词**：数据中心操作, 生成式AI, 深度强化学习, 策略自适应, 超网络, 大语言模型

## 3 点简述
- 核心问题：数据中心高功率密度与快速变化负载导致手动设计DRL策略滞后，可能引发服务中断
- 方法要点：结合LLM生成结构化奖励形式和超网络生成策略权重，通过仿真扩展、元策略蒸馏和在线适应三阶段协同
- 实验或效果：在五个控制任务家族中评估，实现近零约束违反，优于所有基线，消融研究验证LLM奖励生成的有效性

## 摘要（原文）

> Modern data centers (DCs) hosting artificial intelligence (AI)-dedicated devices operate at high power densities with rapidly varying workloads, making minute-level adaptation essential for safe and energy-efficient operation. However, manually designing piecewise deep reinforcement learning (DRL) agents cannot keep pace with frequent dynamics shifts and service-level agreement (SLA) changes of an evolving DC. This specification-to-policy lag causes a lack of timely, effective control policies, which may lead to service outages. To bridge the gap, we present DCoPilot, a hybrid framework for generative control policies in dynamic DC operation. DCoPilot synergizes two distinct generative paradigms, i.e., a large language model (LLM) that performs symbolic generation of structured reward forms, and a hypernetwork that conducts parametric generation of policy weights. DCoPilot operates through three coordinated phases: (i) simulation scale-up, which stress-tests reward candidates across diverse simulation-ready (SimReady) scenes; (ii) meta policy distillation, where a hypernetwork is trained to output policy weights conditioned on SLA and scene embeddings; and (iii) online adaptation, enabling zero-shot policy generation in response to updated specifications. Evaluated across five control task families spanning diverse DC components, DCoPilot achieves near-zero constraint violations and outperforms all baselines across specification variations. Ablation studies validate the effectiveness of LLM-based unified reward generation in enabling stable hypernetwork convergence.

