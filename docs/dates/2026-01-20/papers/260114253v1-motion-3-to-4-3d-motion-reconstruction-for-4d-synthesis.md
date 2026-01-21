---
layout: default
title: Motion 3-to-4: 3D Motion Reconstruction for 4D Synthesis
---

# Motion 3-to-4: 3D Motion Reconstruction for 4D Synthesis
**arXiv**：[2601.14253v1](https://arxiv.org/abs/2601.14253) · [PDF](https://arxiv.org/pdf/2601.14253.pdf)  
**作者**：Hongyuan Chen, Xingyu Chen, Youjia Zhang, Zexiang Xu, Anpei Chen  

**一句话要点**：提出Motion 3-to-4框架，从单目视频合成高质量4D动态对象

**关键词**：4D合成, 运动重建, 单目视频, 3D形状生成, 变换器模型

## 3 点简述
- 核心问题：4D合成因训练数据有限和单视角几何与运动恢复的模糊性而困难
- 方法要点：将4D合成分解为静态3D形状生成和运动重建，使用规范参考网格学习紧凑运动潜在表示
- 实验或效果：在标准基准和新数据集上评估，显示优于先前工作的保真度和空间一致性

## 摘要（原文）

> We present Motion 3-to-4, a feed-forward framework for synthesising high-quality 4D dynamic objects from a single monocular video and an optional 3D reference mesh. While recent advances have significantly improved 2D, video, and 3D content generation, 4D synthesis remains difficult due to limited training data and the inherent ambiguity of recovering geometry and motion from a monocular viewpoint. Motion 3-to-4 addresses these challenges by decomposing 4D synthesis into static 3D shape generation and motion reconstruction. Using a canonical reference mesh, our model learns a compact motion latent representation and predicts per-frame vertex trajectories to recover complete, temporally coherent geometry. A scalable frame-wise transformer further enables robustness to varying sequence lengths. Evaluations on both standard benchmarks and a new dataset with accurate ground-truth geometry show that Motion 3-to-4 delivers superior fidelity and spatial consistency compared to prior work. Project page is available at https://motion3-to-4.github.io/.

