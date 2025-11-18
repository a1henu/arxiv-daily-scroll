---
layout: default
title: RobustGait: Robustness Analysis for Appearance Based Gait Recognition
---

# RobustGait: Robustness Analysis for Appearance Based Gait Recognition
**arXiv**：[2511.13065v1](https://arxiv.org/abs/2511.13065) · [PDF](https://arxiv.org/pdf/2511.13065.pdf)  
**作者**：Reeshoon Sayera, Akash Kumar, Sirshapan Mitra, Prudvi Kamtam, Yogesh S Rawat  

**一句话要点**：提出RobustGait框架以评估步态识别系统在真实世界扰动下的鲁棒性

**关键词**：步态识别, 鲁棒性评估, 轮廓提取, 噪声训练, 知识蒸馏, 扰动分析

## 3 点简述
- 核心问题：步态识别在受控数据集表现良好，但缺乏对真实世界扰动和轮廓变化的鲁棒性评估
- 方法要点：构建多维度评估框架，涵盖扰动类型、轮廓提取方法、模型架构和部署场景
- 实验或效果：在多个数据集上测试15种扰动，发现噪声训练和知识蒸馏可提升鲁棒性

## 摘要（原文）

> Appearance-based gait recognition have achieved strong performance on controlled datasets, yet systematic evaluation of its robustness to real-world corruptions and silhouette variability remains lacking. We present RobustGait, a framework for fine-grained robustness evaluation of appearance-based gait recognition systems. RobustGait evaluation spans four dimensions: the type of perturbation (digital, environmental, temporal, occlusion), the silhouette extraction method (segmentation and parsing networks), the architectural capacities of gait recognition models, and various deployment scenarios. The benchmark introduces 15 corruption types at 5 severity levels across CASIA-B, CCPG, and SUSTech1K, with in-the-wild validation on MEVID, and evaluates six state-of-the-art gait systems. We came across several exciting insights. First, applying noise at the RGB level better reflects real-world degradation, and reveal how distortions propagate through silhouette extraction to the downstream gait recognition systems. Second, gait accuracy is highly sensitive to silhouette extractor biases, revealing an overlooked source of benchmark bias. Third, robustness is dependent on both the type of perturbation and the architectural design. Finally, we explore robustness-enhancing strategies, showing that noise-aware training and knowledge distillation improve performance and move toward deployment-ready systems.

