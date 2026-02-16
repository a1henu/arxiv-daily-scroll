---
layout: default
title: Represent Micro-Doppler Signature in Orders
---

# Represent Micro-Doppler Signature in Orders
**arXiv**：[2602.12985v1](https://arxiv.org/abs/2602.12985) · [PDF](https://arxiv.org/pdf/2602.12985.pdf)  
**作者**：Weicheng Gao  

**一句话要点**：提出基于切比雪夫多项式分解的微多普勒特征表示方法，以提升穿墙雷达下室内人体活动识别的效率与准确性。

**关键词**：微多普勒特征表示, 穿墙雷达, 切比雪夫多项式分解, 人体活动识别, 时频分析, 特征压缩

## 3 点简述
- 问题：穿墙雷达下相似室内活动（如持枪与正常行走）的微多普勒特征区分度低，且传统时频谱图输入规模大，影响模型训练与推理效率。
- 方法：建立人体运动参数化模型与雷达回波模型，通过正交切比雪夫多项式分解提取躯干和肢体的运动包络，将时频谱映射到鲁棒的切比雪夫-时间系数空间。
- 效果：数值模拟与实验验证该方法能有效表征持枪与非持枪活动，压缩时频谱规模，在识别精度与输入数据维度间取得平衡。

## 摘要（原文）

> Non-line-of-sight sensing of human activities in complex environments is enabled by multiple-input multiple-output through-the-wall radar (TWR). However, the distinctiveness of micro-Doppler signature between similar indoor human activities such as gun carrying and normal walking is minimal, while the large scale of input images required for effective identification utilizing time-frequency spectrograms creates challenges for model training and inference efficiency. To address this issue, the Chebyshev-time map is proposed in this paper, which is a method characterizing micro-Doppler signature using polynomial orders. The parametric kinematic models for human motion and the TWR echo model are first established. Then, a time-frequency feature representation method based on orthogonal Chebyshev polynomial decomposition is proposed. The kinematic envelopes of the torso and limbs are extracted, and the time-frequency spectrum slices are mapped into a robust Chebyshev-time coefficient space, preserving the multi-order morphological detail information of time-frequency spectrum. Numerical simulations and experiments are conducted to verify the effectiveness of the proposed method, which demonstrates the capability to characterize armed and unarmed indoor human activities while effectively compressing the scale of the time-frequency spectrum to achieve a balance between recognition accuracy and input data dimensions. The open-source code of this paper can be found in: https://github.com/JoeyBGOfficial/Represent-Micro-Doppler-Signature-in-Orders.

