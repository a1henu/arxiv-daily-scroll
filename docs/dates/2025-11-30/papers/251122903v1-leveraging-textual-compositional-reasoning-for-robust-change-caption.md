---
layout: default
title: Leveraging Textual Compositional Reasoning for Robust Change Captioning
---

# Leveraging Textual Compositional Reasoning for Robust Change Captioning
**arXiv**：[2511.22903v1](https://arxiv.org/abs/2511.22903) · [PDF](https://arxiv.org/pdf/2511.22903.pdf)  
**作者**：Kyu Ri Park, Jiyoung Park, Seong Tae Kim, Hong Joo Lee, Jung Uk Kim  

**一句话要点**：提出CORTEX框架，通过整合文本组合推理增强变化描述任务

**关键词**：变化描述, 组合推理, 视觉语言模型, 图像-文本对齐, 变化检测

## 3 点简述
- 现有方法依赖视觉特征，难以捕捉细微变化，缺乏结构化信息表示
- CORTEX结合图像级变化检测、推理感知文本提取和图像-文本双重对齐模块
- 利用视觉语言模型提取文本知识，提升变化理解的鲁棒性和准确性

## 摘要（原文）

> Change captioning aims to describe changes between a pair of images. However, existing works rely on visual features alone, which often fail to capture subtle but meaningful changes because they lack the ability to represent explicitly structured information such as object relationships and compositional semantics. To alleviate this, we present CORTEX (COmpositional Reasoning-aware TEXt-guided), a novel framework that integrates complementary textual cues to enhance change understanding. In addition to capturing cues from pixel-level differences, CORTEX utilizes scene-level textual knowledge provided by Vision Language Models (VLMs) to extract richer image text signals that reveal underlying compositional reasoning. CORTEX consists of three key modules: (i) an Image-level Change Detector that identifies low-level visual differences between paired images, (ii) a Reasoning-aware Text Extraction (RTE) module that use VLMs to generate compositional reasoning descriptions implicit in visual features, and (iii) an Image-Text Dual Alignment (ITDA) module that aligns visual and textual features for fine-grained relational reasoning. This enables CORTEX to reason over visual and textual features and capture changes that are otherwise ambiguous in visual features alone.

