---
layout: default
title: MMT-ARD: Multimodal Multi-Teacher Adversarial Distillation for Robust Vision-Language Models
---

# MMT-ARD: Multimodal Multi-Teacher Adversarial Distillation for Robust Vision-Language Models
**arXiv**：[2511.17448v1](https://arxiv.org/abs/2511.17448) · [PDF](https://arxiv.org/pdf/2511.17448.pdf)  
**作者**：Yuqi Li, Junhao Dong, Chuanguang Yang, Shiping Wen, Piotr Koniusz, Tingwen Huang, Yingli Tian, Yew-Soon Ong  

**一句话要点**：提出多模态多教师对抗蒸馏框架以增强视觉语言模型的对抗鲁棒性

**关键词**：视觉语言模型, 对抗鲁棒性, 知识蒸馏, 多教师学习, 模态融合, 动态权重分配

## 3 点简述
- 视觉语言模型在安全关键应用中对抗鲁棒性不足，传统单教师方法知识多样性有限
- 采用双教师知识融合架构，动态权重分配和自适应加权函数平衡模态间知识转移
- 在ImageNet和零样本基准上，ViT-B-32模型鲁棒准确率提升4.32%，训练效率提高2.3倍

## 摘要（原文）

> Vision-Language Models (VLMs) are increasingly deployed in safety-critical applications, making their adversarial robustness a crucial concern. While adversarial knowledge distillation has shown promise in transferring robustness from teacher to student models, traditional single-teacher approaches suffer from limited knowledge diversity, slow convergence, and difficulty in balancing robustness and accuracy. To address these challenges, we propose MMT-ARD: a Multimodal Multi-Teacher Adversarial Robust Distillation framework. Our key innovation is a dual-teacher knowledge fusion architecture that collaboratively optimizes clean feature preservation and robust feature enhancement. To better handle challenging adversarial examples, we introduce a dynamic weight allocation strategy based on teacher confidence, enabling adaptive focus on harder samples. Moreover, to mitigate bias among teachers, we design an adaptive sigmoid-based weighting function that balances the strength of knowledge transfer across modalities. Extensive experiments on ImageNet and zero-shot benchmarks demonstrate that MMT-ARD improves robust accuracy by +4.32% and zero-shot accuracy by +3.5% on the ViT-B-32 model, while achieving a 2.3x increase in training efficiency over traditional single-teacher methods. These results highlight the effectiveness and scalability of MMT-ARD in enhancing the adversarial robustness of multimodal large models. Our codes are available at https://github.com/itsnotacie/MMT-ARD.

