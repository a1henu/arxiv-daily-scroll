---
layout: default
title: PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning
---

# PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning
**arXiv**：[2512.07342v1](https://arxiv.org/abs/2512.07342) · [PDF](https://arxiv.org/pdf/2512.07342.pdf)  
**作者**：Chen Gong, Zheng Liu, Kecen Li, Tianhao Wang  

**一句话要点**：提出PrivORL方法，利用差分隐私合成离线强化学习数据集以保护隐私。

**关键词**：差分隐私, 离线强化学习, 数据集合成, 扩散模型, 隐私保护

## 3 点简述
- 核心问题：离线强化学习数据集存在隐私泄露风险，需保护敏感信息。
- 方法要点：基于扩散模型和扩散变换器，在差分隐私下合成过渡和轨迹，并引入好奇心驱动预训练。
- 实验或效果：在五个敏感数据集上验证，相比基线在效用和保真度方面表现更优。

## 摘要（原文）

> Recently, offline reinforcement learning (RL) has become a popular RL paradigm. In offline RL, data providers share pre-collected datasets -- either as individual transitions or sequences of transitions forming trajectories -- to enable the training of RL models (also called agents) without direct interaction with the environments. Offline RL saves interactions with environments compared to traditional RL, and has been effective in critical areas, such as navigation tasks. Meanwhile, concerns about privacy leakage from offline RL datasets have emerged.
>   To safeguard private information in offline RL datasets, we propose the first differential privacy (DP) offline dataset synthesis method, PrivORL, which leverages a diffusion model and diffusion transformer to synthesize transitions and trajectories, respectively, under DP. The synthetic dataset can then be securely released for downstream analysis and research. PrivORL adopts the popular approach of pre-training a synthesizer on public datasets, and then fine-tuning on sensitive datasets using DP Stochastic Gradient Descent (DP-SGD). Additionally, PrivORL introduces curiosity-driven pre-training, which uses feedback from the curiosity module to diversify the synthetic dataset and thus can generate diverse synthetic transitions and trajectories that closely resemble the sensitive dataset. Extensive experiments on five sensitive offline RL datasets show that our method achieves better utility and fidelity in both DP transition and trajectory synthesis compared to baselines. The replication package is available at the GitHub repository.

