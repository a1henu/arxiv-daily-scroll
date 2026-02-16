---
layout: default
title: When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction
---

# When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction
**arXiv**：[2602.12616v1](https://arxiv.org/abs/2602.12616) · [PDF](https://arxiv.org/pdf/2602.12616.pdf)  
**作者**：Kaizer Rahaman, Jyotirmoy V. Deshmukh, Ashish R. Hota, Lars Lindemann  

**一句话要点**：提出基于生成先验和鲁棒共形预测的规划框架，以在分布偏移下确保自主系统安全。

**关键词**：分布偏移, 共形预测, 模型预测控制, 条件扩散模型, 鲁棒规划, 自主系统安全

## 3 点简述
- 核心问题：自主系统在部署时面临分布偏移，导致训练数据的安全保证失效。
- 方法要点：利用条件扩散模型生成合成数据，结合鲁棒共形预测嵌入MPC，提供概率安全保证。
- 实验或效果：在ORCA模拟器中实证验证了多种分布偏移下的安全性。

## 摘要（原文）

> Autonomous systems operate in environments that may change over time. An example is the control of a self-driving vehicle among pedestrians and human-controlled vehicles whose behavior may change based on factors such as traffic density, road visibility, and social norms. Therefore, the environment encountered during deployment rarely mirrors the environment and data encountered during training -- a phenomenon known as distribution shift -- which can undermine the safety of autonomous systems. Conformal prediction (CP) has recently been used along with data from the training environment to provide prediction regions that capture the behavior of the environment with a desired probability. When embedded within a model predictive controller (MPC), one can provide probabilistic safety guarantees, but only when the deployment and training environments coincide. Once a distribution shift occurs, these guarantees collapse. We propose a planning framework that is robust under distribution shifts by: (i) assuming that the underlying data distribution of the environment is parameterized by a nuisance parameter, i.e., an observable, interpretable quantity such as traffic density, (ii) training a conditional diffusion model that captures distribution shifts as a function of the nuisance parameter, (iii) observing the nuisance parameter online and generating cheap, synthetic data from the diffusion model for the observed nuisance parameter, and (iv) designing an MPC that embeds CP regions constructed from such synthetic data. Importantly, we account for discrepancies between the underlying data distribution and the diffusion model by using robust CP. Thus, the plans computed using robust CP enjoy probabilistic safety guarantees, in contrast with plans obtained from a single, static set of training data. We empirically demonstrate safety under diverse distribution shifts in the ORCA simulator.

