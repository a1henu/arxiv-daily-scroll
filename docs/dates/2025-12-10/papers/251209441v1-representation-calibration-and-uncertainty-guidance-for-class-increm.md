---
layout: default
title: Representation Calibration and Uncertainty Guidance for Class-Incremental Learning based on Vision Language Model
---

# Representation Calibration and Uncertainty Guidance for Class-Incremental Learning based on Vision Language Model
**arXiv**：[2512.09441v1](https://arxiv.org/abs/2512.09441) · [PDF](https://arxiv.org/pdf/2512.09441.pdf)  
**作者**：Jiantao Tan, Peixian Ma, Tong Yu, Wentao Zhang, Ruixuan Wang  

**一句话要点**：提出基于视觉语言模型的类增量学习框架，通过表示校准和不确定性指导缓解跨任务类别混淆

**关键词**：类增量学习, 视觉语言模型, 表示校准, 不确定性指导, 图像分类, 跨任务学习

## 3 点简述
- 核心问题：类增量学习中跨任务类别混淆，现有视觉语言模型方法难以区分不同任务学习的类别
- 方法要点：使用任务特定适配器学习新知识，基于轻量投影器混合的跨任务表示校准策略统一特征空间，开发不确定性指导的推理策略选择最佳图像特征
- 实验或效果：在多个数据集和设置下进行广泛实验，相比现有方法展示出优越性能

## 摘要（原文）

> Class-incremental learning requires a learning system to continually learn knowledge of new classes and meanwhile try to preserve previously learned knowledge of old classes. As current state-of-the-art methods based on Vision-Language Models (VLMs) still suffer from the issue of differentiating classes across learning tasks. Here a novel VLM-based continual learning framework for image classification is proposed. In this framework, task-specific adapters are added to the pre-trained and frozen image encoder to learn new knowledge, and a novel cross-task representation calibration strategy based on a mixture of light-weight projectors is used to help better separate all learned classes in a unified feature space, alleviating class confusion across tasks. In addition, a novel inference strategy guided by prediction uncertainty is developed to more accurately select the most appropriate image feature for class prediction. Extensive experiments on multiple datasets under various settings demonstrate the superior performance of our method compared to existing ones.

