---
layout: default
title: Fourier Angle Alignment for Oriented Object Detection in Remote Sensing
---

# Fourier Angle Alignment for Oriented Object Detection in Remote Sensing
**arXiv**：[2602.23790v1](https://arxiv.org/abs/2602.23790) · [PDF](https://arxiv.org/pdf/2602.23790.pdf)  
**作者**：Changyu Gu, Linwei Chen, Lin Gu, Ying Fu  

**一句话要点**：提出傅里叶角度对齐方法，解决遥感旋转目标检测中的方向不一致和任务冲突问题。

**关键词**：遥感目标检测, 旋转目标检测, 傅里叶变换, 方向对齐, 特征融合, 检测头设计

## 3 点简述
- 核心问题：遥感旋转目标检测存在检测器颈部方向不一致和检测头任务冲突的瓶颈。
- 方法要点：利用傅里叶旋转等变性，通过频谱分析角度信息并对齐主方向，引入FAAFusion和FAA Head模块。
- 实验效果：在DOTA-v1.0和DOTA-v1.5数据集上达到新SOTA，验证了方法的有效性。

## 摘要（原文）

> In remote sensing rotated object detection, mainstream methods suffer from two bottlenecks, directional incoherence at detector neck and task conflict at detecting head. Ulitising fourier rotation equivariance, we introduce Fourier Angle Alignment, which analyses angle information through frequency spectrum and aligns the main direction to a certain orientation. Then we propose two plug and play modules : FAAFusion and FAA Head. FAAFusion works at the detector neck, aligning the main direction of higher-level features to the lower-level features and then fusing them. FAA Head serves as a new detection head, which pre-aligns RoI features to a canonical angle and adds them to the original features before classification and regression. Experiments on DOTA-v1.0, DOTA-v1.5 and HRSC2016 show that our method can greatly improve previous work. Particularly, our method achieves new state-of-the-art results of 78.72% mAP on DOTA-v1.0 and 72.28% mAP on DOTA-v1.5 datasets with single scale training and testing, validating the efficacy of our approach in remote sensing object detection. The code is made publicly available at https://github.com/gcy0423/Fourier-Angle-Alignment .

