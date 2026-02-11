---
layout: default
title: Enhancing Affine Maximizer Auctions with Correlation-Aware Payment
---

# Enhancing Affine Maximizer Auctions with Correlation-Aware Payment
**arXiv**：[2602.09455v1](https://arxiv.org/abs/2602.09455) · [PDF](https://arxiv.org/pdf/2602.09455.pdf)  
**作者**：Haoran Sun, Xuanzhi Xia, Xu Chu, Xiaotie Deng  

**一句话要点**：提出相关性感知支付增强仿射最大化拍卖，以解决估值相关分布下表达受限问题。

**关键词**：拍卖机制设计, 相关性感知支付, 仿射最大化拍卖, 激励兼容性, 约束优化, 收益优化

## 3 点简述
- 仿射最大化拍卖在估值相关分布中表达受限，影响收益。
- 引入相关性感知支付，保持激励兼容性，并形式化为约束优化问题。
- 实验显示算法能近似最优收益，且个体理性违规程度低。

## 摘要（原文）

> Affine Maximizer Auctions (AMAs), a generalized mechanism family from VCG, are widely used in automated mechanism design due to their inherent dominant-strategy incentive compatibility (DSIC) and individual rationality (IR). However, as the payment form is fixed, AMA's expressiveness is restricted, especially in distributions where bidders' valuations are correlated. In this paper, we propose Correlation-Aware AMA (CA-AMA), a novel framework that augments AMA with a new correlation-aware payment. We show that any CA-AMA preserves the DSIC property and formalize finding optimal CA-AMA as a constraint optimization problem subject to the IR constraint. Then, we theoretically characterize scenarios where classic AMAs can perform arbitrarily poorly compared to the optimal revenue, while the CA-AMA can reach the optimal revenue. For optimizing CA-AMA, we design a practical two-stage training algorithm. We derive that the target function's continuity and the generalization bound on the degree of deviation from strict IR. Finally, extensive experiments showcase that our algorithm can find an approximate optimal CA-AMA in various distributions with improved revenue and a low degree of violation of IR.

