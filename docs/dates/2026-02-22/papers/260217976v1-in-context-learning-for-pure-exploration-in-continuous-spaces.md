---
layout: default
title: In-Context Learning for Pure Exploration in Continuous Spaces
---

# In-Context Learning for Pure Exploration in Continuous Spaces
**arXiv**：[2602.17976v1](https://arxiv.org/abs/2602.17976) · [PDF](https://arxiv.org/pdf/2602.17976.pdf)  
**作者**：Alessio Russo, Yin-Ching Lee, Ryan Welch, Aldo Pacchiano  

**一句话要点**：提出C-ICPE-TS算法，通过元训练深度神经网络策略解决连续空间中的纯探索问题。

**关键词**：纯探索, 连续空间, 元学习, 深度神经网络, 序列测试, 最优臂识别

## 3 点简述
- 研究连续空间中的纯探索问题，如连续臂赌博机最优动作识别和函数最小化器估计。
- 提出C-ICPE-TS算法，元训练深度神经网络从数据中学习可迁移的序列测试策略，无需参数更新。
- 在连续最优臂识别、区域定位和函数最小化器识别等基准上验证算法有效性。

## 摘要（原文）

> In active sequential testing, also termed pure exploration, a learner is tasked with the goal to adaptively acquire information so as to identify an unknown ground-truth hypothesis with as few queries as possible. This problem, originally studied by Chernoff in 1959, has several applications: classical formulations include Best-Arm Identification (BAI) in bandits, where actions index hypotheses, and generalized search problems, where strategically chosen queries reveal partial information about a hidden label. In many modern settings, however, the hypothesis space is continuous and naturally coincides with the query/action space: for example, identifying an optimal action in a continuous-armed bandit, localizing an $ε$-ball contained in a target region, or estimating the minimizer of an unknown function from a sequence of observations. In this work, we study pure exploration in such continuous spaces and introduce Continuous In-Context Pure Exploration for this regime. We introduce C-ICPE-TS, an algorithm that meta-trains deep neural policies to map observation histories to (i) the next continuous query action and (ii) a predicted hypothesis, thereby learning transferable sequential testing strategies directly from data. At inference time, C-ICPE-TS actively gathers evidence on previously unseen tasks and infers the true hypothesis without parameter updates or explicit hand-crafted information models. We validate C-ICPE-TS across a range of benchmarks, spanning continuous best-arm identification, region localization, and function minimizer identification.

