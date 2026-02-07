---
layout: default
title: MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation
---

# MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation
**arXiv**：[2602.05467v1](https://arxiv.org/abs/2602.05467) · [PDF](https://arxiv.org/pdf/2602.05467.pdf)  
**作者**：Dekang Qi, Shuang Zeng, Xinyuan Chang, Feng Xiong, Shichao Xie, Xiaolong Wu, Mu Xu  

**一句话要点**：提出Memory-Execute-Review框架以解决零样本目标导航中成功率和泛化性的平衡问题

**关键词**：零样本目标导航, 视觉语言导航, 记忆-执行-回顾框架, 泛化性提升, 成功率优化

## 3 点简述
- 核心问题：现有视觉语言导航方法在成功率和泛化性上难以兼顾，监督微调方法成功率较高但泛化差，无训练方法泛化好但成功率低。
- 方法要点：设计包含分层记忆模块、执行模块和回顾模块的框架，记忆模块提供信息支持，执行模块负责常规决策，回顾模块处理异常并纠正行为。
- 实验或效果：在4个数据集上，零样本设置下平均成功率比基线方法提升5%，在HM3D_v0.1和HM3D_OVON数据集上分别提升8%和6%，并在MP3D和HM3D_OVON上超越所有无训练和监督微调方法。

## 摘要（原文）

> Visual Language Navigation (VLN) is one of the fundamental capabilities for embodied intelligence and a critical challenge that urgently needs to be addressed. However, existing methods are still unsatisfactory in terms of both success rate (SR) and generalization: Supervised Fine-Tuning (SFT) approaches typically achieve higher SR, while Training-Free (TF) approaches often generalize better, but it is difficult to obtain both simultaneously. To this end, we propose a Memory-Execute-Review framework. It consists of three parts: a hierarchical memory module for providing information support, an execute module for routine decision-making and actions, and a review module for handling abnormal situations and correcting behavior. We validated the effectiveness of this framework on the Object Goal Navigation task. Across 4 datasets, our average SR achieved absolute improvements of 7% and 5% compared to all baseline methods under TF and Zero-Shot (ZS) settings, respectively. On the most commonly used HM3D_v0.1 and the more challenging open vocabulary dataset HM3D_OVON, the SR improved by 8% and 6%, under ZS settings. Furthermore, on the MP3D and HM3D_OVON datasets, our method not only outperformed all TF methods but also surpassed all SFT methods, achieving comprehensive leadership in both SR (5% and 2%) and generalization.

