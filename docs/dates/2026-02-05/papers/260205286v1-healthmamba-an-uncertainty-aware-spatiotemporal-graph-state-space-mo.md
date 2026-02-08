---
layout: default
title: HealthMamba: An Uncertainty-aware Spatiotemporal Graph State Space Model for Effective and Reliable Healthcare Facility Visit Prediction
---

# HealthMamba: An Uncertainty-aware Spatiotemporal Graph State Space Model for Effective and Reliable Healthcare Facility Visit Prediction
**arXiv**：[2602.05286v1](https://arxiv.org/abs/2602.05286) · [PDF](https://arxiv.org/pdf/2602.05286.pdf)  
**作者**：Dahai Yu, Lin Jiang, Rongchao Xu, Guang Wang  

**一句话要点**：提出HealthMamba框架，用于准确可靠的医疗设施访问预测，融合时空依赖与不确定性量化。

**关键词**：医疗设施访问预测, 时空图模型, 不确定性量化, 状态空间模型, 资源优化

## 3 点简述
- 核心问题：现有方法忽略医疗设施间的空间依赖，且在异常情况下预测不可靠。
- 方法要点：结合统一时空编码器、GraphMamba模型和不确定性量化模块。
- 实验或效果：在四个真实数据集上，预测准确率提升约6.0%，不确定性量化提升3.5%。

## 摘要（原文）

> Healthcare facility visit prediction is essential for optimizing healthcare resource allocation and informing public health policy. Despite advanced machine learning methods being employed for better prediction performance, existing works usually formulate this task as a time-series forecasting problem without considering the intrinsic spatial dependencies of different types of healthcare facilities, and they also fail to provide reliable predictions under abnormal situations such as public emergencies. To advance existing research, we propose HealthMamba, an uncertainty-aware spatiotemporal framework for accurate and reliable healthcare facility visit prediction. HealthMamba comprises three key components: (i) a Unified Spatiotemporal Context Encoder that fuses heterogeneous static and dynamic information, (ii) a novel Graph State Space Model called GraphMamba for hierarchical spatiotemporal modeling, and (iii) a comprehensive uncertainty quantification module integrating three uncertainty quantification mechanisms for reliable prediction. We evaluate HealthMamba on four large-scale real-world datasets from California, New York, Texas, and Florida. Results show HealthMamba achieves around 6.0% improvement in prediction accuracy and 3.5% improvement in uncertainty quantification over state-of-the-art baselines.

