---
layout: default
title: Evaluating OCR Performance for Assistive Technology: Effects of Walking Speed, Camera Placement, and Camera Type
---

# Evaluating OCR Performance for Assistive Technology: Effects of Walking Speed, Camera Placement, and Camera Type
**arXiv**：[2602.02223v1](https://arxiv.org/abs/2602.02223) · [PDF](https://arxiv.org/pdf/2602.02223.pdf)  
**作者**：Junchi Feng, Nikhil Ballem, Mahya Beheshti, Giles Hamilton-Fletcher, Todd Hudson, Maurizio Porfiri, William H. Seiple, John-Ross Rizzo  

**一句话要点**：评估OCR在辅助技术中的性能：分析行走速度、相机位置和类型的影响

**关键词**：光学字符识别, 辅助技术, 动态评估, 相机位置, 行走速度, OCR引擎

## 3 点简述
- 核心问题：现有OCR评估多基于静态数据集，未反映移动使用中的挑战，如动态条件下的性能下降。
- 方法要点：系统评估静态和动态条件，包括距离、视角、行走速度和相机位置，使用多种OCR引擎和设备。
- 实验或效果：结果显示，行走速度增加和视角变宽会降低识别准确率，Google Vision表现最佳，肩部佩戴位置平均准确率最高。

## 摘要（原文）

> Optical character recognition (OCR), which converts printed or handwritten text into machine-readable form, is widely used in assistive technology for people with blindness and low vision. Yet, most evaluations rely on static datasets that do not reflect the challenges of mobile use. In this study, we systematically evaluated OCR performance under both static and dynamic conditions. Static tests measured detection range across distances of 1-7 meters and viewing angles of 0-75 degrees horizontally. Dynamic tests examined the impact of motion by varying walking speed from slow (0.8 m/s) to very fast (1.8 m/s) and comparing three camera mounting positions: head-mounted, shoulder-mounted, and hand-held. We evaluated both a smartphone and smart glasses, using the phone's main and ultra-wide cameras. Four OCR engines were benchmarked to assess accuracy at different distances and viewing angles: Google Vision, PaddleOCR 3.0, EasyOCR, and Tesseract. PaddleOCR 3.0 was then used to evaluate accuracy at different walking speeds. Accuracy was computed at the character level using the Levenshtein ratio against manually defined ground truth. Results showed that recognition accuracy declined with increased walking speed and wider viewing angles. Google Vision achieved the highest overall accuracy, with PaddleOCR close behind as the strongest open-source alternative. Across devices, the phone's main camera achieved the highest accuracy, and a shoulder-mounted placement yielded the highest average among body positions; however, differences among shoulder, head, and hand were not statistically significant.

