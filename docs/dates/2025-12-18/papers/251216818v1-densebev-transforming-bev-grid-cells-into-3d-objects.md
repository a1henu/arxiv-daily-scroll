---
layout: default
title: DenseBEV: Transforming BEV Grid Cells into 3D Objects
---

# DenseBEV: Transforming BEV Grid Cells into 3D Objects
**arXiv**：[2512.16818v1](https://arxiv.org/abs/2512.16818) · [PDF](https://arxiv.org/pdf/2512.16818.pdf)  
**作者**：Marius Dähling, Sebastian Krebs, J. Marius Zöllner  

**一句话要点**：提出DenseBEV方法，通过将BEV网格单元直接用作锚点，优化多摄像头3D物体检测。

**关键词**：BEV检测, 3D物体检测, 多摄像头感知, 锚点生成, 端到端训练, 时序建模

## 3 点简述
- 核心问题：传统BEV检测模型依赖随机或辅助网络锚点，效率低且不直观。
- 方法要点：使用BEV特征单元作为锚点，结合两阶段锚点生成和BEV-NMS，实现端到端训练。
- 实验效果：在nuScenes和Waymo数据集上显著提升NDS和mAP，尤其改善小物体检测性能。

## 摘要（原文）

> In current research, Bird's-Eye-View (BEV)-based transformers are increasingly utilized for multi-camera 3D object detection. Traditional models often employ random queries as anchors, optimizing them successively. Recent advancements complement or replace these random queries with detections from auxiliary networks. We propose a more intuitive and efficient approach by using BEV feature cells directly as anchors. This end-to-end approach leverages the dense grid of BEV queries, considering each cell as a potential object for the final detection task. As a result, we introduce a novel two-stage anchor generation method specifically designed for multi-camera 3D object detection. To address the scaling issues of attention with a large number of queries, we apply BEV-based Non-Maximum Suppression, allowing gradients to flow only through non-suppressed objects. This ensures efficient training without the need for post-processing. By using BEV features from encoders such as BEVFormer directly as object queries, temporal BEV information is inherently embedded. Building on the temporal BEV information already embedded in our object queries, we introduce a hybrid temporal modeling approach by integrating prior detections to further enhance detection performance. Evaluating our method on the nuScenes dataset shows consistent and significant improvements in NDS and mAP over the baseline, even with sparser BEV grids and therefore fewer initial anchors. It is particularly effective for small objects, enhancing pedestrian detection with a 3.8% mAP increase on nuScenes and an 8% increase in LET-mAP on Waymo. Applying our method, named DenseBEV, to the challenging Waymo Open dataset yields state-of-the-art performance, achieving a LET-mAP of 60.7%, surpassing the previous best by 5.4%. Code is available at https://github.com/mdaehl/DenseBEV.

