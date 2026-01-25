---
layout: default
title: DSFedMed: Dual-Scale Federated Medical Image Segmentation via Mutual Distillation Between Foundation and Lightweight Models
---

# DSFedMed: Dual-Scale Federated Medical Image Segmentation via Mutual Distillation Between Foundation and Lightweight Models
**arXiv**：[2601.16073v1](https://arxiv.org/abs/2601.16073) · [PDF](https://arxiv.org/pdf/2601.16073.pdf)  
**作者**：Hanwen Zhang, Qiaojin Shen, Yuxi Liu, Yuesheng Zhu, Guibo Luo  

**一句话要点**：提出DSFedMed框架，通过基础模型与轻量模型间的互蒸馏解决联邦医疗图像分割中的效率与泛化问题。

**关键词**：联邦学习, 医疗图像分割, 知识蒸馏, 基础模型, 轻量模型, 互蒸馏

## 3 点简述
- 核心问题：基础模型在联邦部署中面临高计算、通信和推理成本，难以在资源受限环境中应用。
- 方法要点：采用双尺度联邦框架，通过生成高质量医疗图像和可学习性引导样本选择，实现基础模型与轻量客户端模型间的互蒸馏。
- 实验或效果：在五个医疗图像分割数据集上，平均Dice分数提升2%，通信成本和推理时间减少近90%。

## 摘要（原文）

> Foundation Models (FMs) have demonstrated strong generalization across diverse vision tasks. However, their deployment in federated settings is hindered by high computational demands, substantial communication overhead, and significant inference costs. We propose DSFedMed, a dual-scale federated framework that enables mutual knowledge distillation between a centralized foundation model and lightweight client models for medical image segmentation. To support knowledge distillation, a set of high-quality medical images is generated to replace real public datasets, and a learnability-guided sample selection strategy is proposed to enhance efficiency and effectiveness in dual-scale distillation. This mutual distillation enables the foundation model to transfer general knowledge to lightweight clients, while also incorporating client-specific insights to refine the foundation model. Evaluations on five medical imaging segmentation datasets show that DSFedMed achieves an average 2 percent improvement in Dice score while reducing communication costs and inference time by nearly 90 percent compared to existing federated foundation model baselines. These results demonstrate significant efficiency gains and scalability for resource-limited federated deployments.

