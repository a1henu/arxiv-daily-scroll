---
layout: default
title: NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects
---

# NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects
**arXiv**：[2602.05822v1](https://arxiv.org/abs/2602.05822) · [PDF](https://arxiv.org/pdf/2602.05822.pdf)  
**作者**：Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano  

**一句话要点**：提出NVS-HO基准，用于评估真实环境中手持物体的RGB输入新视角合成性能。

**关键词**：新视角合成, 手持物体, RGB输入, 基准测试, NeRF, 高斯溅射

## 3 点简述
- 核心问题：现有方法在无约束手持条件下新视角合成性能不足，缺乏专门基准。
- 方法要点：通过手持和固定板序列提供训练与评估数据，结合NeRF和高斯溅射建立基线模型。
- 实验或效果：实验显示当前方法在手持条件下存在显著性能差距，突显鲁棒性需求。

## 摘要（原文）

> We propose NVS-HO, the first benchmark designed for novel view synthesis of handheld objects in real-world environments using only RGB inputs. Each object is recorded in two complementary RGB sequences: (1) a handheld sequence, where the object is manipulated in front of a static camera, and (2) a board sequence, where the object is fixed on a ChArUco board to provide accurate camera poses via marker detection. The goal of NVS-HO is to learn a NVS model that captures the full appearance of an object from (1), whereas (2) provides the ground-truth images used for evaluation. To establish baselines, we consider both a classical SfM pipeline and a state-of-the-art pre-trained feed-forward neural network (VGGT) as pose estimators, and train NVS models based on NeRF and Gaussian Splatting. Our experiments reveal significant performance gaps in current methods under unconstrained handheld conditions, highlighting the need for more robust approaches. NVS-HO thus offers a challenging real-world benchmark to drive progress in RGB-based novel view synthesis of handheld objects.

