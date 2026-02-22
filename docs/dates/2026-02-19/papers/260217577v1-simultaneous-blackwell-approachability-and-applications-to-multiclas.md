---
layout: default
title: Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction
---

# Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction
**arXiv**：[2602.17577v1](https://arxiv.org/abs/2602.17577) · [PDF](https://arxiv.org/pdf/2602.17577.pdf)  
**作者**：Lunjia Hu, Kevin Tian, Chutong Yang  

**一句话要点**：提出多类别全预测框架，扩展二元全预测至多类别无限比较器场景。

**关键词**：多类别全预测, Blackwell逼近, 样本复杂度, 在线学习, 比较器族, 损失函数族

## 3 点简述
- 研究多类别全预测问题，要求对损失函数族和无限比较器族提供次优性界。
- 设计算法扩展二元全预测至多类别，样本复杂度或遗憾界约为ε^{-(k+1)}。
- 引入同时Blackwell逼近框架，用于解决多集合耦合动作的逼近问题。

## 摘要（原文）

> Omniprediction is a learning problem that requires suboptimality bounds for each of a family of losses $\mathcal{L}$ against a family of comparator predictors $\mathcal{C}$. We initiate the study of omniprediction in a multiclass setting, where the comparator family $\mathcal{C}$ may be infinite. Our main result is an extension of the recent binary omniprediction algorithm of [OKK25] to the multiclass setting, with sample complexity (in statistical settings) or regret horizon (in online settings) $\approx \varepsilon^{-(k+1)}$, for $\varepsilon$-omniprediction in a $k$-class prediction problem. En route to proving this result, we design a framework of potential broader interest for solving Blackwell approachability problems where multiple sets must simultaneously be approached via coupled actions.

