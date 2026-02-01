---
layout: default
title: PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing
---

# PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing
**arXiv**：[2601.21957v1](https://arxiv.org/abs/2601.21957) · [PDF](https://arxiv.org/pdf/2601.21957.pdf)  
**作者**：Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang, Changda Zhou, Hongen Liu, Manhui Lin, Yue Zhang, Yubo Zhang, Yi Liu, Dianhai Yu, Yanjun Ma  

**一句话要点**：提出PaddleOCR-VL-1.5模型，以0.9B参数实现多任务视觉语言模型，提升野外文档解析的鲁棒性。

**关键词**：文档解析, 视觉语言模型, 鲁棒性评估, 多任务学习, 超紧凑模型

## 3 点简述
- 核心问题：野外文档解析面临扫描、倾斜、扭曲等物理失真挑战，需鲁棒模型处理。
- 方法要点：升级模型至0.9B超紧凑视觉语言模型，集成印章识别和文本检测等多任务能力。
- 实验或效果：在OmniDocBench v1.5上达到94.5% SOTA准确率，并在新基准Real5-OmniDocBench上验证鲁棒性。

## 摘要（原文）

> We introduce PaddleOCR-VL-1.5, an upgraded model achieving a new state-of-the-art (SOTA) accuracy of 94.5% on OmniDocBench v1.5. To rigorously evaluate robustness against real-world physical distortions, including scanning, skew, warping, screen-photography, and illumination, we propose the Real5-OmniDocBench benchmark. Experimental results demonstrate that this enhanced model attains SOTA performance on the newly curated benchmark. Furthermore, we extend the model's capabilities by incorporating seal recognition and text spotting tasks, while remaining a 0.9B ultra-compact VLM with high efficiency. Code: https://github.com/PaddlePaddle/PaddleOCR

