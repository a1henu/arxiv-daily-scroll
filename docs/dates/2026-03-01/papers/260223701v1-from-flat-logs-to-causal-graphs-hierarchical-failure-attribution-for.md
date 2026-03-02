---
layout: default
title: From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems
---

# From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems
**arXiv**：[2602.23701v1](https://arxiv.org/abs/2602.23701) · [PDF](https://arxiv.org/pdf/2602.23701.pdf)  
**作者**：Yawen Wang, Wenjie Wu, Junjie Wang, Qing Wang  

**一句话要点**：提出CHIEF框架，将LLM多智能体系统日志转化为层次因果图以解决故障归因问题

**关键词**：多智能体系统, 故障归因, 因果图, LLM应用, 层次回溯

## 3 点简述
- 核心问题：现有方法将执行日志视为扁平序列，难以解析多智能体系统中的复杂因果链，导致故障归因模糊。
- 方法要点：CHIEF通过构建层次因果图、层次回溯剪枝和渐进因果筛选，实现高效故障根因识别。
- 实验或效果：在Who&When基准测试中，CHIEF在智能体和步骤级别准确率上优于八个基线方法，消融研究验证了各模块的关键作用。

## 摘要（原文）

> LLM-powered Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in complex domains but suffer from inherent fragility and opaque failure mechanisms. Existing failure attribution methods, whether relying on direct prompting, costly replays, or supervised fine-tuning, typically treat execution logs as flat sequences. This linear perspective fails to disentangle the intricate causal links inherent to MAS, leading to weak observability and ambiguous responsibility boundaries. To address these challenges, we propose CHIEF, a novel framework that transforms chaotic trajectories into a structured hierarchical causal graph. It then employs hierarchical oracle-guided backtracking to efficiently prune the search space via sybthesized virtual oracles. Finally, it implements counterfactual attribution via a progressive causal screening strategy to rigorously distinguish true root causes from propagated symptoms. Experiments on Who&When benchmark show that CHIEF outperforms eight strong and state-of-the-art baselines on both agent- and step-level accuracy. Ablation studies further confirm the critical role of each proposed module.

