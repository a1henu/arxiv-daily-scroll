---
layout: default
title: Synthetic-Child: An AIGC-Based Synthetic Data Pipeline for Privacy-Preserving Child Posture Estimation
---

# Synthetic-Child: An AIGC-Based Synthetic Data Pipeline for Privacy-Preserving Child Posture Estimation
**arXiv**：[2603.02598v1](https://arxiv.org/abs/2603.02598) · [PDF](https://arxiv.org/pdf/2603.02598.pdf)  
**作者**：Taowen Zeng  

**一句话要点**：提出基于AIGC的合成数据管道Synthetic-Child，以解决儿童姿态估计中隐私保护与数据稀缺问题。

**关键词**：合成数据生成, 儿童姿态估计, 隐私保护, AIGC管道, 边缘部署, 姿态分类

## 3 点简述
- 核心问题：儿童姿态估计因隐私和成本难以获取大规模标注数据，影响AI学习伴侣设备性能。
- 方法要点：通过3D模型生成多样姿态，结合ControlNet合成逼真图像，并优化模型训练与部署。
- 实验或效果：在真实儿童测试集上AP提升12.5，量化后保持高精度，实现实时边缘部署。

## 摘要（原文）

> Accurate child posture estimation is critical for AI-powered study companion devices, yet collecting large-scale annotated datasets of children is both expensive and ethically prohibitive due to privacy concerns. We present Synthetic-Child, an AIGC-based synthetic data pipeline that produces photorealistic child posture training images with ground-truth-projected keypoint annotations, requiring zero real child photographs. The pipeline comprises four stages: (1) a programmable 3D child body model (SMPL-X) in Blender generates diverse desk-study poses with IK-constrained anatomical plausibility and automatic COCO-format ground-truth export; (2) a custom PoseInjectorNode feeds 3D-derived skeletons into a dual ControlNet (pose + depth) conditioned on FLUX-1 Dev, synthesizing 12,000 photorealistic images across 10 posture categories with low annotation drift; (3) ViTPose-based confidence filtering and targeted augmentation remove generation failures and improve robustness; (4) RTMPose-M (13.6M params) is fine-tuned on the synthetic data and paired with geometric feature engineering and a lightweight MLP for posture classification, then quantized to INT8 for real-time edge deployment. On a real-child test set (n~300), the FP16 model achieves 71.2 AP -- a +12.5 AP improvement over the COCO-pretrained adult-data baseline at identical model capacity. After INT8 quantization the model retains 70.4 AP while running at 22 FPS on a 0.8-TOPS Rockchip RK3568 NPU. In a single-subject controlled comparison with a commercial posture corrector, our system achieves substantially higher recognition rates across most tested categories and responds ~1.8x faster on average. These results demonstrate that carefully designed AIGC pipelines can substantially reduce dependence on real child imagery while achieving deployment-ready accuracy, with potential applications to other privacy-sensitive domains.

