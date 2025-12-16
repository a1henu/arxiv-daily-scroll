---
layout: default
title: DP-CSGP: Differentially Private Stochastic Gradient Push with Compressed Communication
---

# DP-CSGP: Differentially Private Stochastic Gradient Push with Compressed Communication
**arXiv**：[2512.13583v1](https://arxiv.org/abs/2512.13583) · [PDF](https://arxiv.org/pdf/2512.13583.pdf)  
**作者**：Zehan Zhu, Heng Zhao, Yan Huang, Joey Tianyi Zhou, Shouling Ji, Jinming Xu  

**一句话要点**：提出DP-CSGP算法，在定向图去中心化学习中实现差分隐私与压缩通信的高效结合。

**关键词**：差分隐私, 去中心化学习, 压缩通信, 随机梯度推送, 定向图, 非凸优化

## 3 点简述
- 针对去中心化学习在定向图中兼顾隐私保护与通信效率的挑战。
- 通过差分隐私随机梯度推送与压缩通信技术，在非凸平滑目标下保持紧致效用界。
- 实验表明，在相同隐私预算下，相比精确通信方法，显著降低通信成本并保持模型精度。

## 摘要（原文）

> In this paper, we propose a Differentially Private Stochastic Gradient Push with Compressed communication (termed DP-CSGP) for decentralized learning over directed graphs. Different from existing works, the proposed algorithm is designed to maintain high model utility while ensuring both rigorous differential privacy (DP) guarantees and efficient communication. For general non-convex and smooth objective functions, we show that the proposed algorithm achieves a tight utility bound of $\mathcal{O}\left( \sqrt{d\log \left( \frac{1}δ \right)}/(\sqrt{n}Jε) \right)$ ($J$ and $d$ are the number of local samples and the dimension of decision variables, respectively) with $\left(ε, δ\right)$-DP guarantee for each node, matching that of decentralized counterparts with exact communication. Extensive experiments on benchmark tasks show that, under the same privacy budget, DP-CSGP achieves comparable model accuracy with significantly lower communication cost than existing decentralized counterparts with exact communication.

