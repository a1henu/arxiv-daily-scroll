---
layout: default
title: Ridge Estimation-Based Vision and Laser Ranging Fusion Localization Method for UAVs
---

# Ridge Estimation-Based Vision and Laser Ranging Fusion Localization Method for UAVs
**arXiv**：[2512.16314v1](https://arxiv.org/abs/2512.16314) · [PDF](https://arxiv.org/pdf/2512.16314.pdf)  
**作者**：Huayu Huang, Chen Chen, Banglei Guan, Ze Tan, Yang Shang, Zhang Li, Qifeng Yu  

**一句话要点**：提出基于岭估计的视觉与激光测距融合定位方法，以提升无人机在有限观测条件下的定位精度与鲁棒性。

**关键词**：无人机定位, 传感器融合, 岭估计, 多重共线性, 激光测距, 视觉定位

## 3 点简述
- 核心问题：在长距离、小交角和大倾角等有限观测条件下，最小二乘估计的设计矩阵列向量存在严重多重共线性，导致定位不稳定和鲁棒性低。
- 方法要点：引入岭估计来缓解多重共线性，融合序列图像的丰富场景信息和激光测距的高精度，以增强定位准确性。
- 实验或效果：实验表明，该方法相比基于单一信息的地面定位算法具有更高定位精度，岭估计有效提升了鲁棒性，尤其在有限观测条件下。

## 摘要（原文）

> Tracking and measuring targets using a variety of sensors mounted on UAVs is an effective means to quickly and accurately locate the target. This paper proposes a fusion localization method based on ridge estimation, combining the advantages of rich scene information from sequential imagery with the high precision of laser ranging to enhance localization accuracy. Under limited conditions such as long distances, small intersection angles, and large inclination angles, the column vectors of the design matrix have serious multicollinearity when using the least squares estimation algorithm. The multicollinearity will lead to ill-conditioned problems, resulting in significant instability and low robustness. Ridge estimation is introduced to mitigate the serious multicollinearity under the condition of limited observation. Experimental results demonstrate that our method achieves higher localization accuracy compared to ground localization algorithms based on single information. Moreover, the introduction of ridge estimation effectively enhances the robustness, particularly under limited observation conditions.

