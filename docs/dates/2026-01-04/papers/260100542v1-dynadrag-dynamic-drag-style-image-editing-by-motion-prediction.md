---
layout: default
title: DynaDrag: Dynamic Drag-Style Image Editing by Motion Prediction
---

# DynaDrag: Dynamic Drag-Style Image Editing by Motion Prediction
**arXiv**：[2601.00542v1](https://arxiv.org/abs/2601.00542) · [PDF](https://arxiv.org/pdf/2601.00542.pdf)  
**作者**：Jiacheng Sui, Yujie Zhou, Li Niu  

**一句话要点**：提出DynaDrag以解决拖拽式图像编辑中的跟踪与编辑性问题

**关键词**：拖拽式图像编辑, 运动预测, 像素级操作, 动态调整, 人脸编辑, 人体编辑

## 3 点简述
- 核心问题：现有拖拽式编辑方法存在跟踪失败、编辑间隙大等问题，影响编辑效果。
- 方法要点：采用预测-移动框架，迭代执行运动预测与运动监督，动态调整有效处理点。
- 实验或效果：在人脸和人体数据集上验证了优于先前方法的性能。

## 摘要（原文）

> To achieve pixel-level image manipulation, drag-style image editing which edits images using points or trajectories as conditions is attracting widespread attention. Most previous methods follow move-and-track framework, in which miss tracking and ambiguous tracking are unavoidable challenging issues. Other methods under different frameworks suffer from various problems like the huge gap between source image and target edited image as well as unreasonable intermediate point which can lead to low editability. To avoid these problems, we propose DynaDrag, the first dragging method under predict-and-move framework. In DynaDrag, Motion Prediction and Motion Supervision are performed iteratively. In each iteration, Motion Prediction first predicts where the handle points should move, and then Motion Supervision drags them accordingly. We also propose to dynamically adjust the valid handle points to further improve the performance. Experiments on face and human datasets showcase the superiority over previous works.

