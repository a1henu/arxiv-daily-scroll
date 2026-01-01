---
layout: default
title: FireRescue: A UAV-Based Dataset and Enhanced YOLO Model for Object Detection in Fire Rescue Scenes
---

# FireRescue: A UAV-Based Dataset and Enhanced YOLO Model for Object Detection in Fire Rescue Scenes
**arXiv**：[2512.24622v1](https://arxiv.org/abs/2512.24622) · [PDF](https://arxiv.org/pdf/2512.24622.pdf)  
**作者**：Qingyu Xu, Runtong Zhang, Zihuan Qiu, Fanman Meng  

**一句话要点**：提出FRS-YOLO模型和FireRescue数据集以提升火灾救援场景中的目标检测性能

**关键词**：火灾救援场景, 目标检测, 无人机数据集, YOLO改进, 注意力机制, 动态特征采样

## 3 点简述
- 核心问题：现有火灾救援检测研究缺乏对城市场景的覆盖和关键目标类别的全面性
- 方法要点：构建包含多场景和八类关键目标的FireRescue数据集，并设计FRS-YOLO模型引入注意力模块和动态特征采样器
- 实验或效果：实验表明该方法有效提升了YOLO系列模型在火灾救援场景中的检测性能

## 摘要（原文）

> Object detection in fire rescue scenarios is importance for command and decision-making in firefighting operations. However, existing research still suffers from two main limitations. First, current work predominantly focuses on environments such as mountainous or forest areas, while paying insufficient attention to urban rescue scenes, which are more frequent and structurally complex. Second, existing detection systems include a limited number of classes, such as flames and smoke, and lack a comprehensive system covering key targets crucial for command decisions, such as fire trucks and firefighters. To address the above issues, this paper first constructs a new dataset named "FireRescue" for rescue command, which covers multiple rescue scenarios, including urban, mountainous, forest, and water areas, and contains eight key categories such as fire trucks and firefighters, with a total of 15,980 images and 32,000 bounding boxes. Secondly, to tackle the problems of inter-class confusion and missed detection of small targets caused by chaotic scenes, diverse targets, and long-distance shooting, this paper proposes an improved model named FRS-YOLO. On the one hand, the model introduces a plug-and-play multidi-mensional collaborative enhancement attention module, which enhances the discriminative representation of easily confused categories (e.g., fire trucks vs. ordinary trucks) through cross-dimensional feature interaction. On the other hand, it integrates a dynamic feature sampler to strengthen high-response foreground features, thereby mitigating the effects of smoke occlusion and background interference. Experimental results demonstrate that object detection in fire rescue scenarios is highly challenging, and the proposed method effectively improves the detection performance of YOLO series models in this context.

