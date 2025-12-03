---
layout: default
title: SurfFill: Completion of LiDAR Point Clouds via Gaussian Surfel Splatting
---

# SurfFill: Completion of LiDAR Point Clouds via Gaussian Surfel Splatting
**arXiv**：[2512.03010v1](https://arxiv.org/abs/2512.03010) · [PDF](https://arxiv.org/pdf/2512.03010.pdf)  
**作者**：Svenja Strobel, Matthias Innmann, Bernhard Egger, Marc Stamminger, Linus Franke  

**一句话要点**：提出SurfFill方法，通过高斯面元重建完成LiDAR点云，结合LiDAR与相机优势以补全缺失几何结构。

**关键词**：LiDAR点云补全, 高斯面元重建, 光束发散分析, 模糊性启发式, 多模态融合, 大规模重建

## 3 点简述
- 核心问题：LiDAR点云在薄结构和边缘处易因光束发散产生缺失，而相机能捕捉细节但精度不足。
- 方法要点：引入模糊性启发式识别缺失区域，约束高斯面元重建在模糊区域进行优化和密集化以补全点云。
- 实验或效果：在合成和真实场景的LiDAR点云补全任务中，性能优于先前重建方法，并扩展至建筑规模处理。

## 摘要（原文）

> LiDAR-captured point clouds are often considered the gold standard in active 3D reconstruction. While their accuracy is exceptional in flat regions, the capturing is susceptible to miss small geometric structures and may fail with dark, absorbent materials. Alternatively, capturing multiple photos of the scene and applying 3D photogrammetry can infer these details as they often represent feature-rich regions. However, the accuracy of LiDAR for featureless regions is rarely reached. Therefore, we suggest combining the strengths of LiDAR and camera-based capture by introducing SurfFill: a Gaussian surfel-based LiDAR completion scheme. We analyze LiDAR capturings and attribute LiDAR beam divergence as a main factor for artifacts, manifesting mostly at thin structures and edges. We use this insight to introduce an ambiguity heuristic for completed scans by evaluating the change in density in the point cloud. This allows us to identify points close to missed areas, which we can then use to grow additional points from to complete the scan. For this point growing, we constrain Gaussian surfel reconstruction [Huang et al. 2024] to focus optimization and densification on these ambiguous areas. Finally, Gaussian primitives of the reconstruction in ambiguous areas are extracted and sampled for points to complete the point cloud. To address the challenges of large-scale reconstruction, we extend this pipeline with a divide-and-conquer scheme for building-sized point cloud completion. We evaluate on the task of LiDAR point cloud completion of synthetic and real-world scenes and find that our method outperforms previous reconstruction methods.

