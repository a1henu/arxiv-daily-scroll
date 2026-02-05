---
layout: default
title: Attack-Resistant Uniform Fairness for Linear and Smooth Contextual Bandits
---

# Attack-Resistant Uniform Fairness for Linear and Smooth Contextual Bandits
**arXiv**：[2602.04125v1](https://arxiv.org/abs/2602.04125) · [PDF](https://arxiv.org/pdf/2602.04125.pdf)  
**作者**：Qingwen Zhang, Wenjia Wang  

**一句话要点**：提出抗攻击的统一公平算法，用于线性和平滑上下文赌博机，以应对策略操纵。

**关键词**：上下文赌博机, 统一公平性, 抗攻击算法, 极小极大遗憾, 策略操纵, 鲁棒性

## 3 点简述
- 研究上下文赌博机在统一(1-δ)-公平约束下的问题，揭示其易受信号操纵的独特脆弱性。
- 开发新算法，实现近似极小极大最优遗憾，同时保持强(1-˜O(1/T))-公平保证，并设计鲁棒变体以抵御攻击。
- 通过数值实验和真实案例验证算法在保持公平性和效率方面的有效性。

## 摘要（原文）

> Modern systems, such as digital platforms and service systems, increasingly rely on contextual bandits for online decision-making; however, their deployment can inadvertently create unfair exposure among arms, undermining long-term platform sustainability and supplier trust. This paper studies the contextual bandit problem under a uniform $(1-δ)$-fairness constraint, and addresses its unique vulnerabilities to strategic manipulation. The fairness constraint ensures that preferential treatment is strictly justified by an arm's actual reward across all contexts and time horizons, using uniformity to prevent statistical loopholes. We develop novel algorithms that achieve (nearly) minimax-optimal regret for both linear and smooth reward functions, while maintaining strong $(1-\tilde{O}(1/T))$-fairness guarantees, and further characterize the theoretically inherent yet asymptotically marginal "price of fairness". However, we reveal that such merit-based fairness becomes uniquely susceptible to signal manipulation. We show that an adversary with a minimal $\tilde{O}(1)$ budget can not only degrade overall performance as in traditional attacks, but also selectively induce insidious fairness-specific failures while leaving conspicuous regret measures largely unaffected. To counter this, we design robust variants incorporating corruption-adaptive exploration and error-compensated thresholding. Our approach yields the first minimax-optimal regret bounds under $C$-budgeted attack while preserving $(1-\tilde{O}(1/T))$-fairness. Numerical experiments and a real-world case demonstrate that our algorithms sustain both fairness and efficiency.

