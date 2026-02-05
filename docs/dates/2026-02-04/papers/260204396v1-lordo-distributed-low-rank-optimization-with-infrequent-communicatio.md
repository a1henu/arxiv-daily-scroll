---
layout: default
title: LoRDO: Distributed Low-Rank Optimization with Infrequent Communication
---

# LoRDO: Distributed Low-Rank Optimization with Infrequent Communication
**arXiv**：[2602.04396v1](https://arxiv.org/abs/2602.04396) · [PDF](https://arxiv.org/pdf/2602.04396.pdf)  
**作者**：Andrej Jovanović, Alex Iacob, Mher Safaryan, Ionut-Vlad Modoranu, Lorenzo Sani, William F. Shen, Xinchi Qiu, Dan Alistarh, Nicholas D. Lane  

**一句话要点**：提出LoRDO框架，结合低秩优化与低频通信以解决分布式训练中的带宽瓶颈问题。

**关键词**：分布式训练, 低秩优化, 低频通信, 优化器状态, 模型训练效率, 带宽瓶颈

## 3 点简述
- 核心问题：分布式训练中，DDP受限于互联带宽，低频通信策略仍受优化器状态的内存和通信需求限制。
- 方法要点：LoRDO统一低秩优化与低频同步，引入全秩拟双曲更新以恢复子空间探索，避免低秩投影限制优化轨迹。
- 实验或效果：在125M-720M模型规模的语言建模和下游任务中，实现与低秩DDP近似的性能，通信减少约10倍，并在低内存设置中表现更佳。

## 摘要（原文）

> Distributed training of foundation models via $\texttt{DDP}$ is limited by interconnect bandwidth. While infrequent communication strategies reduce synchronization frequency, they remain bottlenecked by the memory and communication requirements of optimizer states. Low-rank optimizers can alleviate these constraints; however, in the local-update regime, workers lack access to the full-batch gradients required to compute low-rank projections, which degrades performance. We propose $\texttt{LoRDO}$, a principled framework unifying low-rank optimization with infrequent synchronization. We first demonstrate that, while global projections based on pseudo-gradients are theoretically superior, they permanently restrict the optimization trajectory to a low-rank subspace. To restore subspace exploration, we introduce a full-rank quasi-hyperbolic update. $\texttt{LoRDO}$ achieves near-parity with low-rank $\texttt{DDP}$ in language modeling and downstream tasks at model scales of $125$M--$720$M, while reducing communication by $\approx 10 \times$. Finally, we show that $\texttt{LoRDO}$ improves performance even more in very low-memory settings with small rank/batch size.

