---
layout: default
title: On Cost-Aware Sequential Hypothesis Testing with Random Costs and Action Cancellation
---

# On Cost-Aware Sequential Hypothesis Testing with Random Costs and Action Cancellation
**arXiv**：[2512.19067v1](https://arxiv.org/abs/2512.19067) · [PDF](https://arxiv.org/pdf/2512.19067.pdf)  
**作者**：George Vershinin, Asaf Cohen, Omer Gurewitz  

**一句话要点**：提出带随机成本和动作取消的序贯假设检验，分析后验与先验成本揭示模型下的成本-误差权衡。

**关键词**：序贯假设检验, 随机成本, 动作取消, 成本-误差权衡, 决策理论

## 3 点简述
- 研究带随机成本和动作取消的序贯假设检验，决策者通过设置每动作截止期限来优化成本。
- 分析后验成本揭示模型下截止期限不影响总成本，先验模型下截止期限增加动作应用次数。
- 未知实验细节，但理论分析表明截止期限可降低总成本至恒定成本设置，并探讨其适用条件。

## 摘要（原文）

> We study a variant of cost-aware sequential hypothesis testing in which a single active Decision Maker (DM) selects actions with positive, random costs to identify the true hypothesis under an average error constraint, while minimizing the expected total cost. The DM may abort an in-progress action, yielding no sample, by truncating its realized cost at a smaller, tunable deterministic limit, which we term a per-action deadline. We analyze how this cancellation option can be exploited under two cost-revelation models: ex-post, where the cost is revealed only after the sample is obtained, and ex-ante, where the cost accrues before sample acquisition.
>   In the ex-post model, per-action deadlines do not affect the expected total cost, and the cost-error tradeoffs coincide with the baseline obtained by replacing deterministic costs with cost means. In the ex-ante model, we show how per-action deadlines inflate the expected number of times actions are applied, and that the resulting expected total cost can be reduced to the constant-cost setting by introducing an effective per-action cost. We characterize when deadlines are beneficial and study several families in detail.

