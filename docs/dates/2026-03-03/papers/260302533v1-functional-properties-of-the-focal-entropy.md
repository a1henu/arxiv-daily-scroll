---
layout: default
title: Functional Properties of the Focal-Entropy
---

# Functional Properties of the Focal-Entropy
**arXiv**：[2603.02533v1](https://arxiv.org/abs/2603.02533) · [PDF](https://arxiv.org/pdf/2603.02533.pdf)  
**作者**：Jaimin Shah, Martina Cardone, Alex Dytso  

**一句话要点**：提出focal-entropy以系统分析focal-loss在类别不平衡分类中的信息论性质。

**关键词**：focal-loss, 类别不平衡分类, 信息论分析, focal-entropy, 概率分布, 计算机视觉

## 3 点简述
- 核心问题：focal-loss在类别不平衡分类中广泛应用，但缺乏系统信息论研究。
- 方法要点：从分布视角研究focal-entropy，分析其有限性、凸性、连续性及渐近特性。
- 实验或效果：证明focal-entropy最小化器的存在与唯一性，揭示其放大中概率、抑制高概率，并在极端不平衡时过度抑制小概率。

## 摘要（原文）

> The focal-loss has become a widely used alternative to cross-entropy in class-imbalanced classification problems, particularly in computer vision. Despite its empirical success, a systematic information-theoretic study of the focal-loss remains incomplete. In this work, we adopt a distributional viewpoint and study the focal-entropy, a focal-loss analogue of the cross-entropy. Our analysis establishes conditions for finiteness, convexity, and continuity of the focal-entropy, and provides various asymptotic characterizations. We prove the existence and uniqueness of the focal-entropy minimizer, describe its structure, and show that it can depart significantly from the data distribution. In particular, we rigorously show that the focal-loss amplifies mid-range probabilities, suppresses high-probability outcomes, and, under extreme class imbalance, induces an over-suppression regime in which very small probabilities are further diminished. These results, which are also experimentally validated, offer a theoretical foundation for understanding the focal-loss and clarify the trade-offs that it introduces when applied to imbalanced learning tasks.

