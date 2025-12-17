---
layout: default
title: DriverGaze360: OmniDirectional Driver Attention with Object-Level Guidance
---

# DriverGaze360: OmniDirectional Driver Attention with Object-Level Guidance
**arXiv**：[2512.14266v1](https://arxiv.org/abs/2512.14266) · [PDF](https://arxiv.org/pdf/2512.14266.pdf)  
**作者**：Shreedhar Govil, Didier Stricker, Jason Rambach  

**一句话要点**：提出DriverGaze360全景数据集与DriverGaze360-Net方法，以解决驾驶员注意力预测中视野受限问题。

**关键词**：驾驶员注意力预测, 全景数据集, 语义分割, 自动驾驶, 全景建模

## 3 点简述
- 核心问题：现有驾驶员注意力预测受限于窄视野，无法捕捉全景环境，尤其在变道、转弯等场景。
- 方法要点：引入全景数据集DriverGaze360，并设计DriverGaze360-Net网络，联合学习注意力图和关注对象。
- 实验或效果：在多个指标上实现最优注意力预测性能，提升全景驾驶图像的空间感知能力。

## 摘要（原文）

> Predicting driver attention is a critical problem for developing explainable autonomous driving systems and understanding driver behavior in mixed human-autonomous vehicle traffic scenarios. Although significant progress has been made through large-scale driver attention datasets and deep learning architectures, existing works are constrained by narrow frontal field-of-view and limited driving diversity. Consequently, they fail to capture the full spatial context of driving environments, especially during lane changes, turns, and interactions involving peripheral objects such as pedestrians or cyclists. In this paper, we introduce DriverGaze360, a large-scale 360$^\circ$ field of view driver attention dataset, containing $\sim$1 million gaze-labeled frames collected from 19 human drivers, enabling comprehensive omnidirectional modeling of driver gaze behavior. Moreover, our panoramic attention prediction approach, DriverGaze360-Net, jointly learns attention maps and attended objects by employing an auxiliary semantic segmentation head. This improves spatial awareness and attention prediction across wide panoramic inputs. Extensive experiments demonstrate that DriverGaze360-Net achieves state-of-the-art attention prediction performance on multiple metrics on panoramic driving images. Dataset and method available at https://av.dfki.de/drivergaze360.

