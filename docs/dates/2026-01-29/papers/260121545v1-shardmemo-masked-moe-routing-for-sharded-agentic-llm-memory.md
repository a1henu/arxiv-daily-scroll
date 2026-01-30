---
layout: default
title: ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory
---

# ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory
**arXiv**：[2601.21545v1](https://arxiv.org/abs/2601.21545) · [PDF](https://arxiv.org/pdf/2601.21545.pdf)  
**作者**：Yang Zhao, Chengxiao Dai, Yue Xiu, Mengying Kou, Yuliang Zheng, Dusit Niyato  

**一句话要点**：提出ShardMemo，一种预算化分层内存服务，以解决智能体LLM系统中内存扩展和并行访问的瓶颈问题。

**关键词**：智能体LLM系统, 分层内存服务, 掩码MoE路由, 分片证据库, 近似最近邻索引, 预算化检索

## 3 点简述
- 核心问题：智能体LLM系统依赖外部内存，但集中式索引和启发式分区在内存量和并行访问增长时成为瓶颈。
- 方法要点：采用三层内存结构，包括每代理工作状态、分片证据库和版本化技能库，通过掩码MoE路由实现范围优先路由。
- 实验或效果：在LoCoMo基准上，ShardMemo相比最强基线提升5.11至6.82 F1，在固定预算路由下减少检索工作和延迟，并在长上下文和工具使用任务中表现优异。

## 摘要（原文）

> Agentic large language model (LLM) systems rely on external memory for long-horizon state and concurrent multi-agent execution, but centralized indexes and heuristic partitions become bottlenecks as memory volume and parallel access grow. We present ShardMemo, a budgeted tiered memory service with Tier A per-agent working state, Tier B sharded evidence with shard-local approximate nearest neighbor (ANN) indexes, and Tier C, a versioned skill library. Tier B enforces scope-before-routing: structured eligibility constraints mask ineligible shards before routing or ANN search. We cast shard probing as masked mixture-of-experts (MoE) routing over eligible shards, probing up to $B_{\mathrm{probe}}$ shards via Top-$B_{\mathrm{probe}}$ or adaptive Top-$P$, and use cost-aware gating over profile/observation/session shard families; the router is trained from evidence-to-shard supervision. On LoCoMo, ShardMemo improves over the strongest baseline (GAM) by +5.11 to +6.82 F1 across question categories. Under a fixed-budget routing setting ($B_{\mathrm{probe}}=3$), ShardMemo improves over cosine-to-prototype shard routing by +6.87 F1 while reducing retrieval work (VecScan 521->414, -20.5%) and p95 latency (95->76 ms). On long-context HotpotQA, ShardMemo achieves 63.41/61.88/57.95 F1 at 56K/224K/448K tokens. On ToolBench, Tier C reaches 0.97 Precision@3 and 1.94 StepRed (+10.2% and +7.2% over embedding-similarity retrieval).

