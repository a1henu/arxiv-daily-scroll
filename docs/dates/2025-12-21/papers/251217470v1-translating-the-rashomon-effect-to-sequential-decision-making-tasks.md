---
layout: default
title: Translating the Rashomon Effect to Sequential Decision-Making Tasks
---

# Translating the Rashomon Effect to Sequential Decision-Making Tasks
**arXiv**：[2512.17470v1](https://arxiv.org/abs/2512.17470) · [PDF](https://arxiv.org/pdf/2512.17470.pdf)  
**作者**：Dennis Gross, Jørn Eirik Betten, Helge Spieker  

**一句话要点**：将拉什莫尔效应引入序列决策任务，通过形式化验证方法识别行为相同但内部结构不同的策略。

**关键词**：拉什莫尔效应, 序列决策, 形式化验证, 策略集成, 鲁棒性, 概率行为

## 3 点简述
- 核心问题：拉什莫尔效应在分类任务中已研究，但在序列决策中未知，需定义和验证行为相同的策略。
- 方法要点：使用形式化验证方法比较策略的完整概率行为，以应对随机转移带来的不确定性。
- 实验或效果：实验证实序列决策中存在拉什莫尔效应，基于此构建的集成策略对分布偏移更鲁棒。

## 摘要（原文）

> The Rashomon effect describes the phenomenon where multiple models trained on the same data produce identical predictions while differing in which features they rely on internally. This effect has been studied extensively in classification tasks, but not in sequential decision-making, where an agent learns a policy to achieve an objective by taking actions in an environment. In this paper, we translate the Rashomon effect to sequential decision-making. We define it as multiple policies that exhibit identical behavior, visiting the same states and selecting the same actions, while differing in their internal structure, such as feature attributions. Verifying identical behavior in sequential decision-making differs from classification. In classification, predictions can be directly compared to ground-truth labels. In sequential decision-making with stochastic transitions, the same policy may succeed or fail on any single trajectory due to randomness. We address this using formal verification methods that construct and compare the complete probabilistic behavior of each policy in the environment. Our experiments demonstrate that the Rashomon effect exists in sequential decision-making. We further show that ensembles constructed from the Rashomon set exhibit greater robustness to distribution shifts than individual policies. Additionally, permissive policies derived from the Rashomon set reduce computational requirements for verification while maintaining optimal performance.

