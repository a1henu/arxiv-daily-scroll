---
layout: default
title: Why Do Unlearnable Examples Work: A Novel Perspective of Mutual Information
---

# Why Do Unlearnable Examples Work: A Novel Perspective of Mutual Information
**arXiv**：[2603.03725v1](https://arxiv.org/abs/2603.03725) · [PDF](https://arxiv.org/pdf/2603.03725.pdf)  
**作者**：Yifan Zhu, Yibo Miao, Yinpeng Dong, Xiao-Shan Gao  

**一句话要点**：提出基于互信息减少的不可学习示例方法，以增强数据隐私保护效果。

**关键词**：不可学习示例, 互信息减少, 数据隐私保护, 协方差减少, 深度学习安全

## 3 点简述
- 核心问题：现有不可学习示例方法依赖经验启发，缺乏理论解释，难以有效提升。
- 方法要点：从互信息减少视角分析，证明有效示例降低干净与污染特征间互信息，提出最大化类内特征余弦相似度以减少协方差。
- 实验或效果：广泛实验显示，该方法显著优于先前方法，即使在防御机制下也有效。

## 摘要（原文）

> The volume of freely scraped data on the Internet has driven the tremendous success of deep learning. Along with this comes the growing concern about data privacy and security. Numerous methods for generating unlearnable examples have been proposed to prevent data from being illicitly learned by unauthorized deep models by impeding generalization. However, the existing approaches primarily rely on empirical heuristics, making it challenging to enhance unlearnable examples with solid explanations. In this paper, we analyze and improve unlearnable examples from a novel perspective: mutual information reduction. We demonstrate that effective unlearnable examples always decrease mutual information between clean features and poisoned features, and when the network gets deeper, the unlearnability goes better together with lower mutual information. Further, we prove from a covariance reduction perspective that minimizing the conditional covariance of intra-class poisoned features reduces the mutual information between distributions. Based on the theoretical results, we propose a novel unlearnable method called Mutual Information Unlearnable Examples (MI-UE) that reduces covariance by maximizing the cosine similarity among intra-class features, thus impeding the generalization effectively. Extensive experiments demonstrate that our approach significantly outperforms the previous methods, even under defense mechanisms.

