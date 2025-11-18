---
layout: default
title: Computer Vision based group activity detection and action spotting
---

# Computer Vision based group activity detection and action spotting
**arXiv**：[2511.13315v1](https://arxiv.org/abs/2511.13315) · [PDF](https://arxiv.org/pdf/2511.13315.pdf)  
**作者**：Narthana Sivalingam, Santhirarajah Sivasthigan, Thamayanthi Mahendranathan, G. M. R. I. Godaliyadda, M. P. B. Ekanayake, H. M. V. R. Herath  

**一句话要点**：提出基于掩码特征优化与图卷积网络的群体活动检测框架，以处理多人场景中的复杂交互。

**关键词**：群体活动检测, 图卷积网络, 掩码特征优化, 多人交互建模, 视频理解

## 3 点简述
- 核心问题：多人场景中群体活动检测因遮挡、外观变化和复杂交互而具挑战性。
- 方法要点：融合Mask R-CNN定位、多骨干网络特征提取和Actor Relation Graphs建模交互。
- 实验或效果：在Collective Activity数据集上验证，提升拥挤和非拥挤场景的识别性能。

## 摘要（原文）

> Group activity detection in multi-person scenes is challenging due to complex human interactions, occlusions, and variations in appearance over time. This work presents a computer vision based framework for group activity recognition and action spotting using a combination of deep learning models and graph based relational reasoning. The system first applies Mask R-CNN to obtain accurate actor localization through bounding boxes and instance masks. Multiple backbone networks, including Inception V3, MobileNet, and VGG16, are used to extract feature maps, and RoIAlign is applied to preserve spatial alignment when generating actor specific features. The mask information is then fused with the feature maps to obtain refined masked feature representations for each actor. To model interactions between individuals, we construct Actor Relation Graphs that encode appearance similarity and positional relations using methods such as normalized cross correlation, sum of absolute differences, and dot product. Graph Convolutional Networks operate on these graphs to reason about relationships and predict both individual actions and group level activities. Experiments on the Collective Activity dataset demonstrate that the combination of mask based feature refinement, robust similarity search, and graph neural network reasoning leads to improved recognition performance across both crowded and non crowded scenarios. This approach highlights the potential of integrating segmentation, feature extraction, and relational graph reasoning for complex video understanding tasks.

