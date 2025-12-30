---
layout: default
title: Automated river gauge plate reading using a hybrid object detection and generative AI framework in the Limpopo River Basin
---

# Automated river gauge plate reading using a hybrid object detection and generative AI framework in the Limpopo River Basin
**arXiv**：[2512.23454v1](https://arxiv.org/abs/2512.23454) · [PDF](https://arxiv.org/pdf/2512.23454.pdf)  
**作者**：Kayathri Vigneswaran, Hugo Retief, Jai Clifford Holmes, Mariangel Garcia Andarcia, Hansaka Tennakoon  

**一句话要点**：提出混合目标检测与生成式AI框架，用于林波波河流域的自动化水位计读数。

**关键词**：水位计读数, 目标检测, 多模态大语言模型, 水线检测, 水文监测, 自动化系统

## 3 点简述
- 核心问题：传统水文观测方法易受人工误差和环境限制，需自动化水位监测。
- 方法要点：结合视觉水线检测、YOLOv8姿态尺度提取和多模态大语言模型（GPT-4o和Gemini 2.0 Flash）。
- 实验或效果：水线检测精度达94.24%，Gemini Stage 2在最佳图像条件下平均绝对误差为5.43厘米，R平方为0.84。

## 摘要（原文）

> Accurate and continuous monitoring of river water levels is essential for flood forecasting, water resource management, and ecological protection. Traditional hydrological observation methods are often limited by manual measurement errors and environmental constraints. This study presents a hybrid framework integrating vision based waterline detection, YOLOv8 pose scale extraction, and large multimodal language models (GPT 4o and Gemini 2.0 Flash) for automated river gauge plate reading. The methodology involves sequential stages of image preprocessing, annotation, waterline detection, scale gap estimation, and numeric reading extraction. Experiments demonstrate that waterline detection achieved high precision of 94.24 percent and an F1 score of 83.64 percent, while scale gap detection provided accurate geometric calibration for subsequent reading extraction. Incorporating scale gap metadata substantially improved the predictive performance of LLMs, with Gemini Stage 2 achieving the highest accuracy, with a mean absolute error of 5.43 cm, root mean square error of 8.58 cm, and R squared of 0.84 under optimal image conditions. Results highlight the sensitivity of LLMs to image quality, with degraded images producing higher errors, and underscore the importance of combining geometric metadata with multimodal artificial intelligence for robust water level estimation. Overall, the proposed approach offers a scalable, efficient, and reliable solution for automated hydrological monitoring, demonstrating potential for real time river gauge digitization and improved water resource management.

