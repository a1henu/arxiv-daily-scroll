---
layout: default
title: MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems
---

# MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems
**arXiv**：[2602.19843v1](https://arxiv.org/abs/2602.19843) · [PDF](https://arxiv.org/pdf/2602.19843.pdf)  
**作者**：Jin Jia, Zhiling Deng, Zhuangbin Chen, Yingqi Wang, Zibin Zheng  

**一句话要点**：提出MAS-FIRE框架以评估基于LLM的多智能体系统可靠性

**关键词**：多智能体系统, 故障注入, 可靠性评估, 语义故障, 容错行为, 架构拓扑

## 3 点简述
- 核心问题：多智能体系统易受语义故障影响，现有评估方法难以诊断故障根源
- 方法要点：定义15种故障类型，通过提示修改等非侵入机制注入故障
- 实验或效果：应用于三种架构，揭示容错行为分层，发现架构拓扑对鲁棒性有决定性作用

## 摘要（原文）

> As LLM-based Multi-Agent Systems (MAS) are increasingly deployed for complex tasks, ensuring their reliability has become a pressing challenge. Since MAS coordinate through unstructured natural language rather than rigid protocols, they are prone to semantic failures (e.g., hallucinations, misinterpreted instructions, and reasoning drift) that propagate silently without raising runtime exceptions. Prevailing evaluation approaches, which measure only end-to-end task success, offer limited insight into how these failures arise or how effectively agents recover from them. To bridge this gap, we propose MAS-FIRE, a systematic framework for fault injection and reliability evaluation of MAS. We define a taxonomy of 15 fault types covering intra-agent cognitive errors and inter-agent coordination failures, and inject them via three non-invasive mechanisms: prompt modification, response rewriting, and message routing manipulation. Applying MAS-FIRE to three representative MAS architectures, we uncover a rich set of fault-tolerant behaviors that we organize into four tiers: mechanism, rule, prompt, and reasoning. This tiered view enables fine-grained diagnosis of where and why systems succeed or fail. Our findings reveal that stronger foundation models do not uniformly improve robustness. We further show that architectural topology plays an equally decisive role, with iterative, closed-loop designs neutralizing over 40% of faults that cause catastrophic collapse in linear workflows. MAS-FIRE provides the process-level observability and actionable guidance needed to systematically improve multi-agent systems.

