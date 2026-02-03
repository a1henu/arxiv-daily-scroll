---
layout: default
title: ORCH: many analyses, one merge-a deterministic multi-agent orchestrator for discrete-choice reasoning with EMA-guided routing
---

# ORCH: many analyses, one merge-a deterministic multi-agent orchestrator for discrete-choice reasoning with EMA-guided routing
**arXiv**：[2602.01797v1](https://arxiv.org/abs/2602.01797) · [PDF](https://arxiv.org/pdf/2602.01797.pdf)  
**作者**：Hanlin Zhou, Huah Yong Chan  

**一句话要点**：提出ORCH确定性多智能体协调框架，用于离散选择推理，实现可复现与可解释的决策。

**关键词**：多智能体系统, 离散选择推理, 确定性协调, EMA引导路由, 可解释AI, 基准测试

## 3 点简述
- 现有系统依赖随机路由或启发式方法，导致行为难以复现和决策过程不透明。
- ORCH采用固定规则分解任务和聚合答案，结合EMA引导路由优化智能体选择，保持训练无关性。
- 在MMLU、MMLU-Pro和GSM8K基准上，ORCH显著超越单模型和多数投票集成，提升准确率10-50点以上。

## 摘要（原文）

> Recent advances in large-scale language models (LLMs) have made multi-agent architectures attractive for challenging reasoning tasks. However, many existing systems rely on stochastic routing or ad-hoc heuristics, making their behavior difficult to reproduce and their decision process hard to interpret. We propose ORCH, a deterministic coordination framework for discrete-choice reasoning that orchestrates heterogeneous LLMs. ORCH follows a ``many analyses, one decision'' paradigm: multiple base models independently produce structured analyses, and a dedicated merge agent outputs the final choice. The framework uses fixed rules for task decomposition and answer aggregation, keeping the pipeline predictable, reproducible, and training-free. Determinism here refers to fixed routing and aggregation rules under a fixed evaluation protocol, rather than strict bit-level reproducibility across deployments. To exploit model complementarity, we optionally introduce an EMA-guided router that updates agent selection using historical accuracy, latency, or cost; since it relies on answer-based feedback, it is mainly intended for benchmarking, controlled evaluation, or delayed-feedback settings. Experiments on MMLU, MMLU-Pro, and GSM8K show that ORCH consistently outperforms single-model baselines and a majority-vote ensemble. On MMLU-Pro, ORCH improves accuracy by over 10 points compared to the strongest baseline, and on GSM8K it yields gains exceeding 50 points; McNemar tests confirm statistical significance. The EMA router provides an additional 0.7--2.0 point accuracy boost, and ablations show that both multi-agent collaboration and routing contribute substantially. Overall, ORCH offers a practical path toward controllable, interpretable, and deployment-ready LLM-based agent systems for discrete-choice reasoning.

