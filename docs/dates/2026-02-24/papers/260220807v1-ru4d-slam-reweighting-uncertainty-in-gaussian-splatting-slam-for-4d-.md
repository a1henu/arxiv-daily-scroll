---
layout: default
title: RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction
---

# RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction
**arXiv**：[2602.20807v1](https://arxiv.org/abs/2602.20807) · [PDF](https://arxiv.org/pdf/2602.20807.pdf)  
**作者**：Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu  

**一句话要点**：提出RU4D-SLAM框架，通过重加权不确定性实现动态环境下的4D场景重建与SLAM

**关键词**：4D场景重建, 高斯溅射SLAM, 不确定性建模, 动态环境处理, 运动模糊渲染, 语义引导重加权

## 3 点简述
- 核心问题：现有3D高斯溅射SLAM在动态环境中重建与跟踪困难，4D重建潜力未充分探索。
- 方法要点：引入时间因素、不确定性感知、运动模糊渲染和语义引导重加权机制，支持自适应4D映射。
- 实验或效果：在标准基准测试中，轨迹精度和4D场景重建显著优于现有方法，尤其在动态环境和低质量输入下。

## 摘要（原文）

> Combining 3D Gaussian splatting with Simultaneous Localization and Mapping (SLAM) has gained popularity as it enables continuous 3D environment reconstruction during motion. However, existing methods struggle in dynamic environments, particularly moving objects complicate 3D reconstruction and, in turn, hinder reliable tracking. The emergence of 4D reconstruction, especially 4D Gaussian splatting, offers a promising direction for addressing these challenges, yet its potential for 4D-aware SLAM remains largely underexplored. Along this direction, we propose a robust and efficient framework, namely Reweighting Uncertainty in Gaussian Splatting SLAM (RU4D-SLAM) for 4D scene reconstruction, that introduces temporal factors into spatial 3D representation while incorporating uncertainty-aware perception of scene changes, blurred image synthesis, and dynamic scene reconstruction. We enhance dynamic scene representation by integrating motion blur rendering, and improve uncertainty-aware tracking by extending per-pixel uncertainty modeling, which is originally designed for static scenarios, to handle blurred images. Furthermore, we propose a semantic-guided reweighting mechanism for per-pixel uncertainty estimation in dynamic scenes, and introduce a learnable opacity weight to support adaptive 4D mapping. Extensive experiments on standard benchmarks demonstrate that our method substantially outperforms state-of-the-art approaches in both trajectory accuracy and 4D scene reconstruction, particularly in dynamic environments with moving objects and low-quality inputs. Code available: https://ru4d-slam.github.io

