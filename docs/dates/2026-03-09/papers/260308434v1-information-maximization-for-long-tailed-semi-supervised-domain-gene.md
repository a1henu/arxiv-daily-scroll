---
layout: default
title: Information Maximization for Long-Tailed Semi-Supervised Domain Generalization
---

# Information Maximization for Long-Tailed Semi-Supervised Domain Generalization
**arXiv**：[2603.08434v1](https://arxiv.org/abs/2603.08434) · [PDF](https://arxiv.org/pdf/2603.08434.pdf)  
**作者**：Leo Fillioux, Omprakash Chakraborty, Quentin Gopée, Pierre Marza, Paul-Henry Cournède, Stergios Christodoulidis, Maria Vakalopoulou, Ismail Ben Ayed, Jose Dolz  

**一句话要点**：提出IMaX方法以解决长尾半监督域泛化中的类别不平衡问题

**关键词**：半监督域泛化, 长尾分布, 互信息最大化, α-熵目标, 类别不平衡

## 3 点简述
- 核心问题：现有半监督域泛化方法在长尾类别分布下性能严重下降
- 方法要点：基于InfoMax原则最大化特征与潜在标签的互信息，引入α-熵目标缓解类别平衡偏差
- 实验或效果：IMaX可无缝集成到先进方法中，在两个图像模态上一致提升性能

## 摘要（原文）

> Semi-supervised domain generalization (SSDG) has recently emerged as an appealing alternative to tackle domain generalization when labeled data is scarce but unlabeled samples across domains are abundant. In this work, we identify an important limitation that hampers the deployment of state-of-the-art methods on more challenging but practical scenarios. In particular, state-of-the-art SSDG severely suffers in the presence of long-tailed class distributions, an arguably common situation in real-world settings. To alleviate this limitation, we propose IMaX, a simple yet effective objective based on the well-known InfoMax principle adapted to the SSDG scenario, where the Mutual Information (MI) between the learned features and latent labels is maximized, constrained by the supervision from the labeled samples. Our formulation integrates an α-entropic objective, which mitigates the class-balance bias encoded in the standard marginal entropy term of the MI, thereby better handling arbitrary class distributions. IMaX can be seamlessly plugged into recent state-of-the-art SSDG, consistently enhancing their performance, as demonstrated empirically across two different image modalities.

