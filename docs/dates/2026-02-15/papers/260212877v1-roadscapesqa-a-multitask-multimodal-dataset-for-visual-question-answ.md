---
layout: default
title: RoadscapesQA: A Multitask, Multimodal Dataset for Visual Question Answering on Indian Roads
---

# RoadscapesQA: A Multitask, Multimodal Dataset for Visual Question Answering on Indian Roads
**arXiv**：[2602.12877v1](https://arxiv.org/abs/2602.12877) · [PDF](https://arxiv.org/pdf/2602.12877.pdf)  
**作者**：Vijayasri Iyer, Maahin Rathinagiriswaran, Jyothikamalesh S  

**一句话要点**：提出RoadscapesQA数据集，用于印度道路场景的视觉问答，以支持自动驾驶研究。

**关键词**：视觉问答, 自动驾驶, 多模态数据集, 印度道路场景, 场景理解, 规则启发式

## 3 点简述
- 核心问题：自动驾驶需理解非结构化道路场景，但现有数据集在印度多样化环境中的覆盖不足。
- 方法要点：基于9,000张印度道路图像，通过规则启发式生成多任务问答对，涵盖对象定位、推理和场景理解。
- 实验或效果：提供数据集统计和基于视觉语言模型的初始基线，旨在推动非结构化环境下的视觉场景理解研究。

## 摘要（原文）

> Understanding road scenes is essential for autonomous driving, as it enables systems to interpret visual surroundings to aid in effective decision-making. We present Roadscapes, a multitask multimodal dataset consisting of upto 9,000 images captured in diverse Indian driving environments, accompanied by manually verified bounding boxes. To facilitate scalable scene understanding, we employ rule-based heuristics to infer various scene attributes, which are subsequently used to generate question-answer (QA) pairs for tasks such as object grounding, reasoning, and scene understanding. The dataset includes a variety of scenes from urban and rural India, encompassing highways, service roads, village paths, and congested city streets, captured in both daytime and nighttime settings. Roadscapes has been curated to advance research on visual scene understanding in unstructured environments. In this paper, we describe the data collection and annotation process, present key dataset statistics, and provide initial baselines for image QA tasks using vision-language models.

