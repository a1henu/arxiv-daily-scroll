---
layout: default
title: Synthetic-to-Real Domain Bridging for Single-View 3D Reconstruction of Ships for Maritime Monitoring
---

# Synthetic-to-Real Domain Bridging for Single-View 3D Reconstruction of Ships for Maritime Monitoring
**arXiv**：[2601.21786v1](https://arxiv.org/abs/2601.21786) · [PDF](https://arxiv.org/pdf/2601.21786.pdf)  
**作者**：Borja Carrillo-Perez, Felix Sattler, Angel Bueno Rodriguez, Maurice Stephan, Sarah Barnes  

**一句话要点**：提出基于合成数据训练的单视图三维重建管道，用于海事监控中的船舶三维重建。

**关键词**：单视图三维重建, 合成数据训练, 海事监控, Splatter Image网络, 域桥接

## 3 点简述
- 核心问题：海事监控中三维重建方法多依赖多视图或标注数据，难以实时部署。
- 方法要点：使用Splatter Image网络，通过合成数据训练并桥接合成与真实图像域差距。
- 实验或效果：在合成数据上评估重建保真度，真实图像上展示向实际海事场景迁移的潜力。

## 摘要（原文）

> Three-dimensional (3D) reconstruction of ships is an important part of maritime monitoring, allowing improved visualization, inspection, and decision-making in real-world monitoring environments. However, most state-ofthe-art 3D reconstruction methods require multi-view supervision, annotated 3D ground truth, or are computationally intensive, making them impractical for real-time maritime deployment. In this work, we present an efficient pipeline for single-view 3D reconstruction of real ships by training entirely on synthetic data and requiring only a single view at inference. Our approach uses the Splatter Image network, which represents objects as sparse sets of 3D Gaussians for rapid and accurate reconstruction from single images. The model is first fine-tuned on synthetic ShapeNet vessels and further refined with a diverse custom dataset of 3D ships, bridging the domain gap between synthetic and real-world imagery. We integrate a state-of-the-art segmentation module based on YOLOv8 and custom preprocessing to ensure compatibility with the reconstruction network. Postprocessing steps include real-world scaling, centering, and orientation alignment, followed by georeferenced placement on an interactive web map using AIS metadata and homography-based mapping. Quantitative evaluation on synthetic validation data demonstrates strong reconstruction fidelity, while qualitative results on real maritime images from the ShipSG dataset confirm the potential for transfer to operational maritime settings. The final system provides interactive 3D inspection of real ships without requiring real-world 3D annotations. This pipeline provides an efficient, scalable solution for maritime monitoring and highlights a path toward real-time 3D ship visualization in practical applications. Interactive demo: https://dlr-mi.github.io/ship3d-demo/.

