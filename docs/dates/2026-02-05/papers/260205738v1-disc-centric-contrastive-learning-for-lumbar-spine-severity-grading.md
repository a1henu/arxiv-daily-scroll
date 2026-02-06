---
layout: default
title: Disc-Centric Contrastive Learning for Lumbar Spine Severity Grading
---

# Disc-Centric Contrastive Learning for Lumbar Spine Severity Grading
**arXiv**：[2602.05738v1](https://arxiv.org/abs/2602.05738) · [PDF](https://arxiv.org/pdf/2602.05738.pdf)  
**作者**：Sajjan Acharya, Pralisha Kansakar  

**一句话要点**：提出基于椎间盘对比学习的方法，用于腰椎管狭窄症的自动严重程度分级。

**关键词**：腰椎管狭窄症分级, 对比学习, 椎间盘定位, 医学影像分析, 加权焦点损失

## 3 点简述
- 核心问题：从矢状T2加权MRI自动评估腰椎管狭窄症的严重程度，需处理图像外观差异和类别不平衡。
- 方法要点：采用对比预训练结合椎间盘级微调，通过辅助回归任务定位椎间盘，并使用加权焦点损失。
- 实验或效果：相比从头监督训练，平衡准确率达78.1%，严重到正常误分类率降至2.13%。

## 摘要（原文）

> This work examines a disc-centric approach for automated severity grading of lumbar spinal stenosis from sagittal T2-weighted MRI. The method combines contrastive pretraining with disc-level fine-tuning, using a single anatomically localized region of interest per intervertebral disc. Contrastive learning is employed to help the model focus on meaningful disc features and reduce sensitivity to irrelevant differences in image appearance. The framework includes an auxiliary regression task for disc localization and applies weighted focal loss to address class imbalance. Experiments demonstrate a 78.1% balanced accuracy and a reduced severe-to-normal misclassification rate of 2.13% compared with supervised training from scratch. Detecting discs with moderate severity can still be challenging, but focusing on disc-level features provides a practical way to assess the lumbar spinal stenosis.

