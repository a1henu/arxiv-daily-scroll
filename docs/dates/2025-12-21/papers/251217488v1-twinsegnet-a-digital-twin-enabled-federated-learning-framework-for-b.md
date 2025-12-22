---
layout: default
title: TwinSegNet: A Digital Twin-Enabled Federated Learning Framework for Brain Tumor Analysis
---

# TwinSegNet: A Digital Twin-Enabled Federated Learning Framework for Brain Tumor Analysis
**arXiv**：[2512.17488v1](https://arxiv.org/abs/2512.17488) · [PDF](https://arxiv.org/pdf/2512.17488.pdf)  
**作者**：Almustapha A. Wakili, Adamu Hussaini, Abubakar A. Musa, Woosub Jung, Wei Yu  

**一句话要点**：提出TwinSegNet联邦学习框架，结合数字孪生实现隐私保护的脑肿瘤分割。

**关键词**：脑肿瘤分割, 联邦学习, 数字孪生, ViT-UNet模型, 隐私保护

## 3 点简述
- 核心问题：集中式深度学习在脑肿瘤分割中引发隐私担忧并限制跨机构泛化。
- 方法要点：集成混合ViT-UNet模型，通过数字孪生个性化微调，保护数据隐私。
- 实验或效果：在九个异构MRI数据集上验证，Dice分数高达0.90%，敏感性和特异性超90%。

## 摘要（原文）

> Brain tumor segmentation is critical in diagnosis and treatment planning for the disease. Yet, current deep learning methods rely on centralized data collection, which raises privacy concerns and limits generalization across diverse institutions. In this paper, we propose TwinSegNet, which is a privacy-preserving federated learning framework that integrates a hybrid ViT-UNet model with personalized digital twins for accurate and real-time brain tumor segmentation. Our architecture combines convolutional encoders with Vision Transformer bottlenecks to capture local and global context. Each institution fine-tunes the global model of private data to form its digital twin. Evaluated on nine heterogeneous MRI datasets, including BraTS 2019-2021 and custom tumor collections, TwinSegNet achieves high Dice scores (up to 0.90%) and sensitivity/specificity exceeding 90%, demonstrating robustness across non-independent and identically distributed (IID) client distributions. Comparative results against centralized models such as TumorVisNet highlight TwinSegNet's effectiveness in preserving privacy without sacrificing performance. Our approach enables scalable, personalized segmentation for multi-institutional clinical settings while adhering to strict data confidentiality requirements.

