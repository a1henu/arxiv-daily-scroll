---
layout: default
title: Discrete Fourier Transform-based Point Cloud Compression for Efficient SLAM in Featureless Terrain
---

# Discrete Fourier Transform-based Point Cloud Compression for Efficient SLAM in Featureless Terrain
**arXiv**：[2601.04551v1](https://arxiv.org/abs/2601.04551) · [PDF](https://arxiv.org/pdf/2601.04551.pdf)  
**作者**：Riku Suzuki, Ayumi Umemura, Shreya Santra, Kentaro Uno, Kazuya Yoshida  

**一句话要点**：提出基于离散傅里叶变换的点云压缩方法，以提升特征贫瘠地形中SLAM的效率。

**关键词**：点云压缩, 离散傅里叶变换, SLAM, 数字高程模型, 特征贫瘠地形

## 3 点简述
- SLAM在机器人探索中面临点云数据量大与计算资源受限的矛盾。
- 方法将数字高程模型转换为频域图像，通过去除高频分量压缩数据。
- 实验评估了不同地形下的压缩率和精度，验证了方法在平缓地形中的有效性。

## 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) is an essential technology for the efficiency and reliability of unmanned robotic exploration missions. While the onboard computational capability and communication bandwidth are critically limited, the point cloud data handled by SLAM is large in size, attracting attention to data compression methods. To address such a problem, in this paper, we propose a new method for compressing point cloud maps by exploiting the Discrete Fourier Transform (DFT). The proposed technique converts the Digital Elevation Model (DEM) to the frequency-domain 2D image and omits its high-frequency components, focusing on the exploration of gradual terrains such as planets and deserts. Unlike terrains with detailed structures such as artificial environments, high-frequency components contribute little to the representation of gradual terrains. Thus, this method is effective in compressing data size without significant degradation of the point cloud. We evaluated the method in terms of compression rate and accuracy using camera sequences of two terrains with different elevation profiles.

