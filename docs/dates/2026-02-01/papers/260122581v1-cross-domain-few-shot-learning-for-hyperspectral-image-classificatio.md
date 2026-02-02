---
layout: default
title: Cross-Domain Few-Shot Learning for Hyperspectral Image Classification Based on Mixup Foundation Model
---

# Cross-Domain Few-Shot Learning for Hyperspectral Image Classification Based on Mixup Foundation Model
**arXiv**：[2601.22581v1](https://arxiv.org/abs/2601.22581) · [PDF](https://arxiv.org/pdf/2601.22581.pdf)  
**作者**：Naeem Paeedeh, Mahardhika Pratama, Ary Shiddiqi, Zehong Cao, Mukesh Prasad, Wisnu Jatmiko  

**一句话要点**：提出MIFOMO模型，基于混合增强基础模型解决高光谱图像跨域少样本分类问题。

**关键词**：高光谱图像分类, 跨域少样本学习, 基础模型, 混合增强, 域适应, 标签平滑

## 3 点简述
- 现有方法依赖外部噪声数据增强，参数多易过拟合，未利用基础模型泛化能力。
- MIFOMO结合遥感基础模型、凝聚投影快速适应、混合域适应和标签平滑，提升跨域性能。
- 实验显示MIFOMO优于先前方法，最高提升14%，代码已开源供复现研究。

## 摘要（原文）

> Although cross-domain few-shot learning (CDFSL) for hyper-spectral image (HSI) classification has attracted significant research interest, existing works often rely on an unrealistic data augmentation procedure in the form of external noise to enlarge the sample size, thus greatly simplifying the issue of data scarcity. They involve a large number of parameters for model updates, being prone to the overfitting problem. To the best of our knowledge, none has explored the strength of the foundation model, having strong generalization power to be quickly adapted to downstream tasks. This paper proposes the MIxup FOundation MOdel (MIFOMO) for CDFSL of HSI classifications. MIFOMO is built upon the concept of a remote sensing (RS) foundation model, pre-trained across a large scale of RS problems, thus featuring generalizable features. The notion of coalescent projection (CP) is introduced to quickly adapt the foundation model to downstream tasks while freezing the backbone network. The concept of mixup domain adaptation (MDM) is proposed to address the extreme domain discrepancy problem. Last but not least, the label smoothing concept is implemented to cope with noisy pseudo-label problems. Our rigorous experiments demonstrate the advantage of MIFOMO, where it beats prior arts with up to 14% margin. The source code of MIFOMO is open-sourced in https://github.com/Naeem- Paeedeh/MIFOMO for reproducibility and convenient further study.

