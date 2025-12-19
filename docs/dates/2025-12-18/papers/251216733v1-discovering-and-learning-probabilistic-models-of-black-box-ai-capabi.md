---
layout: default
title: Discovering and Learning Probabilistic Models of Black-Box AI Capabilities
---

# Discovering and Learning Probabilistic Models of Black-Box AI Capabilities
**arXiv**：[2512.16733v1](https://arxiv.org/abs/2512.16733) · [PDF](https://arxiv.org/pdf/2512.16733.pdf)  
**作者**：Daniel Bramblett, Rushang Karia, Adrian Ciotinga, Ruthvick Suresh, Pulkit Verma, YooJung Choi, Siddharth Srivastava  

**一句话要点**：提出基于PDDL和蒙特卡洛树搜索的方法，以学习黑盒AI系统的概率规划能力模型。

**关键词**：黑盒AI建模, 概率规划模型, 蒙特卡洛树搜索, PDDL表示, 序列决策安全

## 3 点简述
- 核心问题：黑盒AI系统在序列决策中缺乏可解释的能力表示，需确保安全部署。
- 方法要点：使用PDDL风格表示和蒙特卡洛树搜索，通过系统测试任务生成和假设空间剪枝学习模型。
- 实验或效果：理论证明模型正确性、完备性和收敛性，多系统实验验证方法范围、效率和准确性。

## 摘要（原文）

> Black-box AI (BBAI) systems such as foundational models are increasingly being used for sequential decision making. To ensure that such systems are safe to operate and deploy, it is imperative to develop efficient methods that can provide a sound and interpretable representation of the BBAI's capabilities. This paper shows that PDDL-style representations can be used to efficiently learn and model an input BBAI's planning capabilities. It uses the Monte-Carlo tree search paradigm to systematically create test tasks, acquire data, and prune the hypothesis space of possible symbolic models. Learned models describe a BBAI's capabilities, the conditions under which they can be executed, and the possible outcomes of executing them along with their associated probabilities. Theoretical results show soundness, completeness and convergence of the learned models. Empirical results with multiple BBAI systems illustrate the scope, efficiency, and accuracy of the presented methods.

