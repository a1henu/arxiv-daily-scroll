---
layout: default
title: Sample Complexity of Average-Reward Q-Learning: From Single-agent to Federated Reinforcement Learning
---

# Sample Complexity of Average-Reward Q-Learning: From Single-agent to Federated Reinforcement Learning
**arXiv**：[2601.13642v1](https://arxiv.org/abs/2601.13642) · [PDF](https://arxiv.org/pdf/2601.13642.pdf)  
**作者**：Yuchen Jiao, Jiin Woo, Gen Li, Gauri Joshi, Yuejie Chi  

**一句话要点**：提出平均奖励Q学习算法，在单智能体与联邦场景下建立首个样本复杂度理论保证

**关键词**：平均奖励强化学习, Q学习算法, 样本复杂度分析, 联邦强化学习, 马尔可夫决策过程, 通信效率

## 3 点简述
- 研究平均奖励MDP中Q学习的样本复杂度理论，填补现有理论空白
- 针对单智能体场景，通过参数优化将样本复杂度改进至Õ(\|S\|\|A\|‖h*‖³/ε³)
- 在联邦场景中证明协作可将单智能体样本复杂度降低M倍，仅需Õ(‖h*‖/ε)通信轮次

## 摘要（原文）

> Average-reward reinforcement learning offers a principled framework for long-term decision-making by maximizing the mean reward per time step. Although Q-learning is a widely used model-free algorithm with established sample complexity in discounted and finite-horizon Markov decision processes (MDPs), its theoretical guarantees for average-reward settings remain limited. This work studies a simple but effective Q-learning algorithm for average-reward MDPs with finite state and action spaces under the weakly communicating assumption, covering both single-agent and federated scenarios. For the single-agent case, we show that Q-learning with carefully chosen parameters achieves sample complexity $\widetilde{O}\left(\frac{\|\mathcal{S}\|\|\mathcal{A}\|\\|h^{\star}\\|_{\mathsf{sp}}^3}{\varepsilon^3}\right)$, where $\\|h^{\star}\\|_{\mathsf{sp}}$ is the span norm of the bias function, improving previous results by at least a factor of $\frac{\\|h^{\star}\\|_{\mathsf{sp}}^2}{\varepsilon^2}$. In the federated setting with $M$ agents, we prove that collaboration reduces the per-agent sample complexity to $\widetilde{O}\left(\frac{\|\mathcal{S}\|\|\mathcal{A}\|\\|h^{\star}\\|_{\mathsf{sp}}^3}{M\varepsilon^3}\right)$, with only $\widetilde{O}\left(\frac{\\|h^{\star}\\|_{\mathsf{sp}}}{\varepsilon}\right)$ communication rounds required. These results establish the first federated Q-learning algorithm for average-reward MDPs, with provable efficiency in both sample and communication complexity.

