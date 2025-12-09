---
layout: default
title: Decomposition Sampling for Efficient Region Annotations in Active Learning
---

# Decomposition Sampling for Efficient Region Annotations in Active Learning
**arXiv**：[2512.07606v1](https://arxiv.org/abs/2512.07606) · [PDF](https://arxiv.org/pdf/2512.07606.pdf)  
**作者**：Jingna Qiu, Frauke Wilm, Mathias Öttl, Jonas Utz, Maja Schlereth, Moritz Schillinger, Marc Aubreville, Katharina Breininger  

**一句话要点**：提出分解采样以提升密集预测任务中区域标注效率

**关键词**：主动学习, 密集预测, 区域标注, 分解采样, 医学影像, 少数类采样

## 3 点简述
- 核心问题：现有区域标注选择方法计算成本高、依赖不确定性采样且区域选择不相关
- 方法要点：通过伪标签分解图像为类特定组件，从每类采样区域，结合类置信度指导
- 实验或效果：在ROI分类、2D和3D分割中超越基线，提升少数类区域采样和性能

## 摘要（原文）

> Active learning improves annotation efficiency by selecting the most informative samples for annotation and model training. While most prior work has focused on selecting informative images for classification tasks, we investigate the more challenging setting of dense prediction, where annotations are more costly and time-intensive, especially in medical imaging. Region-level annotation has been shown to be more efficient than image-level annotation for these tasks. However, existing methods for representative annotation region selection suffer from high computational and memory costs, irrelevant region choices, and heavy reliance on uncertainty sampling. We propose decomposition sampling (DECOMP), a new active learning sampling strategy that addresses these limitations. It enhances annotation diversity by decomposing images into class-specific components using pseudo-labels and sampling regions from each class. Class-wise predictive confidence further guides the sampling process, ensuring that difficult classes receive additional annotations. Across ROI classification, 2-D segmentation, and 3-D segmentation, DECOMP consistently surpasses baseline methods by better sampling minority-class regions and boosting performance on these challenging classes. Code is in https://github.com/JingnaQiu/DECOMP.git.

