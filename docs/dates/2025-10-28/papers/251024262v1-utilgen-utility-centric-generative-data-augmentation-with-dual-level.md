---
layout: default
title: UtilGen: Utility-Centric Generative Data Augmentation with Dual-Level Task Adaptation
---

# UtilGen: Utility-Centric Generative Data Augmentation with Dual-Level Task Adaptation
**arXiv**：[2510.24262v1](https://arxiv.org/abs/2510.24262) · [PDF](https://arxiv.org/pdf/2510.24262.pdf)  
**作者**：Jiyu Guo, Shuo Yang, Yiming Huang, Yancheng Long, Xiaobo Xia, Xiu Su, Bo Zhao, Zeke Xie, Liqiang Nie  

**一句话要点**：提出UtilGen框架以解决生成数据增强中忽略任务特定需求的问题

**关键词**：数据增强, 生成模型, 任务适应, 双级优化, 计算机视觉

## 3 点简述
- 核心问题：现有数据增强方法注重数据内在属性，忽视下游任务需求。
- 方法要点：引入权重分配网络和双级优化策略，自适应生成高效用数据。
- 实验或效果：在八个基准数据集上平均准确率提升3.87%，验证任务效用中心的有效性。

## 摘要（原文）

> Data augmentation using generative models has emerged as a powerful paradigm
> for enhancing performance in computer vision tasks. However, most existing
> augmentation approaches primarily focus on optimizing intrinsic data attributes
> -- such as fidelity and diversity -- to generate visually high-quality
> synthetic data, while often neglecting task-specific requirements. Yet, it is
> essential for data generators to account for the needs of downstream tasks, as
> training data requirements can vary significantly across different tasks and
> network architectures. To address these limitations, we propose UtilGen, a
> novel utility-centric data augmentation framework that adaptively optimizes the
> data generation process to produce task-specific, high-utility training data
> via downstream task feedback. Specifically, we first introduce a weight
> allocation network to evaluate the task-specific utility of each synthetic
> sample. Guided by these evaluations, UtilGen iteratively refines the data
> generation process using a dual-level optimization strategy to maximize the
> synthetic data utility: (1) model-level optimization tailors the generative
> model to the downstream task, and (2) instance-level optimization adjusts
> generation policies -- such as prompt embeddings and initial noise -- at each
> generation round. Extensive experiments on eight benchmark datasets of varying
> complexity and granularity demonstrate that UtilGen consistently achieves
> superior performance, with an average accuracy improvement of 3.87% over
> previous SOTA. Further analysis of data influence and distribution reveals that
> UtilGen produces more impactful and task-relevant synthetic data, validating
> the effectiveness of the paradigm shift from visual characteristics-centric to
> task utility-centric data augmentation.

