---
layout: default
title: CartoMapQA: A Fundamental Benchmark Dataset Evaluating Vision-Language Models on Cartographic Map Understanding
---

# CartoMapQA: A Fundamental Benchmark Dataset Evaluating Vision-Language Models on Cartographic Map Understanding
**arXiv**：[2512.03558v1](https://arxiv.org/abs/2512.03558) · [PDF](https://arxiv.org/pdf/2512.03558.pdf)  
**作者**：Huy Quang Ung, Guillaume Habault, Yasutaka Nishimura, Hao Niu, Roberto Legaspi, Tomoki Oya, Ryoichi Kojima, Masato Taya, Chihiro Ono, Atsunori Minamikawa, Yan Liu  

**一句话要点**：提出CartoMapQA基准数据集以评估视觉语言模型在地图理解任务中的性能

**关键词**：地图理解, 视觉语言模型, 基准数据集, 地理空间推理, 符号识别, OCR错误

## 3 点简述
- 核心问题：视觉语言模型在地图理解方面能力未充分探索，存在语义理解、空间推理和OCR错误等挑战。
- 方法要点：构建包含2000多个样本的基准数据集，涵盖符号识别、信息提取、尺度解释和路径推理等多层次任务。
- 实验或效果：评估开源和专有模型，揭示模型在地图特定语义和地理空间推理方面的持续困难，为未来改进提供指导。

## 摘要（原文）

> The rise of Visual-Language Models (LVLMs) has unlocked new possibilities for seamlessly integrating visual and textual information. However, their ability to interpret cartographic maps remains largely unexplored. In this paper, we introduce CartoMapQA, a benchmark specifically designed to evaluate LVLMs' understanding of cartographic maps through question-answering tasks. The dataset includes over 2000 samples, each composed of a cartographic map, a question (with open-ended or multiple-choice answers), and a ground-truth answer. These tasks span key low-, mid- and high-level map interpretation skills, including symbol recognition, embedded information extraction, scale interpretation, and route-based reasoning. Our evaluation of both open-source and proprietary LVLMs reveals persistent challenges: models frequently struggle with map-specific semantics, exhibit limited geospatial reasoning, and are prone to Optical Character Recognition (OCR)-related errors. By isolating these weaknesses, CartoMapQA offers a valuable tool for guiding future improvements in LVLM architectures. Ultimately, it supports the development of models better equipped for real-world applications that depend on robust and reliable map understanding, such as navigation, geographic search, and urban planning. Our source code and data are openly available to the research community at: https://github.com/ungquanghuy-kddi/CartoMapQA.git

