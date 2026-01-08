---
layout: default
title: Investigating Knowledge Distillation Through Neural Networks for Protein Binding Affinity Prediction
---

# Investigating Knowledge Distillation Through Neural Networks for Protein Binding Affinity Prediction
**arXiv**：[2601.03704v1](https://arxiv.org/abs/2601.03704) · [PDF](https://arxiv.org/pdf/2601.03704.pdf)  
**作者**：Wajid Arshad Abbasi, Syed Ali Abbas, Maryum Bibi, Saiqa Andleeb, Muhammad Naveed Akhtar  

**一句话要点**：提出基于知识蒸馏的回归框架，以提升仅用序列数据预测蛋白质结合亲和力的性能。

**关键词**：蛋白质结合亲和力预测, 知识蒸馏, 序列-结构模型, 回归框架, 机器学习

## 3 点简述
- 核心问题：蛋白质结构数据稀缺，限制基于结构的机器学习模型在结合亲和力预测中的应用。
- 方法要点：通过结构信息教师网络指导序列学生网络，利用结合亲和力标签和中间特征表示进行联合监督。
- 实验或效果：在基准数据集上，蒸馏模型显著优于仅序列基线，Pearson相关系数从0.375提升至0.481。

## 摘要（原文）

> The trade-off between predictive accuracy and data availability makes it difficult to predict protein--protein binding affinity accurately. The lack of experimentally resolved protein structures limits the performance of structure-based machine learning models, which generally outperform sequence-based methods. In order to overcome this constraint, we suggest a regression framework based on knowledge distillation that uses protein structural data during training and only needs sequence data during inference. The suggested method uses binding affinity labels and intermediate feature representations to jointly supervise the training of a sequence-based student network under the guidance of a structure-informed teacher network. Leave-One-Complex-Out (LOCO) cross-validation was used to assess the framework on a non-redundant protein--protein binding affinity benchmark dataset. A maximum Pearson correlation coefficient (P_r) of 0.375 and an RMSE of 2.712 kcal/mol were obtained by sequence-only baseline models, whereas a P_r of 0.512 and an RMSE of 2.445 kcal/mol were obtained by structure-based models. With a P_r of 0.481 and an RMSE of 2.488 kcal/mol, the distillation-based student model greatly enhanced sequence-only performance. Improved agreement and decreased bias were further confirmed by thorough error analyses. With the potential to close the performance gap between sequence-based and structure-based models as larger datasets become available, these findings show that knowledge distillation is an efficient method for transferring structural knowledge to sequence-based predictors. The source code for running inference with the proposed distillation-based binding affinity predictor can be accessed at https://github.com/wajidarshad/ProteinAffinityKD.

