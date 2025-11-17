---
layout: default
title: Multimodal Posterior Sampling-based Uncertainty in PD-L1 Segmentation from H&E Images
---

# Multimodal Posterior Sampling-based Uncertainty in PD-L1 Segmentation from H&E Images
**arXiv**：[2511.11486v1](https://arxiv.org/abs/2511.11486) · [PDF](https://arxiv.org/pdf/2511.11486.pdf)  
**作者**：Roman Kinakh, Gonzalo R. Ríos-Muñoz, Arrate Muñoz-Barrutia  

**一句话要点**：提出基于多模态后验采样的贝叶斯分割框架，从H&E图像预测PD-L1表达以解决资源密集问题。

**关键词**：贝叶斯分割, 多模态后验采样, PD-L1表达预测, H&E图像分析, 不确定性估计

## 3 点简述
- 核心问题：PD-L1表达评估依赖资源密集的免疫组化方法，需更高效替代方案。
- 方法要点：基于nnUNet-v2，通过循环训练采样模型检查点近似后验，实现分割和不确定性估计。
- 实验或效果：在肺鳞癌数据集上，平均Dice分数0.805，平均IoU 0.709，不确定性图与分割误差相关。

## 摘要（原文）

> Accurate assessment of PD-L1 expression is critical for guiding immunotherapy, yet current immunohistochemistry (IHC) based methods are resource-intensive. We present nnUNet-B: a Bayesian segmentation framework that infers PD-L1 expression directly from H&E-stained histology images using Multimodal Posterior Sampling (MPS). Built upon nnUNet-v2, our method samples diverse model checkpoints during cyclic training to approximate the posterior, enabling both accurate segmentation and epistemic uncertainty estimation via entropy and standard deviation. Evaluated on a dataset of lung squamous cell carcinoma, our approach achieves competitive performance against established baselines with mean Dice Score and mean IoU of 0.805 and 0.709, respectively, while providing pixel-wise uncertainty maps. Uncertainty estimates show strong correlation with segmentation error, though calibration remains imperfect. These results suggest that uncertainty-aware H&E-based PD-L1 prediction is a promising step toward scalable, interpretable biomarker assessment in clinical workflows.

