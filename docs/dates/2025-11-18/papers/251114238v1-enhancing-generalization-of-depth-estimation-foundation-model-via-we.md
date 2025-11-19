---
layout: default
title: Enhancing Generalization of Depth Estimation Foundation Model via Weakly-Supervised Adaptation with Regularization
---

# Enhancing Generalization of Depth Estimation Foundation Model via Weakly-Supervised Adaptation with Regularization
**arXiv**：[2511.14238v1](https://arxiv.org/abs/2511.14238) · [PDF](https://arxiv.org/pdf/2511.14238.pdf)  
**作者**：Yan Huang, Yongyi Su, Xin Lin, Le Zhang, Xun Xu  

**一句话要点**：提出WeSTAR框架，通过弱监督自适应增强深度估计基础模型的泛化能力

**关键词**：单目深度估计, 基础模型适应, 弱监督学习, 参数高效微调, 泛化增强

## 3 点简述
- 核心问题：基础模型在零样本深度估计中泛化不足，需利用下游数据提升性能
- 方法要点：结合自训练、语义感知归一化、弱监督和权重正则化进行参数高效适应
- 实验或效果：在多样分布外数据集上验证，提升泛化并达到先进性能

## 摘要（原文）

> The emergence of foundation models has substantially advanced zero-shot generalization in monocular depth estimation (MDE), as exemplified by the Depth Anything series. However, given access to some data from downstream tasks, a natural question arises: can the performance of these models be further improved? To this end, we propose WeSTAR, a parameter-efficient framework that performs Weakly supervised Self-Training Adaptation with Regularization, designed to enhance the robustness of MDE foundation models in unseen and diverse domains. We first adopt a dense self-training objective as the primary source of structural self-supervision. To further improve robustness, we introduce semantically-aware hierarchical normalization, which exploits instance-level segmentation maps to perform more stable and multi-scale structural normalization. Beyond dense supervision, we introduce a cost-efficient weak supervision in the form of pairwise ordinal depth annotations to further guide the adaptation process, which enforces informative ordinal constraints to mitigate local topological errors. Finally, a weight regularization loss is employed to anchor the LoRA updates, ensuring training stability and preserving the model's generalizable knowledge. Extensive experiments on both realistic and corrupted out-of-distribution datasets under diverse and challenging scenarios demonstrate that WeSTAR consistently improves generalization and achieves state-of-the-art performance across a wide range of benchmarks.

