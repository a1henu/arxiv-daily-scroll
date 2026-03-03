---
layout: default
title: Tri-path DINO: Feature Complementary Learning for Remote Sensing Multi-Class Change Detection
---

# Tri-path DINO: Feature Complementary Learning for Remote Sensing Multi-Class Change Detection
**arXiv**：[2603.01498v1](https://arxiv.org/abs/2603.01498) · [PDF](https://arxiv.org/pdf/2603.01498.pdf)  
**作者**：Kai Zheng, Hang-Cheng Dong, Zhenkai Wu, Fupeng Wei, Wei Zhang  

**一句话要点**：提出Tri-path DINO架构，通过三路径互补特征学习解决遥感多类变化检测中的复杂场景变化问题。

**关键词**：遥感多类变化检测, 特征互补学习, DINOv3预训练, 多尺度注意力机制, 损伤评估

## 3 点简述
- 核心问题：遥感多类变化检测受复杂场景变化和标注稀缺限制，需精细监测。
- 方法要点：采用DINOv3预训练主干，结合辅助路径和多尺度注意力机制，实现粗粒度与细粒度特征互补学习。
- 实验或效果：在Gaza change和SECOND数据集上达到最优性能，GradCAM可视化验证路径互补性，支持快速准确损伤评估。

## 摘要（原文）

> In remote sensing imagery, multi class change detection (MCD) is crucial for fine grained monitoring, yet it has long been constrained by complex scene variations and the scarcity of detailed annotations. To address this, we propose the Tripath DINO architecture, which adopts a three path complementary feature learning strategy to facilitate the rapid adaptation of pre trained foundation models to complex vertical domains. Specifically, we employ the DINOv3 pre trained model as the backbone feature extraction network to learn coarse grained features. An auxiliary path also adopts a siamese structure, progressively aggregating intermediate features from the siamese encoder to enhance the learning of fine grained features. Finally, a multi scale attention mechanism is introduced to augment the decoder network, where parallel convolutions adaptively capture and enhance contextual information under different receptive fields. The proposed method achieves optimal performance on the MCD task on both the Gaza facility damage assessment dataset (Gaza change) and the classic SECOND dataset. GradCAM visualizations further confirm that the main and auxiliary paths naturally focus on coarse grained semantic changes and fine grained structural details, respectively. This synergistic complementarity provides a robust and interpretable solution for advanced change detection tasks, offering a basis for rapid and accurate damage assessment.

