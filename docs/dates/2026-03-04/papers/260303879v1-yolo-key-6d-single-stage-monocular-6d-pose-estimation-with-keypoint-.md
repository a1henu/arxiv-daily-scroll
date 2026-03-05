---
layout: default
title: Yolo-Key-6D: Single Stage Monocular 6D Pose Estimation with Keypoint Enhancements
---

# Yolo-Key-6D: Single Stage Monocular 6D Pose Estimation with Keypoint Enhancements
**arXiv**：[2603.03879v1](https://arxiv.org/abs/2603.03879) · [PDF](https://arxiv.org/pdf/2603.03879.pdf)  
**作者**：Kemal Alperen Çetiner, Hazım Kemal Ekenel  

**一句话要点**：提出Yolo-Key-6D单阶段框架，通过关键点增强实现快速准确的单目6D姿态估计。

**关键词**：单目6D姿态估计, 单阶段框架, 关键点检测, 实时性能, YOLO架构, 端到端训练

## 3 点简述
- 核心问题：多阶段方法延迟高，难以满足实时应用需求。
- 方法要点：基于YOLO架构，集成辅助头回归3D边界框角点的2D投影，并使用9D表示直接回归旋转。
- 实验或效果：在LINEMOD和LINEMOD-Occluded基准上分别达到96.24%和69.41%的准确率，并实现实时运行。

## 摘要（原文）

> Estimating the 6D pose of objects from a single RGB image is a critical task for robotics and extended reality applications. However, state-of-the-art multi stage methods often suffer from high latency, making them unsuitable for real time use. In this paper, we present Yolo-Key-6D, a novel single stage, end-to-end framework for monocular 6D pose estimation designed for both speed and accuracy. Our approach enhances a YOLO based architecture by integrating an auxiliary head that regresses the 2D projections of an object's 3D bounding box corners. This keypoint detection task significantly improves the network's understanding of 3D geometry. For stable end-to-end training, we directly regress rotation using a continuous 9D representation projected to SO(3) via singular value decomposition. On the LINEMOD and LINEMOD-Occluded benchmarks, YOLO-Key-6D achieves competitive accuracy scores of 96.24% and 69.41%, respectively, with the ADD(-S) 0.1d metric, while proving itself to operate in real time. Our results demonstrate that a carefully designed single stage method can provide a practical and effective balance of performance and efficiency for real world deployment.

