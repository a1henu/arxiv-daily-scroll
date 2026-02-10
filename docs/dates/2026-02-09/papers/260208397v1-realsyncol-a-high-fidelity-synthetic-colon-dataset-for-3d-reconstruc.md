---
layout: default
title: RealSynCol: a high-fidelity synthetic colon dataset for 3D reconstruction applications
---

# RealSynCol: a high-fidelity synthetic colon dataset for 3D reconstruction applications
**arXiv**：[2602.08397v1](https://arxiv.org/abs/2602.08397) · [PDF](https://arxiv.org/pdf/2602.08397.pdf)  
**作者**：Chiara Lena, Davide Milesi, Alessandro Casella, Luca Carlini, Joseph C. Norton, James Martin, Bruno Scaglioni, Keith L. Obstein, Roberto De Sire, Marco Spadaccini, Cesare Hassan, Pietro Valdastri, Elena De Momi  

**一句话要点**：提出RealSynCol高保真合成结肠数据集以支持结肠镜3D重建的深度学习算法开发

**关键词**：合成数据集, 结肠镜3D重建, 深度学习, 深度估计, 姿态估计, 医学影像

## 3 点简述
- 核心问题：结肠镜3D重建缺乏大规模真实数据，限制深度学习方法的稳健性。
- 方法要点：基于10个CT扫描构建虚拟环境，生成28,130帧合成图像，附带深度图、光流、3D网格和相机轨迹。
- 实验或效果：基准测试显示RealSynCol的高真实性和多样性显著提升在临床图像上的泛化性能。

## 摘要（原文）

> Deep learning has the potential to improve colonoscopy by enabling 3D reconstruction of the colon, providing a comprehensive view of mucosal surfaces and lesions, and facilitating the identification of unexplored areas. However, the development of robust methods is limited by the scarcity of large-scale ground truth data. We propose RealSynCol, a highly realistic synthetic dataset designed to replicate the endoscopic environment. Colon geometries extracted from 10 CT scans were imported into a virtual environment that closely mimics intraoperative conditions and rendered with realistic vascular textures. The resulting dataset comprises 28\,130 frames, paired with ground truth depth maps, optical flow, 3D meshes, and camera trajectories. A benchmark study was conducted to evaluate the available synthetic colon datasets for the tasks of depth and pose estimation. Results demonstrate that the high realism and variability of RealSynCol significantly enhance generalization performance on clinical images, proving it to be a powerful tool for developing deep learning algorithms to support endoscopic diagnosis.

