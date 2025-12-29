---
layout: default
title: Scalable Class-Incremental Learning Based on Parametric Neural Collapse
---

# Scalable Class-Incremental Learning Based on Parametric Neural Collapse
**arXiv**：[2512.21845v1](https://arxiv.org/abs/2512.21845) · [PDF](https://arxiv.org/pdf/2512.21845.pdf)  
**作者**：Chuangxin Zhang, Guangfeng Lin, Enhui Zhao, Kaiyang Liao, Yajun Chen  

**一句话要点**：提出基于参数化神经坍缩的可扩展类增量学习方法，以解决模型扩展中的特征差异和类别错位问题。

**关键词**：类增量学习, 神经坍缩, 知识蒸馏, 模型扩展, 特征对齐, 等角紧框架

## 3 点简述
- 核心问题：增量学习中模型扩展导致特征差异和类别分布演化引起的类别错位。
- 方法要点：通过自适应层和动态参数化等角紧框架，实现需求驱动的低成本骨干扩展和特征对齐。
- 实验或效果：在标准基准测试中验证了方法的有效性和效率，代码已开源。

## 摘要（原文）

> Incremental learning often encounter challenges such as overfitting to new data and catastrophic forgetting of old data. Existing methods can effectively extend the model for new tasks while freezing the parameters of the old model, but ignore the necessity of structural efficiency to lead to the feature difference between modules and the class misalignment due to evolving class distributions. To address these issues, we propose scalable class-incremental learning based on parametric neural collapse (SCL-PNC) that enables demand-driven, minimal-cost backbone expansion by adapt-layer and refines the static into a dynamic parametric Equiangular Tight Frame (ETF) framework according to incremental class. This method can efficiently handle the model expansion question with the increasing number of categories in real-world scenarios. Additionally, to counteract feature drift in serial expansion models, the parallel expansion framework is presented with a knowledge distillation algorithm to align features across expansion modules. Therefore, SCL-PNC can not only design a dynamic and extensible ETF classifier to address class misalignment due to evolving class distributions, but also ensure feature consistency by an adapt-layer with knowledge distillation between extended modules. By leveraging neural collapse, SCL-PNC induces the convergence of the incremental expansion model through a structured combination of the expandable backbone, adapt-layer, and the parametric ETF classifier. Experiments on standard benchmarks demonstrate the effectiveness and efficiency of our proposed method. Our code is available at https://github.com/zhangchuangxin71-cyber/dynamic_ ETF2. Keywords: Class incremental learning; Catastrophic forgetting; Neural collapse;Knowledge distillation; Expanded model.

