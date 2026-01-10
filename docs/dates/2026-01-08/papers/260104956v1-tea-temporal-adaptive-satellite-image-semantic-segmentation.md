---
layout: default
title: TEA: Temporal Adaptive Satellite Image Semantic Segmentation
---

# TEA: Temporal Adaptive Satellite Image Semantic Segmentation
**arXiv**：[2601.04956v1](https://arxiv.org/abs/2601.04956) · [PDF](https://arxiv.org/pdf/2601.04956.pdf)  
**作者**：Juyuan Kang, Hao Zhu, Yan Zhu, Wei Zhang, Jianing Chen, Tianxiang Xiao, Yike Ma, Hao Jiang, Feng Dai  

**一句话要点**：提出TEA方法以增强卫星图像时间序列语义分割在不同时序长度下的泛化能力

**关键词**：卫星图像时间序列, 语义分割, 时序自适应, 知识蒸馏, 泛化能力, 农业遥感

## 3 点简述
- 核心问题：现有方法在固定时序长度下表现良好，但泛化到不同长度场景时分割效果显著下降
- 方法要点：引入教师模型传递全局序列知识，通过嵌入、原型和软标签指导学生模型，并动态聚合以减轻遗忘
- 实验或效果：在常见基准测试中，对不同时序长度的输入带来显著改进，代码将公开

## 摘要（原文）

> Crop mapping based on satellite images time-series (SITS) holds substantial economic value in agricultural production settings, in which parcel segmentation is an essential step. Existing approaches have achieved notable advancements in SITS segmentation with predetermined sequence lengths. However, we found that these approaches overlooked the generalization capability of models across scenarios with varying temporal length, leading to markedly poor segmentation results in such cases. To address this issue, we propose TEA, a TEmporal Adaptive SITS semantic segmentation method to enhance the model's resilience under varying sequence lengths. We introduce a teacher model that encapsulates the global sequence knowledge to guide a student model with adaptive temporal input lengths. Specifically, teacher shapes the student's feature space via intermediate embedding, prototypes and soft label perspectives to realize knowledge transfer, while dynamically aggregating student model to mitigate knowledge forgetting. Finally, we introduce full-sequence reconstruction as an auxiliary task to further enhance the quality of representations across inputs of varying temporal lengths. Through extensive experiments, we demonstrate that our method brings remarkable improvements across inputs of different temporal lengths on common benchmarks. Our code will be publicly available.

