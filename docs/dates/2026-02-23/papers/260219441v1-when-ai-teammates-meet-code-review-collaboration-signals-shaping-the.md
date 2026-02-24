---
layout: default
title: When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests
---

# When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests
**arXiv**：[2602.19441v1](https://arxiv.org/abs/2602.19441) · [PDF](https://arxiv.org/pdf/2602.19441.pdf)  
**作者**：Costain Nachuma, Minhaz Zibran  

**一句话要点**：通过实证研究揭示AI编码代理提交的拉取请求在代码审查中的协作信号对集成成功的影响

**关键词**：AI编码代理, 代码审查, 协作信号, 拉取请求集成, 实证研究, GitHub工作流

## 3 点简述
- 核心问题：AI编码代理在GitHub上提交拉取请求后，如何融入人类驱动的代码审查工作流，集成成功的关键因素未知。
- 方法要点：基于AIDev数据集进行大规模实证分析，使用逻辑回归模型评估协作信号与集成结果的关系，并辅以定性分析。
- 实验或效果：发现审查员参与度与集成成功强相关，而大变更和强制推送等协调破坏行为降低合并概率，迭代强度解释力有限。

## 摘要（原文）

> Autonomous coding agents increasingly contribute to software development by submitting pull requests on GitHub; yet, little is known about how these contributions integrate into human-driven review workflows. We present a large empirical study of agent-authored pull requests using the public AIDev dataset, examining integration outcomes, resolution speed, and review-time collaboration signals. Using logistic regression with repository-clustered standard errors, we find that reviewer engagement has the strongest correlation with successful integration, whereas larger change sizes and coordination-disrupting actions, such as force pushes, are associated with a lower likelihood of merging. In contrast, iteration intensity alone provides limited explanatory power once collaboration signals are considered. A qualitative analysis further shows that successful integration occurs when agents engage in actionable review loops that converge toward reviewer expectations. Overall, our results highlight that the effective integration of agent-authored pull requests depends not only on code quality but also on alignment with established review and coordination practices.

