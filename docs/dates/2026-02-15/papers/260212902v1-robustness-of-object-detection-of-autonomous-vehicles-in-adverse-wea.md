---
layout: default
title: Robustness of Object Detection of Autonomous Vehicles in Adverse Weather Conditions
---

# Robustness of Object Detection of Autonomous Vehicles in Adverse Weather Conditions
**arXiv**：[2602.12902v1](https://arxiv.org/abs/2602.12902) · [PDF](https://arxiv.org/pdf/2602.12902.pdf)  
**作者**：Fox Pettersen, Hong Zhu  

**一句话要点**：提出基于数据增强的评估方法，以测试自动驾驶车辆在恶劣天气下的目标检测鲁棒性。

**关键词**：自动驾驶, 目标检测, 鲁棒性评估, 数据增强, 恶劣天气, 合成数据

## 3 点简述
- 核心问题：自动驾驶目标检测模型在恶劣天气条件下的安全操作阈值评估。
- 方法要点：使用数据增强生成模拟恶劣条件的合成数据，通过平均首次失败系数衡量鲁棒性。
- 实验或效果：在四种模型和七种条件下测试，Faster R-CNN鲁棒性最高，训练可提升鲁棒性但需防过拟合。

## 摘要（原文）

> As self-driving technology advances toward widespread adoption, determining safe operational thresholds across varying environmental conditions becomes critical for public safety. This paper proposes a method for evaluating the robustness of object detection ML models in autonomous vehicles under adverse weather conditions. It employs data augmentation operators to generate synthetic data that simulates different severance degrees of the adverse operation conditions at progressive intensity levels to find the lowest intensity of the adverse conditions at which the object detection model fails. The robustness of the object detection model is measured by the average first failure coefficients (AFFC) over the input images in the benchmark. The paper reports an experiment with four object detection models: YOLOv5s, YOLOv11s, Faster R-CNN, and Detectron2, utilising seven data augmentation operators that simulate weather conditions fog, rain, and snow, and lighting conditions of dark, bright, flaring, and shadow. The experiment data show that the method is feasible, effective, and efficient to evaluate and compare the robustness of object detection models in various adverse operation conditions. In particular, the Faster R-CNN model achieved the highest robustness with an overall average AFFC of 71.9% over all seven adverse conditions, while YOLO variants showed the AFFC values of 43%. The method is also applied to assess the impact of model training that targets adverse operation conditions using synthetic data on model robustness. It is observed that such training can improve robustness in adverse conditions but may suffer from diminishing returns and forgetting phenomena (i.e., decline in robustness) if overtrained.

