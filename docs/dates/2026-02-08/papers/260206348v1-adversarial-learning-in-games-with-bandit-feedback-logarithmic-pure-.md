---
layout: default
title: Adversarial Learning in Games with Bandit Feedback: Logarithmic Pure-Strategy Maximin Regret
---

# Adversarial Learning in Games with Bandit Feedback: Logarithmic Pure-Strategy Maximin Regret
**arXiv**：[2602.06348v1](https://arxiv.org/abs/2602.06348) · [PDF](https://arxiv.org/pdf/2602.06348.pdf)  
**作者**：Shinji Ito, Haipeng Luo, Arnab Maiti, Taira Tsuchiya, Yue Wu  

**一句话要点**：提出Tsallis-INF和Maximin-UCB算法，在零和博弈的bandit反馈下实现对数级纯策略极大极小遗憾。

**关键词**：零和博弈, bandit反馈, 对抗学习, 极大极小遗憾, 对数遗憾, 双线性博弈

## 3 点简述
- 研究零和博弈在bandit反馈下的对抗学习，目标是最小化纯策略极大极小遗憾。
- 在无信息bandit设置中，Tsallis-INF算法实现O(c log T)遗憾，并证明c依赖的必要性。
- 在有信息bandit设置中，Maximin-UCB算法实现O(c' log T)遗憾，c'可能远小于c，并推广到双线性博弈。

## 摘要（原文）

> Learning to play zero-sum games is a fundamental problem in game theory and machine learning. While significant progress has been made in minimizing external regret in the self-play settings or with full-information feedback, real-world applications often force learners to play against unknown, arbitrary opponents and restrict learners to bandit feedback where only the payoff of the realized action is observable. In such challenging settings, it is well-known that $Ω(\sqrt{T})$ external regret is unavoidable (where T is the number of rounds). To overcome this barrier, we investigate adversarial learning in zero-sum games under bandit feedback, aiming to minimize the deficit against the maximin pure strategy -- a metric we term Pure-Strategy Maximin Regret.
>   We analyze this problem under two bandit feedback models: uninformed (only the realized reward is revealed) and informed (both the reward and the opponent's action are revealed). For uninformed bandit learning of normal-form games, we show that the Tsallis-INF algorithm achieves $O(c \log T)$ instance-dependent regret with a game-dependent parameter $c$. Crucially, we prove an information-theoretic lower bound showing that the dependence on c is necessary. To overcome this hardness, we turn to the informed setting and introduce Maximin-UCB, which obtains another regret bound of the form $O(c' \log T)$ for a different game-dependent parameter $c'$ that could potentially be much smaller than $c$. Finally, we generalize both results to bilinear games over an arbitrary, large action set, proposing Tsallis-FTRL-SPM and Maximin-LinUCB for the uninformed and informed setting respectively and establishing similar game-dependent logarithmic regret bounds.

