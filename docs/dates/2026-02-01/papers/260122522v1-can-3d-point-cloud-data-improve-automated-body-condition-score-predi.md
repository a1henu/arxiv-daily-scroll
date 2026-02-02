---
layout: default
title: Can 3D point cloud data improve automated body condition score prediction in dairy cattle?
---

# Can 3D point cloud data improve automated body condition score prediction in dairy cattle?
**arXiv**：[2601.22522v1](https://arxiv.org/abs/2601.22522) · [PDF](https://arxiv.org/pdf/2601.22522.pdf)  
**作者**：Zhou Tang, Jin Wang, Angelo De Castro, Yuxi Zhang, Victoria Bastos Primo, Ana Beatriz Montevecchio Bernardino, Gota Morota, Xu Wang, Ricardo C Chebel, Haipeng Yu  

**一句话要点**：比较深度图像与点云数据在奶牛体况评分预测中的性能，发现点云未提供一致优势。

**关键词**：体况评分预测, 深度图像, 点云数据, 奶牛养殖, 计算机视觉, 模型比较

## 3 点简述
- 核心问题：奶牛体况评分传统方法主观且耗时，需自动化预测。
- 方法要点：在四种设置下比较深度图像与点云数据，使用交叉验证评估模型。
- 实验或效果：深度图像在多数设置下优于点云，点云对噪声和模型架构更敏感。

## 摘要（原文）

> Body condition score (BCS) is a widely used indicator of body energy status and is closely associated with metabolic status, reproductive performance, and health in dairy cattle; however, conventional visual scoring is subjective and labor-intensive. Computer vision approaches have been applied to BCS prediction, with depth images widely used because they capture geometric information independent of coat color and texture. More recently, three-dimensional point cloud data have attracted increasing interest due to their ability to represent richer geometric characteristics of animal morphology, but direct head-to-head comparisons with depth image-based approaches remain limited. In this study, we compared top-view depth image and point cloud data for BCS prediction under four settings: 1) unsegmented raw data, 2) segmented full-body data, 3) segmented hindquarter data, and 4) handcrafted feature data. Prediction models were evaluated using data from 1,020 dairy cows collected on a commercial farm, with cow-level cross-validation to prevent data leakage. Depth image-based models consistently achieved higher accuracy than point cloud-based models when unsegmented raw data and segmented full-body data were used, whereas comparable performance was observed when segmented hindquarter data were used. Both depth image and point cloud approaches showed reduced accuracy when handcrafted feature data were employed compared with the other settings. Overall, point cloud-based predictions were more sensitive to noise and model architecture than depth image-based predictions. Taken together, these results indicate that three-dimensional point clouds do not provide a consistent advantage over depth images for BCS prediction in dairy cattle under the evaluated conditions.

