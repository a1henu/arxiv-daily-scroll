---
layout: default
title: Agency and Architectural Limits: Why Optimization-Based Systems Cannot Be Norm-Responsive
---

# Agency and Architectural Limits: Why Optimization-Based Systems Cannot Be Norm-Responsive
**arXiv**：[2602.23239v1](https://arxiv.org/abs/2602.23239) · [PDF](https://arxiv.org/pdf/2602.23239.pdf)  
**作者**：Radha Sarma  

**一句话要点**：证明基于优化的AI系统无法实现规范响应，提出代理的架构条件以避免部署风险。

**关键词**：规范治理, 优化系统, 代理架构, RLHF模型, 收敛危机, 形式化约束

## 3 点简述
- 核心问题：优化系统如RLHF模型在规范治理上存在形式化不兼容，导致幻觉等失败模式。
- 方法要点：定义代理需满足不可通约性和否定响应性两个架构条件，并分析RLHF的固有约束。
- 实验或效果：揭示部署引发收敛危机，使人类从代理退化为优化器，削弱规范问责。

## 摘要（原文）

> AI systems are increasingly deployed in high-stakes contexts -- medical diagnosis, legal research, financial analysis -- under the assumption they can be governed by norms. This paper demonstrates that assumption is formally invalid for optimization-based systems, specifically Large Language Models trained via Reinforcement Learning from Human Feedback (RLHF). We establish that genuine agency requires two necessary and jointly sufficient architectural conditions: the capacity to maintain certain boundaries as non-negotiable constraints rather than tradeable weights (Incommensurability), and a non-inferential mechanism capable of suspending processing when those boundaries are threatened (Apophatic Responsiveness). These conditions apply across all normative domains.
>   RLHF-based systems are constitutively incompatible with both conditions. The operations that make optimization powerful -- unifying all values on a scalar metric and always selecting the highest-scoring output -- are precisely the operations that preclude normative governance. This incompatibility is not a correctable training bug awaiting a technical fix; it is a formal constraint inherent to what optimization is. Consequently, documented failure modes - sycophancy, hallucination, and unfaithful reasoning - are not accidents but structural manifestations.
>   Misaligned deployment triggers a second-order risk we term the Convergence Crisis: when humans are forced to verify AI outputs under metric pressure, they degrade from genuine agents into criteria-checking optimizers, eliminating the only component in the system capable of normative accountability. Beyond the incompatibility proof, the paper's primary positive contribution is a substrate-neutral architectural specification defining what any system -- biological, artificial, or institutional -- must satisfy to qualify as an agent rather than a sophisticated instrument.

