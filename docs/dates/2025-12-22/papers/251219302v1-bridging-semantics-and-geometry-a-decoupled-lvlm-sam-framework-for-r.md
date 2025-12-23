---
layout: default
title: Bridging Semantics and Geometry: A Decoupled LVLM-SAM Framework for Reasoning Segmentation in Remote Sensing
---

# Bridging Semantics and Geometry: A Decoupled LVLM-SAM Framework for Reasoning Segmentation in Remote Sensing
**arXiv**：[2512.19302v1](https://arxiv.org/abs/2512.19302) · [PDF](https://arxiv.org/pdf/2512.19302.pdf)  
**作者**：Xu Zhang, Junyao Ge, Yang Zheng, Kaitai Guo, Jimin Liang  

**一句话要点**：提出解耦的LVLM-SAM框架Think2Seg-RS，通过结构化几何提示实现遥感推理分割。

**关键词**：遥感推理分割, 大型视觉语言模型, Segment Anything模型, 解耦框架, 强化学习, 几何提示

## 3 点简述
- 现有遥感推理分割框架耦合语言推理与像素预测，导致几何基础弱和泛化能力有限。
- Think2Seg-RS训练LVLM提示器控制冻结的SAM，使用掩码强化学习目标将语义推理转化为空间动作。
- 在EarthReason数据集上达到SOTA性能，零样本泛化至多个参考分割基准，揭示语义级与实例级基础差异。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) hold great promise for advancing remote sensing (RS) analysis, yet existing reasoning segmentation frameworks couple linguistic reasoning and pixel prediction through end-to-end supervised fine-tuning, leading to weak geometric grounding and limited generalization across tasks. To address this, we developed Think2Seg-RS, a decoupled framework that trains an LVLM prompter to control a frozen Segment Anything Model (SAM) via structured geometric prompts. Through a mask-only reinforcement learning objective, the LVLM learns to translate abstract semantic reasoning into spatially grounded actions, achieving state-of-the-art performance on the EarthReason dataset. Remarkably, the learned prompting policy generalizes zero-shot to multiple referring segmentation benchmarks, exposing a distinct divide between semantic-level and instance-level grounding. We further found that compact segmenters outperform larger ones under semantic-level supervision, and that negative prompts are ineffective in heterogeneous aerial backgrounds. Together, these findings establish semantic-level reasoning segmentation as a new paradigm for geospatial understanding, opening the way toward unified, interpretable LVLM-driven Earth observation. Our code and model are available at https://github.com/Ricardo-XZ/Think2Seg-RS.

