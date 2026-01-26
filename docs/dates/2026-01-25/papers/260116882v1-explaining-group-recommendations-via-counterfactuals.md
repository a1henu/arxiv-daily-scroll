---
layout: default
title: Explaining Group Recommendations via Counterfactuals
---

# Explaining Group Recommendations via Counterfactuals
**arXiv**：[2601.16882v1](https://arxiv.org/abs/2601.16882) · [PDF](https://arxiv.org/pdf/2601.16882.pdf)  
**作者**：Maria Stratigi, Nikos Bikakis  

**一句话要点**：提出基于反事实的群体推荐解释框架，以增强群体推荐系统的透明度。

**关键词**：群体推荐系统, 反事实解释, 透明度, 公平性度量, 启发式算法

## 3 点简述
- 核心问题：群体推荐系统缺乏透明度，现有解释方法难以处理多用户偏好交互。
- 方法要点：通过移除特定历史交互生成反事实解释，并引入群体效用与公平性度量。
- 实验或效果：在MovieLens和Amazon数据集上验证了效率与解释质量间的权衡。

## 摘要（原文）

> Group recommender systems help users make collective choices but often lack transparency, leaving group members uncertain about why items are suggested. Existing explanation methods focus on individuals, offering limited support for groups where multiple preferences interact. In this paper, we propose a framework for group counterfactual explanations, which reveal how removing specific past interactions would change a group recommendation. We formalize this concept, introduce utility and fairness measures tailored to groups, and design heuristic algorithms, such as Pareto-based filtering and grow-and-prune strategies, for efficient explanation discovery. Experiments on MovieLens and Amazon datasets show clear trade-offs: low-cost methods produce larger, less fair explanations, while other approaches yield concise and balanced results at higher cost. Furthermore, the Pareto-filtering heuristic demonstrates significant efficiency improvements in sparse settings.

