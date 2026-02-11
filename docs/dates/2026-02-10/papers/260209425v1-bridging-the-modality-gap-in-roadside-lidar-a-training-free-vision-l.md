---
layout: default
title: Bridging the Modality Gap in Roadside LiDAR: A Training-Free Vision-Language Model Framework for Vehicle Classification
---

# Bridging the Modality Gap in Roadside LiDAR: A Training-Free Vision-Language Model Framework for Vehicle Classification
**arXiv**：[2602.09425v1](https://arxiv.org/abs/2602.09425) · [PDF](https://arxiv.org/pdf/2602.09425.pdf)  
**作者**：Yiqiao Li, Bo Shang, Jie Wei  

**一句话要点**：提出无需训练的视觉-语言模型框架，通过深度感知图像生成桥接模态差距，实现路边LiDAR细粒度卡车分类。

**关键词**：视觉-语言模型, LiDAR分类, 模态桥接, 细粒度识别, 冷启动策略, 智能交通系统

## 3 点简述
- 核心问题：路边LiDAR稀疏点云与密集2D图像间的模态差距限制了视觉-语言模型在细粒度卡车分类中的应用。
- 方法要点：设计深度感知图像生成流程，将稀疏LiDAR扫描转换为深度编码2D视觉代理，无需参数微调。
- 实验或效果：在20类车辆数据集上，每类仅需16-30个示例即达到竞争性准确率，并作为冷启动策略提升轻量监督模型。

## 摘要（原文）

> Fine-grained truck classification is critical for intelligent transportation systems (ITS), yet current LiDAR-based methods face scalability challenges due to their reliance on supervised deep learning and labor-intensive manual annotation. Vision-Language Models (VLMs) offer promising few-shot generalization, but their application to roadside LiDAR is limited by a modality gap between sparse 3D point clouds and dense 2D imagery. We propose a framework that bridges this gap by adapting off-the-shelf VLMs for fine-grained truck classification without parameter fine-tuning. Our new depth-aware image generation pipeline applies noise removal, spatial and temporal registration, orientation rectification, morphological operations, and anisotropic smoothing to transform sparse, occluded LiDAR scans into depth-encoded 2D visual proxies. Validated on a real-world dataset of 20 vehicle classes, our approach achieves competitive classification accuracy with as few as 16-30 examples per class, offering a scalable alternative to data-intensive supervised baselines. We further observe a "Semantic Anchor" effect: text-based guidance regularizes performance in ultra-low-shot regimes $k < 4$, but degrades accuracy in more-shot settings due to semantic mismatch. Furthermore, we demonstrate the efficacy of this framework as a Cold Start strategy, using VLM-generated labels to bootstrap lightweight supervised models. Notably, the few-shot VLM-based model achieves over correct classification rate of 75 percent for specific drayage categories (20ft, 40ft, and 53ft containers) entirely without the costly training or fine-tuning, significantly reducing the intensive demands of initial manual labeling, thus achieving a method of practical use in ITS applications.

