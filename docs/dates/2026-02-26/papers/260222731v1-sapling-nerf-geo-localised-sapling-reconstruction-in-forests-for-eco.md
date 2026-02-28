---
layout: default
title: Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring
---

# Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring
**arXiv**：[2602.22731v1](https://arxiv.org/abs/2602.22731) · [PDF](https://arxiv.org/pdf/2602.22731.pdf)  
**作者**：Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Sruthi M. Krishna Moorthy, Yifu Tao, Fernando Torres, Roberto Salguero-Gómez, Maurice Fallon  

**一句话要点**：提出融合NeRF、LiDAR SLAM与GNSS的管道，实现森林幼苗可重复、地理定位的生态监测。

**关键词**：神经辐射场, 激光雷达SLAM, 地理定位, 生态监测, 三维重建, 森林幼苗

## 3 点简述
- 核心问题：现有3D传感方法难以捕捉幼苗细尺度结构，且缺乏地理定位能力，阻碍长期定量评估。
- 方法要点：采用三级表示，结合GNSS粗定位、LiDAR SLAM厘米级定位与NeRF对象中心重建，提升重建精度与可重复性。
- 实验或效果：在森林样地验证，相比TLS，能更准确测量幼苗高度、分枝模式和叶木比，支持生态分析。

## 摘要（原文）

> Saplings are key indicators of forest regeneration and overall forest health. However, their fine-scale architectural traits are difficult to capture with existing 3D sensing methods, which make quantitative evaluation difficult. Terrestrial Laser Scanners (TLS), Mobile Laser Scanners (MLS), or traditional photogrammetry approaches poorly reconstruct thin branches, dense foliage, and lack the scale consistency needed for long-term monitoring. Implicit 3D reconstruction methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) are promising alternatives, but cannot recover the true scale of a scene and lack any means to be accurately geo-localised. In this paper, we present a pipeline which fuses NeRF, LiDAR SLAM, and GNSS to enable repeatable, geo-localised ecological monitoring of saplings. Our system proposes a three-level representation: (i) coarse Earth-frame localisation using GNSS, (ii) LiDAR-based SLAM for centimetre-accurate localisation and reconstruction, and (iii) NeRF-derived object-centric dense reconstruction of individual saplings. This approach enables repeatable quantitative evaluation and long-term monitoring of sapling traits. Our experiments in forest plots in Wytham Woods (Oxford, UK) and Evo (Finland) show that stem height, branching patterns, and leaf-to-wood ratios can be captured with increased accuracy as compared to TLS. We demonstrate that accurate stem skeletons and leaf distributions can be measured for saplings with heights between 0.5m and 2m in situ, giving ecologists access to richer structural and quantitative data for analysing forest dynamics.

