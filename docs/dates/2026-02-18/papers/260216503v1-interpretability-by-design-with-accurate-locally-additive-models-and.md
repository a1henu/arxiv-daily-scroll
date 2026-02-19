---
layout: default
title: Interpretability-by-Design with Accurate Locally Additive Models and Conditional Feature Effects
---

# Interpretability-by-Design with Accurate Locally Additive Models and Conditional Feature Effects
**arXiv**：[2602.16503v1](https://arxiv.org/abs/2602.16503) · [PDF](https://arxiv.org/pdf/2602.16503.pdf)  
**作者**：Vasilis Gkolemis, Loukas Kavouras, Dimitrios Kyriakopoulos, Konstantinos Tsopelas, Dimitrios Rontogiannis, Giuseppe Casalicchio, Theodore Dalamagas, Christos Diou  

**一句话要点**：提出条件性加性局部模型以平衡可解释性与准确性，解决广义加性模型在交互作用下的欠拟合问题。

**关键词**：条件性加性局部模型, 可解释机器学习, 特征交互作用, 蒸馏训练, 模型审计, 局部可加性

## 3 点简述
- 核心问题：广义加性模型在数据存在交互作用时欠拟合，而GA²Ms添加交互作用牺牲可解释性。
- 方法要点：CALMs允许每个特征有多个单变量形状函数，在不同输入区域激活，通过简单逻辑条件定义区域以保持局部可加性。
- 实验或效果：在分类和回归任务中，CALMs性能优于GAMs，准确性与GA²Ms相当，提供准确性-可解释性权衡。

## 摘要（原文）

> Generalized additive models (GAMs) offer interpretability through independent univariate feature effects but underfit when interactions are present in data. GA$^2$Ms add selected pairwise interactions which improves accuracy, but sacrifices interpretability and limits model auditing. We propose \emph{Conditionally Additive Local Models} (CALMs), a new model class, that balances the interpretability of GAMs with the accuracy of GA$^2$Ms. CALMs allow multiple univariate shape functions per feature, each active in different regions of the input space. These regions are defined independently for each feature as simple logical conditions (thresholds) on the features it interacts with. As a result, effects remain locally additive while varying across subregions to capture interactions. We further propose a principled distillation-based training pipeline that identifies homogeneous regions with limited interactions and fits interpretable shape functions via region-aware backfitting. Experiments on diverse classification and regression tasks show that CALMs consistently outperform GAMs and achieve accuracy comparable with GA$^2$Ms. Overall, CALMs offer a compelling trade-off between predictive accuracy and interpretability.

