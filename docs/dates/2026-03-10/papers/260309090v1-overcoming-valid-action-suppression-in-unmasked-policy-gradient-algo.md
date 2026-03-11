---
layout: default
title: Overcoming Valid Action Suppression in Unmasked Policy Gradient Algorithms
---

# Overcoming Valid Action Suppression in Unmasked Policy Gradient Algorithms
**arXiv**：[2603.09090v1](https://arxiv.org/abs/2603.09090) · [PDF](https://arxiv.org/pdf/2603.09090.pdf)  
**作者**：Renos Zabounidis, Roy Siegelmann, Mohamad Qadri, Woojun Kim, Simon Stepputtis, Katia P. Sycara  

**一句话要点**：提出无掩码策略梯度算法中有效动作抑制问题的理论分析与解决方案

**关键词**：强化学习, 动作掩码, 策略梯度, 有效动作抑制, 熵正则化, 可行性分类

## 3 点简述
- 识别无掩码训练在状态依赖动作有效性环境中的系统性失败模式：未访问状态的有效动作被抑制
- 证明软最大策略中参数共享导致有效动作概率指数衰减，并分析熵正则化的权衡
- 实验验证深度网络特征对齐条件，并在Craftax等环境中展示可行性分类的部署效果

## 摘要（原文）

> In reinforcement learning environments with state-dependent action validity, action masking consistently outperforms penalty-based handling of invalid actions, yet existing theory only shows that masking preserves the policy gradient theorem. We identify a distinct failure mode of unmasked training: it systematically suppresses valid actions at states the agent has not yet visited. This occurs because gradients pushing down invalid actions at visited states propagate through shared network parameters to unvisited states where those actions are valid. We prove that for softmax policies with shared features, when an action is invalid at visited states but valid at an unvisited state $s^*$, the probability $π(a \mid s^*)$ is bounded by exponential decay due to parameter sharing and the zero-sum identity of softmax logits. This bound reveals that entropy regularization trades off between protecting valid actions and sample efficiency, a tradeoff that masking eliminates. We validate empirically that deep networks exhibit the feature alignment condition required for suppression, and experiments on Craftax, Craftax-Classic, and MiniHack confirm the predicted exponential suppression and demonstrate that feasibility classification enables deployment without oracle masks.

