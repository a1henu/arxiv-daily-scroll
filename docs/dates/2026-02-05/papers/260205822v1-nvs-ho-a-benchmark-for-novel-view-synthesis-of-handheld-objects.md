---
layout: default
title: NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects
---

# NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects
**arXiv**：[2602.05822v1](https://arxiv.org/abs/2602.05822) · [PDF](https://arxiv.org/pdf/2602.05822.pdf)  
**作者**：Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano  

**一句话要点**：提出NVS-HO基准，用于真实环境中仅RGB输入的手持物体新视角合成。

**关键词**：新视角合成, 手持物体, RGB基准, NeRF, 高斯溅射, 相机位姿估计

## 3 点简述
- 核心问题：现有方法在无约束手持条件下性能不足，需更鲁棒的新视角合成技术。
- 方法要点：结合手持序列学习物体外观，使用板序列提供精确相机位姿用于评估。
- 实验或效果：基于NeRF和高斯溅射训练模型，揭示当前方法在手持场景中的显著性能差距。

## 摘要（原文）

> We propose NVS-HO, the first benchmark designed for novel view synthesis of handheld objects in real-world environments using only RGB inputs. Each object is recorded in two complementary RGB sequences: (1) a handheld sequence, where the object is manipulated in front of a static camera, and (2) a board sequence, where the object is fixed on a ChArUco board to provide accurate camera poses via marker detection. The goal of NVS-HO is to learn a NVS model that captures the full appearance of an object from (1), whereas (2) provides the ground-truth images used for evaluation. To establish baselines, we consider both a classical SfM pipeline and a state-of-the-art pre-trained feed-forward neural network (VGGT) as pose estimators, and train NVS models based on NeRF and Gaussian Splatting. Our experiments reveal significant performance gaps in current methods under unconstrained handheld conditions, highlighting the need for more robust approaches. NVS-HO thus offers a challenging real-world benchmark to drive progress in RGB-based novel view synthesis of handheld objects.

