---
layout: default
title: A Large Language Model for Disaster Structural Reconnaissance Summarization
---

# A Large Language Model for Disaster Structural Reconnaissance Summarization
**arXiv**：[2602.11588v1](https://arxiv.org/abs/2602.11588) · [PDF](https://arxiv.org/pdf/2602.11588.pdf)  
**作者**：Yuqing Gao, Guanren Zhou, Khalid M. Mosalam  

**一句话要点**：提出基于大语言模型的灾害结构侦察摘要框架，以改进视觉结构健康监测的报告生成。

**关键词**：大语言模型, 视觉结构健康监测, 灾害侦察, 摘要生成, 深度卷积网络

## 3 点简述
- 核心问题：现有视觉结构健康监测方法仅输出离散损伤标签和坐标，需人工整合分析。
- 方法要点：设计标准化侦察流程，整合文本元数据和图像数据，通过深度卷积网络提取关键属性，并输入大语言模型生成摘要报告。
- 实验或效果：结果显示该框架在快速灾后侦察中具有潜力，可提升建筑环境韧性。

## 摘要（原文）

> Artificial Intelligence (AI)-aided vision-based Structural Health Monitoring (SHM) has emerged as an effective approach for monitoring and assessing structural condition by analyzing image and video data. By integrating Computer Vision (CV) and Deep Learning (DL), vision-based SHM can automatically identify and localize visual patterns associated with structural damage. However, previous works typically generate only discrete outputs, such as damage class labels and damage region coordinates, requiring engineers to further reorganize and analyze these results for evaluation and decision-making. In late 2022, Large Language Models (LLMs) became popular across multiple fields, providing new insights into AI-aided vision-based SHM. In this study, a novel LLM-based Disaster Reconnaissance Summarization (LLM-DRS) framework is proposed. It introduces a standard reconnaissance plan in which the collection of vision data and corresponding metadata follows a well-designed on-site investigation process. Text-based metadata and image-based vision data are then processed and integrated into a unified format, where well-trained Deep Convolutional Neural Networks extract key attributes, including damage state, material type, and damage level. Finally, all data are fed into an LLM with carefully designed prompts, enabling the LLM-DRS to generate summary reports for individual structures or affected regions based on aggregated attributes and metadata. Results show that integrating LLMs into vision-based SHM, particularly for rapid post-disaster reconnaissance, demonstrates promising potential for improving resilience of the built environment through effective reconnaissance.

