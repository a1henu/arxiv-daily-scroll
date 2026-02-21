---
layout: default
title: Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction
---

# Simultaneous Blackwell Approachability and Applications to Multiclass Omniprediction
**arXiv**：[2602.17577v1](https://arxiv.org/abs/2602.17577) · [PDF](https://arxiv.org/pdf/2602.17577.pdf)  
**作者**：Lunjia Hu, Kevin Tian, Chutong Yang  

**一句话要点**：提出多类别全预测框架，通过同时Blackwell逼近解决无限比较器问题。

**关键词**：全预测, 多类别分类, Blackwell逼近, 样本复杂度, 在线学习, 比较器族

## 3 点简述
- 研究多类别全预测问题，要求对无限比较器族提供次优性边界。
- 扩展二元全预测算法至多类别，样本复杂度或遗憾界为ε^{-(k+1)}。
- 设计同时Blackwell逼近框架，支持通过耦合动作逼近多个集合。

## 摘要（原文）

> Omniprediction is a learning problem that requires suboptimality bounds for each of a family of losses $\mathcal{L}$ against a family of comparator predictors $\mathcal{C}$. We initiate the study of omniprediction in a multiclass setting, where the comparator family $\mathcal{C}$ may be infinite. Our main result is an extension of the recent binary omniprediction algorithm of [OKK25] to the multiclass setting, with sample complexity (in statistical settings) or regret horizon (in online settings) $\approx \varepsilon^{-(k+1)}$, for $\varepsilon$-omniprediction in a $k$-class prediction problem. En route to proving this result, we design a framework of potential broader interest for solving Blackwell approachability problems where multiple sets must simultaneously be approached via coupled actions.

