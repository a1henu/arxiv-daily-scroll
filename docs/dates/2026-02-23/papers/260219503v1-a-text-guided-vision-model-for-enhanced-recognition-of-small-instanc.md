---
layout: default
title: A Text-Guided Vision Model for Enhanced Recognition of Small Instances
---

# A Text-Guided Vision Model for Enhanced Recognition of Small Instances
**arXiv**：[2602.19503v1](https://arxiv.org/abs/2602.19503) · [PDF](https://arxiv.org/pdf/2602.19503.pdf)  
**作者**：Hyun-Ki Jung  

**一句话要点**：提出改进YOLO-World模型以增强无人机场景下小目标检测精度与轻量化性能

**关键词**：文本引导检测, 小目标识别, 无人机视觉, 轻量化模型, YOLO改进

## 3 点简述
- 核心问题：无人机检测需从通用检测转向用户指定目标的精确识别，小目标检测精度不足。
- 方法要点：替换YOLOv8骨干网络C2f层为C3k2层以提升局部特征表示，并优化并行处理实现轻量化。
- 实验效果：在VisDrone数据集上精度、召回率、F1分数和mAP@0.5均提升，参数量和FLOPs减少。

## 摘要（原文）

> As drone-based object detection technology continues to evolve, the demand is shifting from merely detecting objects to enabling users to accurately identify specific targets. For example, users can input particular targets as prompts to precisely detect desired objects. To address this need, an efficient text-guided object detection model has been developed to enhance the detection of small objects. Specifically, an improved version of the existing YOLO-World model is introduced. The proposed method replaces the C2f layer in the YOLOv8 backbone with a C3k2 layer, enabling more precise representation of local features, particularly for small objects or those with clearly defined boundaries. Additionally, the proposed architecture improves processing speed and efficiency through parallel processing optimization, while also contributing to a more lightweight model design. Comparative experiments on the VisDrone dataset show that the proposed model outperforms the original YOLO-World model, with precision increasing from 40.6% to 41.6%, recall from 30.8% to 31%, F1 score from 35% to 35.5%, and mAP@0.5 from 30.4% to 30.7%, confirming its enhanced accuracy. Furthermore, the model demonstrates superior lightweight performance, with the parameter count reduced from 4 million to 3.8 million and FLOPs decreasing from 15.7 billion to 15.2 billion. These results indicate that the proposed approach provides a practical and effective solution for precise object detection in drone-based applications.

