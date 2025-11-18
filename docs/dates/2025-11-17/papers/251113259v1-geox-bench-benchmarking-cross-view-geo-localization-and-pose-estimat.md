---
layout: default
title: GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models
---

# GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models
**arXiv**：[2511.13259v1](https://arxiv.org/abs/2511.13259) · [PDF](https://arxiv.org/pdf/2511.13259.pdf)  
**作者**：Yushuo Zheng, Jiangyong Ying, Huiyu Duan, Chunyi Li, Zicheng Zhang, Jing Liu, Xiaohong Liu, Guangtao Zhai  

**一句话要点**：提出GeoX-Bench基准以评估大模型在跨视角地理定位和姿态估计中的能力

**关键词**：跨视角地理定位, 姿态估计, 大模型基准, 图像问答对, 指令调优

## 3 点简述
- 核心问题：大模型在跨视角地理定位和姿态估计领域的能力尚未被探索
- 方法要点：构建包含10,859对全景-卫星图像和755,976问答对的基准数据集
- 实验或效果：评估25个模型，地理定位表现佳，姿态估计需改进，指令调优可提升能力

## 摘要（原文）

> Large multimodal models (LMMs) have demonstrated remarkable capabilities across a wide range of tasks, however their knowledge and abilities in the cross-view geo-localization and pose estimation domains remain unexplored, despite potential benefits for navigation, autonomous driving, outdoor robotics, \textit{etc}. To bridge this gap, we introduce \textbf{GeoX-Bench}, a comprehensive \underline{Bench}mark designed to explore and evaluate the capabilities of LMMs in \underline{cross}-view \underline{Geo}-localization and pose estimation. Specifically, GeoX-Bench contains 10,859 panoramic-satellite image pairs spanning 128 cities in 49 countries, along with corresponding 755,976 question-answering (QA) pairs. Among these, 42,900 QA pairs are designated for benchmarking, while the remaining are intended to enhance the capabilities of LMMs. Based on GeoX-Bench, we evaluate the capabilities of 25 state-of-the-art LMMs on cross-view geo-localization and pose estimation tasks, and further explore the empowered capabilities of instruction-tuning. Our benchmark demonstrate that while current LMMs achieve impressive performance in geo-localization tasks, their effectiveness declines significantly on the more complex pose estimation tasks, highlighting a critical area for future improvement, and instruction-tuning LMMs on the training data of GeoX-Bench can significantly improve the cross-view geo-sense abilities. The GeoX-Bench is available at \textcolor{magenta}{https://github.com/IntMeGroup/GeoX-Bench}.

