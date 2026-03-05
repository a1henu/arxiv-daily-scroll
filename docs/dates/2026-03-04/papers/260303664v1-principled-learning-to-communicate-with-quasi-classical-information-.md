---
layout: default
title: Principled Learning-to-Communicate with Quasi-Classical Information Structures
---

# Principled Learning-to-Communicate with Quasi-Classical Information Structures
**arXiv**：[2603.03664v1](https://arxiv.org/abs/2603.03664) · [PDF](https://arxiv.org/pdf/2603.03664.pdf)  
**作者**：Xiangyu Liu, Haoyi You, Kaiqing Zhang  

**一句话要点**：提出基于准经典信息结构的学习通信方法，以解决部分可观测多智能体强化学习中的通信问题。

**关键词**：多智能体强化学习, 部分可观测马尔可夫决策过程, 信息结构, 学习通信, 准经典条件, 算法复杂度

## 3 点简述
- 核心问题：在部分可观测环境中，学习通信策略与决策的联合优化，并基于信息结构分类问题。
- 方法要点：形式化准经典学习通信条件，开发可证明的规划和学习算法，确保通信后信息结构保持准经典。
- 实验或效果：为满足条件的准经典学习通信示例建立准多项式时间和样本复杂度，验证算法有效性。

## 摘要（原文）

> Learning-to-communicate (LTC) in partially observable environments has received increasing attention in deep multi-agent reinforcement learning, where the control and communication strategies are jointly learned. Meanwhile, the impact of communication on decision-making has been extensively studied in control theory. In this paper, we seek to formalize and better understand LTC by bridging these two lines of work, through the lens of information structures (ISs). To this end, we formalize LTC in decentralized partially observable Markov decision processes (Dec-POMDPs) under the common-information-based framework from decentralized stochastic control, and classify LTC problems based on the ISs before (additional) information sharing. We first show that non-classical LTCs are computationally intractable in general, and thus focus on quasi-classical (QC) LTCs. We then propose a series of conditions for QC LTCs, under which LTCs preserve the QC IS after information sharing, whereas violating which can cause computational hardness in general. Further, we develop provable planning and learning algorithms for QC LTCs, and establish quasi-polynomial time and sample complexities for several QC LTC examples that satisfy the above conditions. Along the way, we also establish results on the relationship between (strictly) QC IS and the condition of having strategy-independent common-information-based beliefs (SI-CIBs), as well as on solving Dec-POMDPs without computationally intractable oracles but beyond those with SI-CIBs, which may be of independent interest.

