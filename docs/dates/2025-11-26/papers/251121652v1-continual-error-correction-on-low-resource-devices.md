---
layout: default
title: Continual Error Correction on Low-Resource Devices
---

# Continual Error Correction on Low-Resource Devices
**arXiv**：[2511.21652v1](https://arxiv.org/abs/2511.21652) · [PDF](https://arxiv.org/pdf/2511.21652.pdf)  
**作者**：Kirill Paramonov, Mete Ozay, Aristeidis Mystakidis, Nikolaos Tsalikidis, Dimitrios Sotos, Anastasios Drosou, Dimitrios Tzovaras, Hyunjun Kim, Kiseok Chang, Sangdok Mo, Namwoong Kim, Woojong Yoo, Jijoong Moon, Umberto Michieli  

**一句话要点**：提出基于原型更新的持续错误校正系统，解决低资源设备AI预测错误问题

**关键词**：持续学习, 错误校正, 原型分类, 知识蒸馏, 低资源设备, 少样本学习

## 3 点简述
- 核心问题：AI模型在资源受限设备上预测错误频发，现有方案缺乏高效校正机制
- 方法要点：结合服务器端知识蒸馏和设备端原型更新，实现无需重训练的少样本校正
- 实验或效果：在Food-101和Flowers-102数据集上，单次校正成功率超50%，遗忘率低于0.02%

## 摘要（原文）

> The proliferation of AI models in everyday devices has highlighted a critical challenge: prediction errors that degrade user experience. While existing solutions focus on error detection, they rarely provide efficient correction mechanisms, especially for resource-constrained devices. We present a novel system enabling users to correct AI misclassifications through few-shot learning, requiring minimal computational resources and storage. Our approach combines server-side foundation model training with on-device prototype-based classification, enabling efficient error correction through prototype updates rather than model retraining. The system consists of two key components: (1) a server-side pipeline that leverages knowledge distillation to transfer robust feature representations from foundation models to device-compatible architectures, and (2) a device-side mechanism that enables ultra-efficient error correction through prototype adaptation. We demonstrate our system's effectiveness on both image classification and object detection tasks, achieving over 50% error correction in one-shot scenarios on Food-101 and Flowers-102 datasets while maintaining minimal forgetting (less than 0.02%) and negligible computational overhead. Our implementation, validated through an Android demonstration app, proves the system's practicality in real-world scenarios.

