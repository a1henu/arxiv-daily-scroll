---
layout: default
title: M-PhyGs: Multi-Material Object Dynamics from Video
---

# M-PhyGs: Multi-Material Object Dynamics from Video
**arXiv**：[2512.16885v1](https://arxiv.org/abs/2512.16885) · [PDF](https://arxiv.org/pdf/2512.16885.pdf)  
**作者**：Norika Wada, Kohei Yamashita, Ryo Kawahara, Ko Nishino  

**一句话要点**：提出M-PhyGs方法，从视频中估计多材料复杂自然物体的材料组成和物理参数。

**关键词**：多材料物体动力学, 视频物理参数估计, 连续力学参数恢复, 材料分割, 自然物体建模

## 3 点简述
- 核心问题：现有方法假设物体为单一材料或简单拓扑，难以处理真实世界多材料复杂物体。
- 方法要点：通过级联3D和2D损失及时间小批量处理，联合分割材料并恢复连续力学参数。
- 实验或效果：在Phlowers数据集上验证了M-PhyGs在材料参数估计任务中的准确性和有效性。

## 摘要（原文）

> Knowledge of the physical material properties governing the dynamics of a real-world object becomes necessary to accurately anticipate its response to unseen interactions. Existing methods for estimating such physical material parameters from visual data assume homogeneous single-material objects, pre-learned dynamics, or simplistic topologies. Real-world objects, however, are often complex in material composition and geometry lying outside the realm of these assumptions. In this paper, we particularly focus on flowers as a representative common object. We introduce Multi-material Physical Gaussians (M-PhyGs) to estimate the material composition and parameters of such multi-material complex natural objects from video. From a short video captured in a natural setting, M-PhyGs jointly segments the object into similar materials and recovers their continuum mechanical parameters while accounting for gravity. M-PhyGs achieves this efficiently with newly introduced cascaded 3D and 2D losses, and by leveraging temporal mini-batching. We introduce a dataset, Phlowers, of people interacting with flowers as a novel platform to evaluate the accuracy of this challenging task of multi-material physical parameter estimation. Experimental results on Phlowers dataset demonstrate the accuracy and effectiveness of M-PhyGs and its components.

