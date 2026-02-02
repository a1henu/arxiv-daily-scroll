---
layout: default
title: About an Automating Annotation Method for Robot Markers
---

# About an Automating Annotation Method for Robot Markers
**arXiv**：[2601.22982v1](https://arxiv.org/abs/2601.22982) · [PDF](https://arxiv.org/pdf/2601.22982.pdf)  
**作者**：Wataru Uemura, Takeru Nagashima  

**一句话要点**：提出基于ArUco标记的自动标注方法，以训练深度学习模型提升机器人标记识别性能。

**关键词**：自动标注, ArUco标记, 深度学习, 机器人视觉, YOLO模型

## 3 点简述
- 核心问题：传统图像处理方法在噪声、运动模糊等条件下识别ArUco标记易失效，且深度学习需大量手动标注数据。
- 方法要点：利用ArUco模块的检测结果自动生成标注，训练YOLO模型，无需人工干预。
- 实验或效果：自动标注方法在模糊或失焦图像中优于传统技术，减少人力并保证标注一致性。

## 摘要（原文）

> Factory automation has become increasingly important due to labor shortages, leading to the introduction of autonomous mobile robots for tasks such as material transportation. Markers are commonly used for robot self-localization and object identification. In the RoboCup Logistics League (RCLL), ArUco markers are employed both for robot localization and for identifying processing modules. Conventional recognition relies on OpenCV-based image processing, which detects black-and-white marker patterns. However, these methods often fail under noise, motion blur, defocus, or varying illumination conditions. Deep-learning-based recognition offers improved robustness under such conditions, but requires large amounts of annotated data. Annotation must typically be done manually, as the type and position of objects cannot be detected automatically, making dataset preparation a major bottleneck. In contrast, ArUco markers include built-in recognition modules that provide both ID and positional information, enabling automatic annotation. This paper proposes an automated annotation method for training deep-learning models on ArUco marker images. By leveraging marker detection results obtained from the ArUco module, the proposed approach eliminates the need for manual labeling. A YOLO-based model is trained using the automatically annotated dataset, and its performance is evaluated under various conditions. Experimental results demonstrate that the proposed method improves recognition performance compared with conventional image-processing techniques, particularly for images affected by blur or defocus. Automatic annotation also reduces human effort and ensures consistent labeling quality. Future work will investigate the relationship between confidence thresholds and recognition performance.

