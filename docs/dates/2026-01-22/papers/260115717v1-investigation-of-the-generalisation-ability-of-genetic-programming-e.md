---
layout: default
title: Investigation of the Generalisation Ability of Genetic Programming-evolved Scheduling Rules in Dynamic Flexible Job Shop Scheduling
---

# Investigation of the Generalisation Ability of Genetic Programming-evolved Scheduling Rules in Dynamic Flexible Job Shop Scheduling
**arXiv**：[2601.15717v1](https://arxiv.org/abs/2601.15717) · [PDF](https://arxiv.org/pdf/2601.15717.pdf)  
**作者**：Luyao Zhu, Fangfang Zhang, Yi Mei, Mengjie Zhang  

**一句话要点**：系统研究遗传编程演化调度规则在动态柔性作业车间调度中的跨类型泛化能力

**关键词**：动态柔性作业车间调度, 遗传编程, 调度规则, 泛化能力, 决策点分布, 组合优化

## 3 点简述
- 核心问题：现有研究在相同类型实例上训练和测试遗传编程规则，其跨类型泛化能力未知。
- 方法要点：通过多维度实验分析问题规模、车间参数和数据分布对泛化性能的影响。
- 实验或效果：发现训练实例包含更多作业且决策点分布相似时，泛化能力较好；差异大则性能下降。

## 摘要（原文）

> Dynamic Flexible Job Shop Scheduling (DFJSS) is a complex combinatorial optimisation problem that requires simultaneous machine assignment and operation sequencing decisions in dynamic production environments. Genetic Programming (GP) has been widely applied to automatically evolve scheduling rules for DFJSS. However, existing studies typically train and test GP-evolved rules on DFJSS instances of the same type, which differ only by random seeds rather than by structural characteristics, leaving their cross-type generalisation ability largely unexplored. To address this gap, this paper systematically investigates the generalisation ability of GP-evolved scheduling rules under diverse DFJSS conditions. A series of experiments are conducted across multiple dimensions, including problem scale (i.e., the number of machines and jobs), key job shop parameters (e.g., utilisation level), and data distributions, to analyse how these factors influence GP performance on unseen instance types. The results show that good generalisation occurs when the training instances contain more jobs than the test instances while keeping the number of machines fixed, and when both training and test instances have similar scales or job shop parameters. Further analysis reveals that the number and distribution of decision points in DFJSS instances play a crucial role in explaining these performance differences. Similar decision point distributions lead to better generalisation, whereas significant discrepancies result in a marked degradation of performance. Overall, this study provides new insights into the generalisation ability of GP in DFJSS and highlights the necessity of evolving more generalisable GP rules capable of handling heterogeneous DFJSS instances effectively.

