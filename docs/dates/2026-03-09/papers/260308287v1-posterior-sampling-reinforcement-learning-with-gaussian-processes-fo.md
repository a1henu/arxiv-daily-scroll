---
layout: default
title: Posterior Sampling Reinforcement Learning with Gaussian Processes for Continuous Control: Sublinear Regret Bounds for Unbounded State Spaces
---

# Posterior Sampling Reinforcement Learning with Gaussian Processes for Continuous Control: Sublinear Regret Bounds for Unbounded State Spaces
**arXiv**：[2603.08287v1](https://arxiv.org/abs/2603.08287) · [PDF](https://arxiv.org/pdf/2603.08287.pdf)  
**作者**：Hamish Flynn, Joe Watson, Ingmar Posner, Jan Peters  

## 摘要（原文）

> We analyze the Bayesian regret of the Gaussian process posterior sampling reinforcement learning (GP-PSRL) algorithm. Posterior sampling is an effective heuristic for decision-making under uncertainty that has been used to develop successful algorithms for a variety of continuous control problems. However, theoretical work on GP-PSRL is limited. All known regret bounds either fail to achieve a tight dependence on a kernel-dependent quantity called the maximum information gain or fail to properly account for the fact that the set of possible system states is unbounded. Through a recursive application of the Borell-Tsirelson-Ibragimov-Sudakov inequality, we show that, with high probability, the states actually visited by the algorithm are contained within a ball of near-constant radius. To obtain tight dependence on the maximum information gain, we use the chaining method to control the regret suffered by GP-PSRL. Our main result is a Bayesian regret bound of the order $\widetilde{\mathcal{O}}(H^{3/2}\sqrt{γ_{T/H} T})$, where $H$ is the horizon, $T$ is the number of time steps and $γ_{T/H}$ is the maximum information gain. With this result, we resolve the limitations with prior theoretical work on PSRL, and provide the theoretical foundation and tools for analyzing PSRL in complex settings.

