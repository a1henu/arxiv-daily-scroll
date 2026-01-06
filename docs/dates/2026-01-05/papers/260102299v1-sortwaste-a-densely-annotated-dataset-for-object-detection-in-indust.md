---
layout: default
title: SortWaste: A Densely Annotated Dataset for Object Detection in Industrial Waste Sorting
---

# SortWaste: A Densely Annotated Dataset for Object Detection in Industrial Waste Sorting
**arXiv**：[2601.02299v1](https://arxiv.org/abs/2601.02299) · [PDF](https://arxiv.org/pdf/2601.02299.pdf)  
**作者**：Sara Inácio, Hugo Proença, João C. Neves  

**一句话要点**：提出SortWaste数据集与ClutterScore指标，以解决工业废料分拣中目标检测的挑战。

**关键词**：目标检测, 废料分拣, 数据集, 场景复杂度, 工业视觉, 基准测试

## 3 点简述
- 核心问题：缺乏真实世界废料分拣数据集，自动化系统处理高变异性、杂乱和视觉复杂性时表现不佳。
- 方法要点：引入密集标注的SortWaste数据集，并提出ClutterScore指标客观评估场景硬度。
- 实验或效果：基准测试显示模型在塑料检测任务中mAP达59.7%，但在高度杂乱场景中性能显著下降。

## 摘要（原文）

> The increasing production of waste, driven by population growth, has created challenges in managing and recycling materials effectively. Manual waste sorting is a common practice; however, it remains inefficient for handling large-scale waste streams and presents health risks for workers. On the other hand, existing automated sorting approaches still struggle with the high variability, clutter, and visual complexity of real-world waste streams. The lack of real-world datasets for waste sorting is a major reason automated systems for this problem are underdeveloped. Accordingly, we introduce SortWaste, a densely annotated object detection dataset collected from a Material Recovery Facility. Additionally, we contribute to standardizing waste detection in sorting lines by proposing ClutterScore, an objective metric that gauges the scene's hardness level using a set of proxies that affect visual complexity (e.g., object count, class and size entropy, and spatial overlap). In addition to these contributions, we provide an extensive benchmark of state-of-the-art object detection models, detailing their results with respect to the hardness level assessed by the proposed metric. Despite achieving promising results (mAP of 59.7% in the plastic-only detection task), performance significantly decreases in highly cluttered scenes. This highlights the need for novel and more challenging datasets on the topic.

