---
layout: default
title: From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents
---

# From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents
**arXiv**：[2602.04326v1](https://arxiv.org/abs/2602.04326) · [PDF](https://arxiv.org/pdf/2602.04326.pdf)  
**作者**：SeungWon Seo, SooBin Lim, SeongRae Noh, Haneul Kim, HyeongYeop Kang  

**一句话要点**：提出PCE框架，将LLM推理中的隐含假设转化为结构化决策树，以支持具身智能体在不确定性环境中的高效规划。

**关键词**：具身智能体, 不确定性规划, 大型语言模型, 多智能体系统, 决策树, 通信效率

## 3 点简述
- 核心问题：具身智能体在多智能体、部分可观测环境中面临不确定性，现有方法依赖频繁通信，成本高且可能干扰工作流程。
- 方法要点：PCE框架通过Planner-Composer-Evaluator将LLM推理中的碎片化假设编码为决策树，结合场景似然、目标增益和执行成本评分来指导行动选择。
- 实验或效果：在C-WAH和TDW-MAT基准测试中，PCE在成功率和任务效率上优于通信密集型基线，同时保持可比的令牌使用量，并通过用户研究验证了其高效性和可信度。

## 摘要（原文）

> Embodied agents operating in multi-agent, partially observable, and decentralized environments must plan and act despite pervasive uncertainty about hidden objects and collaborators' intentions. Recent advances in applying Large Language Models (LLMs) to embodied agents have addressed many long-standing challenges, such as high-level goal decomposition and online adaptation. Yet, uncertainty is still primarily mitigated through frequent inter-agent communication. This incurs substantial token and time costs, and can disrupt established workflows, when human partners are involved. We introduce PCE, a Planner-Composer-Evaluator framework that converts the fragmented assumptions latent in LLM reasoning traces into a structured decision tree. Internal nodes encode environment assumptions and leaves map to actions; each path is then scored by scenario likelihood, goal-directed gain, and execution cost to guide rational action selection without heavy communication. Across two challenging multi-agent benchmarks (C-WAH and TDW-MAT) and three diverse LLM backbones, PCE consistently outperforms communication-centric baselines in success rate and task efficiency while showing comparable token usage. Ablation results indicate that the performance gains obtained by scaling model capacity or reasoning depth persist even when PCE is applied, while PCE consistently raises the baseline across both capacity and reasoning-depth scales, confirming that structured uncertainty handling complements both forms of scaling. A user study further demonstrates that PCE produces communication patterns that human partners perceive as more efficient and trustworthy. Together, these results establish a principled route for turning latent LLM assumptions into reliable strategies for uncertainty-aware planning.

