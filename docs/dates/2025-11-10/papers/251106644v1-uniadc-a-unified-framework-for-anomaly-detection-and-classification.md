---
layout: default
title: UniADC: A Unified Framework for Anomaly Detection and Classification
---

# UniADC: A Unified Framework for Anomaly Detection and Classification
**arXiv**：[2511.06644v1](https://arxiv.org/abs/2511.06644) · [PDF](https://arxiv.org/pdf/2511.06644.pdf)  
**作者**：Ximiao Zhang, Min Xu, Zheng Zhang, Junlin Hu, Xiuzhuang Zhou  

**一句话要点**：提出UniADC统一框架，以解决异常检测与分类任务分离问题。

**关键词**：异常检测, 图像分类, 统一框架, 可控修复, 多任务学习, 少样本学习

## 3 点简述
- 核心问题：现有方法将异常检测与分类视为独立任务，忽略相关性，导致性能不佳。
- 方法要点：使用可控修复网络合成异常图像，结合多任务判别器实现检测与分类。
- 实验或效果：在多个数据集上验证，UniADC在检测、定位和分类方面优于现有方法。

## 摘要（原文）

> In this paper, we introduce the task of unified anomaly detection and
> classification, which aims to simultaneously detect anomalous regions in images
> and identify their specific categories. Existing methods typically treat
> anomaly detection and classification as separate tasks, thereby neglecting
> their inherent correlation, limiting information sharing, and resulting in
> suboptimal performance. To address this, we propose UniADC, a unified anomaly
> detection and classification model that can effectively perform both tasks with
> only a few or even no anomaly images. Specifically, UniADC consists of two key
> components: a training-free controllable inpainting network and a multi-task
> discriminator. The inpainting network can synthesize anomaly images of specific
> categories by repainting normal regions guided by anomaly priors, and can also
> repaint few-shot anomaly samples to augment the available anomaly data. The
> multi-task discriminator is then trained on these synthesized samples, enabling
> precise anomaly detection and classification by aligning fine-grained image
> features with anomaly-category embeddings. We conduct extensive experiments on
> three anomaly detection and classification datasets, including MVTec-FS, MTD,
> and WFDD, and the results demonstrate that UniADC consistently outperforms
> existing methods in anomaly detection, localization, and classification. The
> code is available at https://github.com/cnulab/UniADC.

