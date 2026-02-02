---
layout: default
title: End-to-end Optimization of Belief and Policy Learning in Shared Autonomy Paradigms
---

# End-to-end Optimization of Belief and Policy Learning in Shared Autonomy Paradigms
**arXiv**：[2601.23285v1](https://arxiv.org/abs/2601.23285) · [PDF](https://arxiv.org/pdf/2601.23285.pdf)  
**作者**：MH Farhadi, Ali Rabiee, Sima Ghafoori, Anna Cetera, Andrew Fisher, Reza Abiri  

**一句话要点**：提出BRACE框架，通过端到端优化贝叶斯意图推断与上下文自适应辅助，提升共享自主系统在非结构化环境中的性能。

**关键词**：共享自主系统, 贝叶斯意图推断, 端到端优化, 上下文自适应辅助, 人机交互, 机器人控制

## 3 点简述
- 核心问题：共享自主系统中静态混合比或分离的意图推断与辅助仲裁导致非结构化环境下性能不佳。
- 方法要点：BRACE框架通过端到端梯度流，联合优化贝叶斯意图推断和上下文自适应辅助策略。
- 实验或效果：在三维评估中，相比SOTA方法，成功率提升6.3%，路径效率提高41%，验证了在复杂目标模糊场景中的优势。

## 摘要（原文）

> Shared autonomy systems require principled methods for inferring user intent and determining appropriate assistance levels. This is a central challenge in human-robot interaction, where systems must be successful while being mindful of user agency. Previous approaches relied on static blending ratios or separated goal inference from assistance arbitration, leading to suboptimal performance in unstructured environments. We introduce BRACE (Bayesian Reinforcement Assistance with Context Encoding), a novel framework that fine-tunes Bayesian intent inference and context-adaptive assistance through an architecture enabling end-to-end gradient flow between intent inference and assistance arbitration. Our pipeline conditions collaborative control policies on environmental context and complete goal probability distributions. We provide analysis showing (1) optimal assistance levels should decrease with goal uncertainty and increase with environmental constraint severity, and (2) integrating belief information into policy learning yields a quadratic expected regret advantage over sequential approaches. We validated our algorithm against SOTA methods (IDA, DQN) using a three-part evaluation progressively isolating distinct challenges of end-effector control: (1) core human-interaction dynamics in a 2D human-in-the-loop cursor task, (2) non-linear dynamics of a robotic arm, and (3) integrated manipulation under goal ambiguity and environmental constraints. We demonstrate improvements over SOTA, achieving 6.3% higher success rates and 41% increased path efficiency, and 36.3% success rate and 87% path efficiency improvement over unassisted control. Our results confirmed that integrated optimization is most beneficial in complex, goal-ambiguous scenarios, and is generalizable across robotic domains requiring goal-directed assistance, advancing the SOTA for adaptive shared autonomy.

