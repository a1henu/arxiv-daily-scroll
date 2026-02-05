---
layout: default
title: Interval-Based AUC (iAUC): Extending ROC Analysis to Uncertainty-Aware Classification
---

# Interval-Based AUC (iAUC): Extending ROC Analysis to Uncertainty-Aware Classification
**arXiv**：[2602.04775v1](https://arxiv.org/abs/2602.04775) · [PDF](https://arxiv.org/pdf/2602.04775.pdf)  
**作者**：Yuqi Li, Matthew M. Engelhard  

**一句话要点**：提出区间AUC框架以解决高风险预测中不确定性评估的不足

**关键词**：区间预测, 不确定性评估, ROC分析, 选择性预测, 高风险决策

## 3 点简述
- 标准ROC/AUC无法评估区间预测的不确定性影响
- 引入AUC_L和AUC_U作为理论最优AUC的上下界
- 实验验证框架在真实数据集上的正确性和实用性

## 摘要（原文）

> In high-stakes risk prediction, quantifying uncertainty through interval-valued predictions is essential for reliable decision-making. However, standard evaluation tools like the receiver operating characteristic (ROC) curve and the area under the curve (AUC) are designed for point scores and fail to capture the impact of predictive uncertainty on ranking performance. We propose an uncertainty-aware ROC framework specifically for interval-valued predictions, introducing two new measures: $AUC_L$ and $AUC_U$. This framework enables an informative three-region decomposition of the ROC plane, partitioning pairwise rankings into correct, incorrect, and uncertain orderings. This approach naturally supports selective prediction by allowing models to abstain from ranking cases with overlapping intervals, thereby optimizing the trade-off between abstention rate and discriminative reliability. We prove that under valid class-conditional coverage, $AUC_L$ and $AUC_U$ provide formal lower and upper bounds on the theoretical optimal AUC ($AUC^*$), characterizing the physical limit of achievable discrimination. The proposed framework applies broadly to interval-valued prediction models, regardless of the interval construction method. Experiments on real-world benchmark datasets, using bootstrap-based intervals as one instantiation, validate the framework's correctness and demonstrate its practical utility for uncertainty-aware evaluation and decision-making.

