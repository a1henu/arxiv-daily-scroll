---
layout: default
title: Conformal Prediction Sets for Instance Segmentation
---

# Conformal Prediction Sets for Instance Segmentation
**arXiv**：[2602.10045v1](https://arxiv.org/abs/2602.10045) · [PDF](https://arxiv.org/pdf/2602.10045.pdf)  
**作者**：Kerri Lu, Dan M. Kluger, Stephen Bates, Sherrie Wang  

**一句话要点**：提出基于共形预测的实例分割置信集算法，以解决不确定性量化问题。

**关键词**：实例分割, 共形预测, 不确定性量化, 置信集, IoU保证, 自适应预测

## 3 点简述
- 当前实例分割模型缺乏校准和不确定性保证，输出不可靠。
- 算法为像素查询生成自适应置信集，提供IoU高覆盖概率的理论保证。
- 在农业、细胞和车辆检测实验中，算法覆盖目标且优于基线方法。

## 摘要（原文）

> Current instance segmentation models achieve high performance on average predictions, but lack principled uncertainty quantification: their outputs are not calibrated, and there is no guarantee that a predicted mask is close to the ground truth. To address this limitation, we introduce a conformal prediction algorithm to generate adaptive confidence sets for instance segmentation. Given an image and a pixel coordinate query, our algorithm generates a confidence set of instance predictions for that pixel, with a provable guarantee for the probability that at least one of the predictions has high Intersection-Over-Union (IoU) with the true object instance mask. We apply our algorithm to instance segmentation examples in agricultural field delineation, cell segmentation, and vehicle detection. Empirically, we find that our prediction sets vary in size based on query difficulty and attain the target coverage, outperforming existing baselines such as Learn Then Test, Conformal Risk Control, and morphological dilation-based methods. We provide versions of the algorithm with asymptotic and finite sample guarantees.

