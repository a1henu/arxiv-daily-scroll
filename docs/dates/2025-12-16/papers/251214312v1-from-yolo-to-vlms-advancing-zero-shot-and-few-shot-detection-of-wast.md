---
layout: default
title: From YOLO to VLMs: Advancing Zero-Shot and Few-Shot Detection of Wastewater Treatment Plants Using Satellite Imagery in MENA Region
---

# From YOLO to VLMs: Advancing Zero-Shot and Few-Shot Detection of Wastewater Treatment Plants Using Satellite Imagery in MENA Region
**arXiv**：[2512.14312v1](https://arxiv.org/abs/2512.14312) · [PDF](https://arxiv.org/pdf/2512.14312.pdf)  
**作者**：Akila Premarathna, Kanishka Hewageegana, Garcia Andarcia Mariangel  

**一句话要点**：提出基于视觉语言模型的零样本与少样本方法，以替代YOLOv8实现中东和北非地区废水处理厂的卫星图像高效检测。

**关键词**：视觉语言模型, 零样本检测, 卫星图像分析, 废水处理厂识别, 中东和北非地区

## 3 点简述
- 核心问题：中东和北非地区废水处理厂检测依赖传统YOLOv8分割，需大量人工标注，效率低。
- 方法要点：比较多种视觉语言模型（如Gemma-3）的零样本和少样本能力，通过专家提示识别废水处理厂组件并输出JSON。
- 实验或效果：在包含1207个验证点的数据集上，零样本评估显示多个视觉语言模型真阳性率优于YOLOv8，Gemma-3表现最佳。

## 摘要（原文）

> In regions of the Middle East and North Africa (MENA), there is a high demand for wastewater treatment plants (WWTPs), crucial for sustainable water management. Precise identification of WWTPs from satellite images enables environmental monitoring. Traditional methods like YOLOv8 segmentation require extensive manual labeling. But studies indicate that vision-language models (VLMs) are an efficient alternative to achieving equivalent or superior results through inherent reasoning and annotation. This study presents a structured methodology for VLM comparison, divided into zero-shot and few-shot streams specifically to identify WWTPs. The YOLOv8 was trained on a governmental dataset of 83,566 high-resolution satellite images from Egypt, Saudi Arabia, and UAE: ~85% WWTPs (positives), 15% non-WWTPs (negatives). Evaluated VLMs include LLaMA 3.2 Vision, Qwen 2.5 VL, DeepSeek-VL2, Gemma 3, Gemini, and Pixtral 12B (Mistral), used to identify WWTP components such as circular/rectangular tanks, aeration basins and distinguish confounders via expert prompts producing JSON outputs with confidence and descriptions. The dataset comprises 1,207 validated WWTP locations (198 UAE, 354 KSA, 655 Egypt) and equal non-WWTP sites from field/AI data, as 600mx600m Geo-TIFF images (Zoom 18, EPSG:4326). Zero-shot evaluations on WWTP images showed several VLMs out-performing YOLOv8's true positive rate, with Gemma-3 highest. Results confirm that VLMs, particularly with zero-shot, can replace YOLOv8 for efficient, annotation-free WWTP classification, enabling scalable remote sensing.

