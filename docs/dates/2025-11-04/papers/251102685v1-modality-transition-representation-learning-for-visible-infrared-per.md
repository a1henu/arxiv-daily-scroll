---
layout: default
title: Modality-Transition Representation Learning for Visible-Infrared Person Re-Identification
---

# Modality-Transition Representation Learning for Visible-Infrared Person Re-Identification
**arXiv**：[2511.02685v1](https://arxiv.org/abs/2511.02685) · [PDF](https://arxiv.org/pdf/2511.02685.pdf)  
**作者**：Chao Yuan, Zanwu Liu, Guiwei Zhang, Haoxuan Xu, Yujian Zhao, Guanglin Niu, Bo Li  

**一句话要点**：提出模态转换表示学习框架以解决可见光-红外行人重识别中的模态差异问题

**关键词**：可见光-红外行人重识别, 模态转换表示学习, 跨模态特征对齐, 对比学习, 无额外参数设计

## 3 点简述
- 核心问题：可见光与红外模态间存在显著差异，现有方法依赖中间表示但未充分利用
- 方法要点：通过生成中间图像作为转换器，结合对比损失和正则化损失对齐跨模态特征
- 实验或效果：在三个VI-ReID数据集上显著优于现有方法，无需额外参数，推理速度与骨干网络相同

## 摘要（原文）

> Visible-infrared person re-identification (VI-ReID) technique could associate
> the pedestrian images across visible and infrared modalities in the practical
> scenarios of background illumination changes. However, a substantial gap
> inherently exists between these two modalities. Besides, existing methods
> primarily rely on intermediate representations to align cross-modal features of
> the same person. The intermediate feature representations are usually create by
> generating intermediate images (kind of data enhancement), or fusing
> intermediate features (more parameters, lack of interpretability), and they do
> not make good use of the intermediate features. Thus, we propose a novel
> VI-ReID framework via Modality-Transition Representation Learning (MTRL) with a
> middle generated image as a transmitter from visible to infrared modals, which
> are fully aligned with the original visible images and similar to the infrared
> modality. After that, using a modality-transition contrastive loss and a
> modality-query regularization loss for training, which could align the
> cross-modal features more effectively. Notably, our proposed framework does not
> need any additional parameters, which achieves the same inference speed to the
> backbone while improving its performance on VI-ReID task. Extensive
> experimental results illustrate that our model significantly and consistently
> outperforms existing SOTAs on three typical VI-ReID datasets.

