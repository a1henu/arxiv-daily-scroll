---
layout: default
title: Meta-learners for few-shot weakly-supervised optic disc and cup segmentation on fundus images
---

# Meta-learners for few-shot weakly-supervised optic disc and cup segmentation on fundus images
**arXiv**：[2512.15061v1](https://arxiv.org/abs/2512.15061) · [PDF](https://arxiv.org/pdf/2512.15061.pdf)  
**作者**：Pandega Abyan Zumarsyah, Igi Ardiyanto, Hanung Adi Nugroho  

**一句话要点**：提出Omni元训练与高效版本以解决少样本弱监督视盘视杯分割问题

**关键词**：少样本学习, 弱监督分割, 元学习, 视盘视杯分割, 青光眼诊断, 稀疏标注

## 3 点简述
- 核心问题：青光眼诊断中视盘视杯分割标注数据有限，需少样本弱监督方法
- 方法要点：引入Omni元训练平衡数据使用并多样化样本数，开发高效版本降低计算成本
- 实验或效果：EO-ProtoSeg在多个数据集上优于原方法，仅需一张稀疏标注图像，参数少于两百万

## 摘要（原文）

> This study develops meta-learners for few-shot weakly-supervised segmentation (FWS) to address the challenge of optic disc (OD) and optic cup (OC) segmentation for glaucoma diagnosis with limited labeled fundus images. We significantly improve existing meta-learners by introducing Omni meta-training which balances data usage and diversifies the number of shots. We also develop their efficient versions that reduce computational costs. In addition, we develop sparsification techniques that generate more customizable and representative scribbles and other sparse labels. After evaluating multiple datasets, we find that Omni and efficient versions outperform the original versions, with the best meta-learner being Efficient Omni ProtoSeg (EO-ProtoSeg). It achieves intersection over union (IoU) scores of 88.15% for OD and 71.17% for OC on the REFUGE dataset using just one sparsely labeled image, outperforming few-shot and semi-supervised methods which require more labeled images. Its best performance reaches 86.80% for OD and 71.78%for OC on DRISHTIGS, 88.21% for OD and 73.70% for OC on REFUGE, 80.39% for OD and 52.65% for OC on REFUGE. EO-ProtoSeg is comparable to unsupervised domain adaptation methods yet much lighter with less than two million parameters and does not require any retraining.

