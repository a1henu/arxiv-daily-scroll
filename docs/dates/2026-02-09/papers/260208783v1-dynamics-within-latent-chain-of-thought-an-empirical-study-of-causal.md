---
layout: default
title: Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure
---

# Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure
**arXiv**：[2602.08783v1](https://arxiv.org/abs/2602.08783) · [PDF](https://arxiv.org/pdf/2602.08783.pdf)  
**作者**：Zirui Li, Xuefeng Bai, Kehai Chen, Yizhi Li, Jian Yang, Chenghua Lin, Min Zhang  

**一句话要点**：提出基于结构因果模型的干预方法，以分析潜在思维链中的因果动态与推理机制。

**关键词**：潜在思维链, 结构因果模型, 因果干预, 推理机制, 可解释性分析

## 3 点简述
- 核心问题：潜在思维链方法缺乏可解释性，难以评估中间步骤的因果作用。
- 方法要点：将潜在步骤建模为结构因果模型变量，通过逐步干预分析其影响。
- 实验或效果：在数学和通用推理任务上，揭示步骤功能异质性和输出与表示承诺的差距。

## 摘要（原文）

> Latent or continuous chain-of-thought methods replace explicit textual rationales with a number of internal latent steps, but these intermediate computations are difficult to evaluate beyond correlation-based probes. In this paper, we view latent chain-of-thought as a manipulable causal process in representation space by modeling latent steps as variables in a structural causal model (SCM) and analyzing their effects through step-wise $\mathrm{do}$-interventions. We study two representative paradigms (i.e., Coconut and CODI) on both mathematical and general reasoning tasks to investigate three key questions: (1) which steps are causally necessary for correctness and when answers become decidable early; (2) how does influence propagate across steps, and how does this structure compare to explicit CoT; and (3) do intermediate trajectories retain competing answer modes, and how does output-level commitment differ from representational commitment across steps. We find that latent-step budgets behave less like homogeneous extra depth and more like staged functionality with non-local routing, and we identify a persistent gap between early output bias and late representational commitment. These results motivate mode-conditional and stability-aware analyses -- and corresponding training/decoding objectives -- as more reliable tools for interpreting and improving latent reasoning systems.

