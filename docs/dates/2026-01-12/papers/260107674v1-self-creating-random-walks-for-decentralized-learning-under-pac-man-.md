---
layout: default
title: Self-Creating Random Walks for Decentralized Learning under Pac-Man Attacks
---

# Self-Creating Random Walks for Decentralized Learning under Pac-Man Attacks
**arXiv**：[2601.07674v1](https://arxiv.org/abs/2601.07674) · [PDF](https://arxiv.org/pdf/2601.07674.pdf)  
**作者**：Xingran Chen, Parimal Parag, Rohit Bhagat, Salim El Rouayheb  

**一句话要点**：提出CREATE-IF-LATE算法以抵御去中心化学习中的Pac-Man攻击

**关键词**：去中心化学习, 随机漫步, 对抗攻击, 分布式系统, 随机梯度下降

## 3 点简述
- 核心问题：随机漫步算法易受恶意节点Pac-Man攻击，导致学习过程中断
- 方法要点：CIL算法实现自创建随机漫步，保证种群不灭绝和收敛性
- 实验或效果：理论分析验证算法性质，实证结果支持理论发现

## 摘要（原文）

> Random walk (RW)-based algorithms have long been popular in distributed systems due to low overheads and scalability, with recent growing applications in decentralized learning. However, their reliance on local interactions makes them inherently vulnerable to malicious behavior. In this work, we investigate an adversarial threat that we term the ``Pac-Man'' attack, in which a malicious node probabilistically terminates any RW that visits it. This stealthy behavior gradually eliminates active RWs from the network, effectively halting the learning process without triggering failure alarms. To counter this threat, we propose the CREATE-IF-LATE (CIL) algorithm, which is a fully decentralized, resilient mechanism that enables self-creating RWs and prevents RW extinction in the presence of Pac-Man. Our theoretical analysis shows that the CIL algorithm guarantees several desirable properties, such as (i) non-extinction of the RW population, (ii) almost sure boundedness of the RW population, and (iii) convergence of RW-based stochastic gradient descent even in the presence of Pac-Man with a quantifiable deviation from the true optimum. Moreover, the learning process experiences at most a linear time delay due to Pac-Man interruptions and RW regeneration. Our extensive empirical results on both synthetic and public benchmark datasets validate our theoretical findings.

