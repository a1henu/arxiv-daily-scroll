---
layout: default
title: Breaking the Sub-Millimeter Barrier: Eyeframe Acquisition from Color Images
---

# Breaking the Sub-Millimeter Barrier: Eyeframe Acquisition from Color Images
**arXiv**：[2602.16281v1](https://arxiv.org/abs/2602.16281) · [PDF](https://arxiv.org/pdf/2602.16281.pdf)  
**作者**：Manel Guzmán, Antonio Agudo  

**一句话要点**：提出基于多视图计算机视觉的算法，从彩色图像中实现亚毫米级精度的眼镜框轮廓测量，以替代传统机械追踪设备。

**关键词**：眼镜框追踪, 多视图视觉, 深度估计, 图像分割, 光学行业, 亚毫米精度

## 3 点简述
- 核心问题：传统眼镜框追踪依赖机械工具，需精确校准，流程耗时且设备复杂，影响验光师工作效率。
- 方法要点：利用InVision系统采集图像，通过分割、深度估计和多视图处理，结合RGB与深度数据实现精确轮廓测量。
- 实验或效果：在真实数据上分析不同配置，从静态彩色图像获得竞争性测量结果，无需专用追踪设备，简化工作流程。

## 摘要（原文）

> Eyeframe lens tracing is an important process in the optical industry that requires sub-millimeter precision to ensure proper lens fitting and optimal vision correction. Traditional frame tracers rely on mechanical tools that need precise positioning and calibration, which are time-consuming and require additional equipment, creating an inefficient workflow for opticians. This work presents a novel approach based on artificial vision that utilizes multi-view information. The proposed algorithm operates on images captured from an InVision system. The full pipeline includes image acquisition, frame segmentation to isolate the eyeframe from background, depth estimation to obtain 3D spatial information, and multi-view processing that integrates segmented RGB images with depth data for precise frame contour measurement. To this end, different configurations and variants are proposed and analyzed on real data, providing competitive measurements from still color images with respect to other solutions, while eliminating the need for specialized tracing equipment and reducing workflow complexity for optical technicians.

