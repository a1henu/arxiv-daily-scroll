---
layout: default
title: AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications
---

# AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications
**arXiv**：[2602.22769v1](https://arxiv.org/abs/2602.22769) · [PDF](https://arxiv.org/pdf/2602.22769.pdf)  
**作者**：Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Haozhou Xu, Lanxiang Hu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, Yuandong Tian, Jishen Zhao  

**一句话要点**：提出AMA-Bench评估长时记忆，并设计AMA-Agent系统提升智能体性能。

**关键词**：长时记忆评估, 智能体应用, 因果图, 工具增强检索, 基准测试

## 3 点简述
- 现有评估标准与真实应用脱节，缺乏机器生成交互的连续流评估。
- AMA-Bench包含真实轨迹与合成轨迹，支持任意长度记忆测试。
- AMA-Agent通过因果图和工具增强检索，在基准上超越基线11.16%。

## 摘要（原文）

> Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA-Bench (Agent Memory with Any length), which evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons, paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information and are constrained by the lossy nature of similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA-Agent, an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA-Agent achieves 57.22% average accuracy on AMA-Bench, surpassing the strongest memory system baselines by 11.16%.

