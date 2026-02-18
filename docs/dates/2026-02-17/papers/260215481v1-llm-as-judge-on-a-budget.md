---
layout: default
title: LLM-as-Judge on a Budget
---

# LLM-as-Judge on a Budget
**arXiv**：[2602.15481v1](https://arxiv.org/abs/2602.15481) · [PDF](https://arxiv.org/pdf/2602.15481.pdf)  
**作者**：Aadirupa Saha, Aniket Wagde, Branislav Kveton  

**一句话要点**：提出基于多臂老虎机的方差自适应方法，以优化固定预算下LLM评估的查询分配问题。

**关键词**：LLM评估, 多臂老虎机, 方差自适应, 计算预算优化, AI安全评估

## 3 点简述
- 核心问题：在固定计算预算下，如何分配查询以最小化LLM评估中的分数估计误差。
- 方法要点：利用多臂老虎机理论和集中不等式，动态分配查询以降低高方差对的估计不确定性。
- 实验效果：在Summarize-From-Feedback和HelpSteer2数据集上，显著优于均匀分配，减少最坏情况误差。

## 摘要（原文）

> LLM-as-a-judge has emerged as a cornerstone technique for evaluating large language models by leveraging LLM reasoning to score prompt-response pairs. Since LLM judgments are stochastic, practitioners commonly query each pair multiple times to estimate mean scores accurately. This raises a critical challenge: given a fixed computational budget $B$, how to optimally allocate queries across $K$ prompt-response pairs to minimize estimation error? %
> We present a principled variance-adaptive approach leveraging multi-armed bandit theory and concentration inequalities. Our method dynamically allocates queries based on estimated score variances, concentrating resources where uncertainty is highest. Further, our algorithm is shown to achieve a worst-case score-estimation error of $\tilde{O}\left(\sqrt{\frac{\sum_{i=1}^K σ_i^2}{B}}\right)$, $σ_i^2$ being the unknown score variance for pair $i \in [K]$ with near-optimal budget allocation. %
> Experiments on \emph{Summarize-From-Feedback} and \emph{HelpSteer2} demonstrate that our method significantly outperforms uniform allocation, reducing worst-case estimation error while maintaining identical budgets. Our work establishes a theoretical foundation for efficient LLM evaluation with practical implications for AI safety, model alignment, and automated assessment at scale.

