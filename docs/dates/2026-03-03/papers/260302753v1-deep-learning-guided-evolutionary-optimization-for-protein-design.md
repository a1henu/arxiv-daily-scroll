---
layout: default
title: Deep learning-guided evolutionary optimization for protein design
---

# Deep learning-guided evolutionary optimization for protein design
**arXiv**：[2603.02753v1](https://arxiv.org/abs/2603.02753) · [PDF](https://arxiv.org/pdf/2603.02753.pdf)  
**作者**：Erik Hartman, Di Tang, Johan Malmström  

**一句话要点**：提出BoGA框架，结合进化搜索与贝叶斯优化，以高效探索蛋白质序列空间进行设计。

**关键词**：蛋白质设计, 贝叶斯优化, 进化算法, 序列空间探索, 肽结合剂设计

## 3 点简述
- 核心问题：蛋白质设计面临序列空间巨大和序列-功能关系复杂的挑战，需高效探索以识别满足特定标准的序列。
- 方法要点：BoGA将遗传算法作为随机提议生成器集成到代理建模循环中，基于先验评估和模型预测优先选择候选序列。
- 实验或效果：在序列和结构设计任务上基准测试，并应用于设计针对肺炎链球菌毒力因子肺炎溶素的肽结合剂，加速高置信度结合剂的发现。

## 摘要（原文）

> Designing novel proteins with desired characteristics remains a significant challenge due to the large sequence space and the complexity of sequence-function relationships. Efficient exploration of this space to identify sequences that meet specific design criteria is crucial for advancing therapeutics and biotechnology. Here, we present BoGA (Bayesian Optimization Genetic Algorithm), a framework that combines evolutionary search with Bayesian optimization to efficiently navigate the sequence space. By integrating a genetic algorithm as a stochastic proposal generator within a surrogate modeling loop, BoGA prioritizes candidates based on prior evaluations and surrogate model predictions, enabling data-efficient optimization. We demonstrate the utility of BoGA through benchmarking on sequence and structure design tasks, followed by its application in designing peptide binders against pneumolysin, a key virulence factor of \textit{Streptococcus pneumoniae}. BoGA accelerates the discovery of high-confidence binders, demonstrating the potential for efficient protein design across diverse objectives. The algorithm is implemented within the BoPep suite and is available under an MIT license at \href{https://github.com/ErikHartman/bopep}{GitHub}.

