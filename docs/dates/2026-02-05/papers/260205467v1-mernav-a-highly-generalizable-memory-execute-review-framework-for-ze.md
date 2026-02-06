---
layout: default
title: MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation
---

# MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation
**arXiv**：[2602.05467v1](https://arxiv.org/abs/2602.05467) · [PDF](https://arxiv.org/pdf/2602.05467.pdf)  
**作者**：Dekang Qi, Shuang Zeng, Xinyuan Chang, Feng Xiong, Shichao Xie, Xiaolong Wu, Mu Xu  

**一句话要点**：提出Memory-Execute-Review框架以提升零样本物体目标导航的泛化性与成功率

**关键词**：物体目标导航, 零样本学习, 视觉语言导航, 记忆增强框架, 泛化性能提升

## 3 点简述
- 现有视觉语言导航方法在成功率与泛化性间难以兼顾，监督微调方法成功率较高但泛化差，无训练方法泛化好但成功率低。
- 框架包含分层记忆模块提供信息支持、执行模块进行常规决策与行动、回顾模块处理异常并纠正行为。
- 在四个数据集上，零样本设置下平均成功率较基线提升5%，在HM3D_OVON等挑战性数据集上超越所有无训练和监督微调方法。

## 摘要（原文）

> Visual Language Navigation (VLN) is one of the fundamental capabilities for embodied intelligence and a critical challenge that urgently needs to be addressed. However, existing methods are still unsatisfactory in terms of both success rate (SR) and generalization: Supervised Fine-Tuning (SFT) approaches typically achieve higher SR, while Training-Free (TF) approaches often generalize better, but it is difficult to obtain both simultaneously. To this end, we propose a Memory-Execute-Review framework. It consists of three parts: a hierarchical memory module for providing information support, an execute module for routine decision-making and actions, and a review module for handling abnormal situations and correcting behavior. We validated the effectiveness of this framework on the Object Goal Navigation task. Across 4 datasets, our average SR achieved absolute improvements of 7% and 5% compared to all baseline methods under TF and Zero-Shot (ZS) settings, respectively. On the most commonly used HM3D_v0.1 and the more challenging open vocabulary dataset HM3D_OVON, the SR improved by 8% and 6%, under ZS settings. Furthermore, on the MP3D and HM3D_OVON datasets, our method not only outperformed all TF methods but also surpassed all SFT methods, achieving comprehensive leadership in both SR (5% and 2%) and generalization.

