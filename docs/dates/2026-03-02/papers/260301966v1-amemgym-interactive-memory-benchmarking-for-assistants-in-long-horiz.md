---
layout: default
title: AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations
---

# AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations
**arXiv**：[2603.01966v1](https://arxiv.org/abs/2603.01966) · [PDF](https://arxiv.org/pdf/2603.01966.pdf)  
**作者**：Cheng Jiayang, Dongyu Ru, Lin Qiu, Yiyang Li, Xuezhi Cao, Yangqiu Song, Xunliang Cai  

**一句话要点**：提出AMemGym交互式环境，以解决长对话中助手记忆管理的训练与评估挑战。

**关键词**：长对话记忆, 交互式评估, 结构化数据采样, LLM模拟用户, 记忆管理优化

## 3 点简述
- 核心问题：现有记忆基准依赖静态数据，限制评估可靠性和可扩展性。
- 方法要点：通过结构化数据采样和LLM模拟用户，实现成本效益高的交互生成。
- 实验或效果：揭示现有记忆系统性能差距，并支持记忆策略的自进化。

## 摘要（原文）

> Long-horizon interactions between users and LLM-based assistants necessitate effective memory management, yet current approaches face challenges in training and evaluation of memory. Existing memory benchmarks rely on static, off-policy data as context, limiting evaluation reliability and scalability. To address these gaps, we introduce AMemGym, an interactive environment enabling on-policy evaluation and optimization for memory-driven personalization. AMemGym employs structured data sampling to predefine user profiles, state-dependent questions, and state evolution trajectories, enabling cost-effective generation of high-quality, evaluation-aligned interactions. LLM-simulated users expose latent states through role-play while maintaining structured state consistency. Comprehensive metrics based on structured data guide both assessment and optimization of assistants. Extensive experiments reveal performance gaps in existing memory systems (e.g., RAG, long-context LLMs, and agentic memory) and corresponding reasons. AMemGym not only enables effective selection among competing approaches but also can potentially drive the self-evolution of memory management strategies. By bridging structured state evolution with free-form interactions, our framework provides a scalable, diagnostically rich environment for advancing memory capabilities in conversational agents.

