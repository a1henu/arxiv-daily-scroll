---
layout: default
title: Open Polymer Challenge: Post-Competition Report
---

# Open Polymer Challenge: Post-Competition Report
**arXiv**：[2512.08896v1](https://arxiv.org/abs/2512.08896) · [PDF](https://arxiv.org/pdf/2512.08896.pdf)  
**作者**：Gang Liu, Sobin Alosious, Subhamoy Mahajan, Eric Inae, Yihan Zhu, Yuhan Liu, Renzheng Zhang, Jiaxin Xu, Addison Howard, Ying Li, Tengfei Luo, Meng Jiang  

**一句话要点**：发布首个社区基准Open Polymer Challenge，通过多任务预测加速可持续聚合物材料发现

**关键词**：聚合物信息学, 多任务预测, 数据集基准, 材料发现, 机器学习应用

## 3 点简述
- 核心问题：聚合物信息学缺乏大规模高质量开放数据集，限制机器学习在材料发现中的应用
- 方法要点：构建包含10K聚合物和5种属性的数据集，采用特征增强、迁移学习等技术应对小数据和标签不平衡
- 实验或效果：竞赛揭示数据准备、分布偏移等教训，为未来大规模聚合物数据集提供最佳实践

## 摘要（原文）

> Machine learning (ML) offers a powerful path toward discovering sustainable polymer materials, but progress has been limited by the lack of large, high-quality, and openly accessible polymer datasets. The Open Polymer Challenge (OPC) addresses this gap by releasing the first community-developed benchmark for polymer informatics, featuring a dataset with 10K polymers and 5 properties: thermal conductivity, radius of gyration, density, fractional free volume, and glass transition temperature. The challenge centers on multi-task polymer property prediction, a core step in virtual screening pipelines for materials discovery. Participants developed models under realistic constraints that include small data, label imbalance, and heterogeneous simulation sources, using techniques such as feature-based augmentation, transfer learning, self-supervised pretraining, and targeted ensemble strategies. The competition also revealed important lessons about data preparation, distribution shifts, and cross-group simulation consistency, informing best practices for future large-scale polymer datasets. The resulting models, analysis, and released data create a new foundation for molecular AI in polymer science and are expected to accelerate the development of sustainable and energy-efficient materials. Along with the competition, we release the test dataset at https://www.kaggle.com/datasets/alexliu99/neurips-open-polymer-prediction-2025-test-data. We also release the data generation pipeline at https://github.com/sobinalosious/ADEPT, which simulates more than 25 properties, including thermal conductivity, radius of gyration, and density.

