---
layout: default
title: A Comparative Evaluation of Large Vision-Language Models for 2D Object Detection under SOTIF Conditions
---

# A Comparative Evaluation of Large Vision-Language Models for 2D Object Detection under SOTIF Conditions
**arXiv**：[2601.22830v1](https://arxiv.org/abs/2601.22830) · [PDF](https://arxiv.org/pdf/2601.22830.pdf)  
**作者**：Ji Zhou, Yilin Ding, Yongqi Zhao, Jiachen Xu, Arno Eichberger  

**一句话要点**：评估大型视觉语言模型在SOTIF条件下用于2D目标检测的性能，揭示语义推理与几何回归的互补优势。

**关键词**：大型视觉语言模型, 2D目标检测, SOTIF条件, 自动驾驶安全, 语义推理, 几何回归

## 3 点简述
- 核心问题：自动驾驶中感知不足导致的安全风险，尤其在恶劣条件下传统检测器表现不佳。
- 方法要点：系统评估十种代表性LVLMs，使用PeSOTIF数据集，对比YOLO基准检测器。
- 实验或效果：LVLMs在复杂自然场景中召回率提升超25%，但基准在合成扰动下几何精度更优。

## 摘要（原文）

> Reliable environmental perception remains one of the main obstacles for safe operation of automated vehicles. Safety of the Intended Functionality (SOTIF) concerns safety risks from perception insufficiencies, particularly under adverse conditions where conventional detectors often falter. While Large Vision-Language Models (LVLMs) demonstrate promising semantic reasoning, their quantitative effectiveness for safety-critical 2D object detection is underexplored. This paper presents a systematic evaluation of ten representative LVLMs using the PeSOTIF dataset, a benchmark specifically curated for long-tail traffic scenarios and environmental degradations. Performance is quantitatively compared against the classical perception approach, a YOLO-based detector. Experimental results reveal a critical trade-off: top-performing LVLMs (e.g., Gemini 3, Doubao) surpass the YOLO baseline in recall by over 25% in complex natural scenarios, exhibiting superior robustness to visual degradation. Conversely, the baseline retains an advantage in geometric precision for synthetic perturbations. These findings highlight the complementary strengths of semantic reasoning versus geometric regression, supporting the use of LVLMs as high-level safety validators in SOTIF-oriented automated driving systems.

