---
layout: default
title: EnECG: Efficient Ensemble Learning for Electrocardiogram Multi-task Foundation Model
---

# EnECG: Efficient Ensemble Learning for Electrocardiogram Multi-task Foundation Model
**arXiv**：[2511.22935v1](https://arxiv.org/abs/2511.22935) · [PDF](https://arxiv.org/pdf/2511.22935.pdf)  
**作者**：Yuhao Xu, Xiaoda Wang, Jiaying Lu, Sirui Ding, Defu Cao, Huaxiu Yao, Yan Liu, Xiao Hu, Carl Yang  

**一句话要点**：提出EnECG框架，通过集成学习解决心电图多任务分析中的计算效率与特征提取挑战。

**关键词**：心电图分析, 集成学习, 轻量级微调, 混合专家机制, 多任务学习

## 3 点简述
- 核心问题：现有模型未充分利用心电图异常间的关联性，且大规模基础模型在ECG数据上预训练不足，导致全量微调计算成本高。
- 方法要点：集成多个专业基础模型，采用轻量级适配策略（如LoRA）和混合专家机制学习权重，以降低计算开销。
- 实验或效果：实验表明EnECG在减少计算和内存成本的同时，保持了基础模型的强表征能力，提升了预测性能。

## 摘要（原文）

> Electrocardiogram (ECG) analysis plays a vital role in the early detection, monitoring, and management of various cardiovascular conditions. While existing models have achieved notable success in ECG interpretation, they fail to leverage the interrelated nature of various cardiac abnormalities. Conversely, developing a specific model capable of extracting all relevant features for multiple ECG tasks remains a significant challenge. Large-scale foundation models, though powerful, are not typically pretrained on ECG data, making full re-training or fine-tuning computationally expensive. To address these challenges, we propose EnECG(Mixture of Experts-based Ensemble Learning for ECG Multi-tasks), an ensemble-based framework that integrates multiple specialized foundation models, each excelling in different aspects of ECG interpretation. Instead of relying on a single model or single task, EnECG leverages the strengths of multiple specialized models to tackle a variety of ECG-based tasks. To mitigate the high computational cost of full re-training or fine-tuning, we introduce a lightweight adaptation strategy: attaching dedicated output layers to each foundation model and applying Low-Rank Adaptation (LoRA) only to these newly added parameters. We then adopt a Mixture of Experts (MoE) mechanism to learn ensemble weights, effectively combining the complementary expertise of individual models. Our experimental results demonstrate that by minimizing the scope of fine-tuning, EnECG can help reduce computational and memory costs while maintaining the strong representational power of foundation models. This framework not only enhances feature extraction and predictive performance but also ensures practical efficiency for real-world clinical applications. The code is available at https://github.com/yuhaoxu99/EnECG.git.

