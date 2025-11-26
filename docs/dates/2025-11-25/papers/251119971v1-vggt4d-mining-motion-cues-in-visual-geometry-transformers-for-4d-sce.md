---
layout: default
title: VGGT4D: Mining Motion Cues in Visual Geometry Transformers for 4D Scene Reconstruction
---

# VGGT4D: Mining Motion Cues in Visual Geometry Transformers for 4D Scene Reconstruction
**arXiv**：[2511.19971v1](https://arxiv.org/abs/2511.19971) · [PDF](https://arxiv.org/pdf/2511.19971.pdf)  
**作者**：Yu Hu, Chong Cheng, Sicheng Yu, Xiaoyang Guo, Hao Wang  

**一句话要点**：提出VGGT4D框架，无需训练扩展VGGT以实现鲁棒4D场景重建

**关键词**：4D场景重建, 动态物体分割, 视觉几何变换器, 无训练框架, 姿态估计, 长视频推理

## 3 点简述
- 核心问题：动态4D场景重建中，动态物体干扰导致3D基础模型性能下降
- 方法要点：挖掘VGGT全局注意力层的动态线索，通过Gram相似性和投影梯度优化掩码
- 实验或效果：在六个数据集上，动态分割、姿态估计和重建性能优越，支持长序列单次推理

## 摘要（原文）

> Reconstructing dynamic 4D scenes is challenging, as it requires robust disentanglement of dynamic objects from the static background. While 3D foundation models like VGGT provide accurate 3D geometry, their performance drops markedly when moving objects dominate. Existing 4D approaches often rely on external priors, heavy post-optimization, or require fine-tuning on 4D datasets. In this paper, we propose VGGT4D, a training-free framework that extends the 3D foundation model VGGT for robust 4D scene reconstruction. Our approach is motivated by the key finding that VGGT's global attention layers already implicitly encode rich, layer-wise dynamic cues. To obtain masks that decouple static and dynamic elements, we mine and amplify global dynamic cues via gram similarity and aggregate them across a temporal window. To further sharpen mask boundaries, we introduce a refinement strategy driven by projection gradient. We then integrate these precise masks into VGGT's early-stage inference, effectively mitigating motion interference in both pose estimation and geometric reconstruction. Across six datasets, our method achieves superior performance in dynamic object segmentation, camera pose estimation, and dense reconstruction. It also supports single-pass inference on sequences longer than 500 frames.

