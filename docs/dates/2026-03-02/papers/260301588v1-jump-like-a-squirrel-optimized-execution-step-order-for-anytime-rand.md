---
layout: default
title: Jump Like A Squirrel: Optimized Execution Step Order for Anytime Random Forest Inference
---

# Jump Like A Squirrel: Optimized Execution Step Order for Anytime Random Forest Inference
**arXiv**：[2603.01588v1](https://arxiv.org/abs/2603.01588) · [PDF](https://arxiv.org/pdf/2603.01588.pdf)  
**作者**：Daniel Biebert, Christian Hakert, Kay Heider, Daniel Kuhse, Sebastian Buschjäger, Jian-Jia Chen  

**一句话要点**：提出优化执行步序方法，实现随机森林在资源受限系统中的随时推理

**关键词**：随机森林, 随时算法, 资源受限系统, 步序优化, 启发式算法

## 3 点简述
- 核心问题：资源受限系统中随机森林推理时间不足，需保留预测置信度的随时算法
- 方法要点：在决策树单步粒度实现随时算法，设计步序优化平均准确率，包括最优序和启发式松鼠序
- 实验或效果：评估显示后向松鼠序性能接近最优序，优于其他步序

## 摘要（原文）

> Due to their efficiency and small size, decision trees and random forests are popular machine learning models used for classification on resource-constrained systems. In such systems, the available execution time for inference in a random forest might not be sufficient for a complete model execution. Ideally, the already gained prediction confidence should be retained. An anytime algorithm is designed to be able to be aborted anytime, while giving a result with an increasing quality over time. Previous approaches have realized random forests as anytime algorithms on the granularity of trees, stopping after some but not all trees of a forest have been executed. However, due to the way decision trees subdivide the sample space in every step, an increase in prediction quality is achieved with every additional step in one tree. In this paper, we realize decision trees and random forest as anytime algorithms on the granularity of single steps in trees. This approach opens a design space to define the step order in a forest, which has the potential to optimize the mean accuracy. We propose the Optimal Order, which finds a step order with a maximal mean accuracy in exponential runtime and the polynomial runtime heuristics Forward Squirrel Order and Backward Squirrel Order, which greedily maximize the accuracy for each additional step taken down and up the trees, respectively.
>   Our evaluation shows, that the Backward Squirrel Order performs $\sim94\%$ as well as the Optimal Order and $\sim99\%$ as well as all other step orders.

