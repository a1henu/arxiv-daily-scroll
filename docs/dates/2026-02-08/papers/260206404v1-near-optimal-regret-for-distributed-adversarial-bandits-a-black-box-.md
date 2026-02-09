---
layout: default
title: Near-Optimal Regret for Distributed Adversarial Bandits: A Black-Box Approach
---

# Near-Optimal Regret for Distributed Adversarial Bandits: A Black-Box Approach
**arXiv**：[2602.06404v1](https://arxiv.org/abs/2602.06404) · [PDF](https://arxiv.org/pdf/2602.06404.pdf)  
**作者**：Hao Qiu, Mengxiao Zhang, Nicolò Cesa-Bianchi  

**一句话要点**：提出基于黑盒延迟反馈的分布式对抗赌博机算法，实现接近最优的遗憾界

**关键词**：分布式对抗赌博机, 黑盒延迟反馈, gossip通信, 遗憾界分析, 分布式线性赌博机, 体积生成器

## 3 点简述
- 研究分布式对抗赌博机问题，多智能体协作最小化全局平均损失，仅观察本地损失
- 算法通过黑盒延迟反馈减少，利用gossip通信，显著改进先前遗憾界，并匹配下界
- 扩展至分布式线性赌博机，获得遗憾界，每轮通信成本低，基于体积生成器

## 摘要（原文）

> We study distributed adversarial bandits, where $N$ agents cooperate to minimize the global average loss while observing only their own local losses. We show that the minimax regret for this problem is $\tildeΘ(\sqrt{(ρ^{-1/2}+K/N)T})$, where $T$ is the horizon, $K$ is the number of actions, and $ρ$ is the spectral gap of the communication matrix. Our algorithm, based on a novel black-box reduction to bandits with delayed feedback, requires agents to communicate only through gossip. It achieves an upper bound that significantly improves over the previous best bound $\tilde{O}(ρ^{-1/3}(KT)^{2/3})$ of Yi and Vojnovic (2023). We complement this result with a matching lower bound, showing that the problem's difficulty decomposes into a communication cost $ρ^{-1/4}\sqrt{T}$ and a bandit cost $\sqrt{KT/N}$. We further demonstrate the versatility of our approach by deriving first-order and best-of-both-worlds bounds in the distributed adversarial setting. Finally, we extend our framework to distributed linear bandits in $R^d$, obtaining a regret bound of $\tilde{O}(\sqrt{(ρ^{-1/2}+1/N)dT})$, achieved with only $O(d)$ communication cost per agent and per round via a volumetric spanner.

