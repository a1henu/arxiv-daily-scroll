---
layout: default
title: Reliable Abstention under Adversarial Injections: Tight Lower Bounds and New Upper Bounds
---

# Reliable Abstention under Adversarial Injections: Tight Lower Bounds and New Upper Bounds
**arXiv**：[2602.20111v1](https://arxiv.org/abs/2602.20111) · [PDF](https://arxiv.org/pdf/2602.20111.pdf)  
**作者**：Ezra Edelman, Surbhi Goel  

**一句话要点**：提出基于鲁棒见证的潜在框架，在对抗注入模型中实现分布无关的紧下界和新上界。

**关键词**：对抗注入模型, 在线学习, 弃权学习, 鲁棒见证, 证书维度, 半空间学习

## 3 点简述
- 研究对抗注入模型中的在线学习，允许学习者弃权，总误差包括预测错误和弃权错误。
- 证明VC维度1的紧下界Ω(√T)，揭示分布访问与分布无关算法间的根本差距。
- 引入鲁棒见证驱动的潜在框架，基于推理维度和证书维度实例化，应用于二维半空间获得分布无关上界Õ(T^{2/3})。

## 摘要（原文）

> We study online learning in the adversarial injection model introduced by [Goel et al. 2017], where a stream of labeled examples is predominantly drawn i.i.d.\ from an unknown distribution $\mathcal{D}$, but may be interspersed with adversarially chosen instances without the learner knowing which rounds are adversarial. Crucially, labels are always consistent with a fixed target concept (the clean-label setting). The learner is additionally allowed to abstain from predicting, and the total error counts the mistakes whenever the learner decides to predict and incorrect abstentions when it abstains on i.i.d.\ rounds. Perhaps surprisingly, prior work shows that oracle access to the underlying distribution yields $O(d^2 \log T)$ combined error for VC dimension $d$, while distribution-agnostic algorithms achieve only $\tilde{O}(\sqrt{T})$ for restricted classes, leaving open whether this gap is fundamental.
>   We resolve this question by proving a matching $Ω(\sqrt{T})$ lower bound for VC dimension $1$, establishing a sharp separation between the two information regimes. On the algorithmic side, we introduce a potential-based framework driven by \emph{robust witnesses}, small subsets of labeled examples that certify predictions while remaining resilient to adversarial contamination. We instantiate this framework using two combinatorial dimensions: (1) \emph{inference dimension}, yielding combined error $\tilde{O}(T^{1-1/k})$ for classes of inference dimension $k$, and (2) \emph{certificate dimension}, a new relaxation we introduce. As an application, we show that halfspaces in $\mathbb{R}^2$ have certificate dimension $3$, obtaining the first distribution-agnostic bound of $\tilde{O}(T^{2/3})$ for this class. This is notable since [Blum et al. 2021] showed halfspaces are not robustly learnable under clean-label attacks without abstention.

