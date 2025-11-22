---
layout: default
title: Externally Validated Multi-Task Learning via Consistency Regularization Using Differentiable BI-RADS Features for Breast Ultrasound Tumor Segmentation
---

# Externally Validated Multi-Task Learning via Consistency Regularization Using Differentiable BI-RADS Features for Breast Ultrasound Tumor Segmentation
**arXiv**：[2511.15968v1](https://arxiv.org/abs/2511.15968) · [PDF](https://arxiv.org/pdf/2511.15968.pdf)  
**作者**：Jingru Zhang, Saed Moradi, Ashirbani Saha  

**一句话要点**：提出一致性正则化方法以解决乳腺超声肿瘤分割中的多任务干扰问题

**关键词**：多任务学习, 一致性正则化, 乳腺超声分割, BI-RADS特征, 外部验证

## 3 点简述
- 多任务学习存在破坏性任务干扰，导致泛化性能下降
- 使用可微分BI-RADS特征进行一致性正则化，减轻分割与分类干扰
- 在外部数据集验证中，分割性能显著优于基线，Dice系数提升明显

## 摘要（原文）

> Multi-task learning can suffer from destructive task interference, where jointly trained models underperform single-task baselines and limit generalization. To improve generalization performance in breast ultrasound-based tumor segmentation via multi-task learning, we propose a novel consistency regularization approach that mitigates destructive interference between segmentation and classification. The consistency regularization approach is composed of differentiable BI-RADS-inspired morphological features. We validated this approach by training all models on the BrEaST dataset (Poland) and evaluating them on three external datasets: UDIAT (Spain), BUSI (Egypt), and BUS-UCLM (Spain). Our comprehensive analysis demonstrates statistically significant (p<0.001) improvements in generalization for segmentation task of the proposed multi-task approach vs. the baseline one: UDIAT, BUSI, BUS-UCLM (Dice coefficient=0.81 vs 0.59, 0.66 vs 0.56, 0.69 vs 0.49, resp.). The proposed approach also achieves state-of-the-art segmentation performance under rigorous external validation on the UDIAT dataset.

