---
layout: default
title: CropTrack: A Tracking with Re-Identification Framework for Precision Agriculture
---

# CropTrack: A Tracking with Re-Identification Framework for Precision Agriculture
**arXiv**：[2512.24838v1](https://arxiv.org/abs/2512.24838) · [PDF](https://arxiv.org/pdf/2512.24838.pdf)  
**作者**：Md Ahmed Al Muzaddid, Jordan A. James, William J. Beksi  

**一句话要点**：提出CropTrack框架，结合外观与运动信息以解决农业场景中多目标跟踪的身份保持问题。

**关键词**：多目标跟踪, 农业视觉, 外观关联, 运动信息融合, 身份保持

## 3 点简述
- 农业多目标跟踪面临外观相似、频繁遮挡等挑战，传统方法依赖运动信息易丢失身份。
- CropTrack集成重排序增强的外观关联、一对多关联策略和指数移动平均原型特征库。
- 在公开数据集上评估，CropTrack在身份保持和关联准确性上优于传统方法，减少身份切换。

## 摘要（原文）

> Multiple-object tracking (MOT) in agricultural environments presents major challenges due to repetitive patterns, similar object appearances, sudden illumination changes, and frequent occlusions. Contemporary trackers in this domain rely on the motion of objects rather than appearance for association. Nevertheless, they struggle to maintain object identities when targets undergo frequent and strong occlusions. The high similarity of object appearances makes integrating appearance-based association nontrivial for agricultural scenarios. To solve this problem we propose CropTrack, a novel MOT framework based on the combination of appearance and motion information. CropTrack integrates a reranking-enhanced appearance association, a one-to-many association with appearance-based conflict resolution strategy, and an exponential moving average prototype feature bank to improve appearance-based association. Evaluated on publicly available agricultural MOT datasets, CropTrack demonstrates consistent identity preservation, outperforming traditional motion-based tracking methods. Compared to the state of the art, CropTrack achieves significant gains in identification F1 and association accuracy scores with a lower number of identity switches.

