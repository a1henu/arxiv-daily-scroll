---
layout: default
title: PISHYAR: A Socially Intelligent Smart Cane for Indoor Social Navigation and Multimodal Human-Robot Interaction for Visually Impaired People
---

# PISHYAR: A Socially Intelligent Smart Cane for Indoor Social Navigation and Multimodal Human-Robot Interaction for Visually Impaired People
**arXiv**：[2602.12597v1](https://arxiv.org/abs/2602.12597) · [PDF](https://arxiv.org/pdf/2602.12597.pdf)  
**作者**：Mahdi Haghighat Joo, Maryam Karimi Jafari, Alireza Taheri  

**一句话要点**：提出PISHYAR智能手杖，结合社交导航与多模态交互，辅助视障人士室内移动与互动。

**关键词**：社交导航, 多模态交互, 智能手杖, 视障辅助, 室内移动

## 3 点简述
- 核心问题：视障人士在室内环境中面临社交导航和交互支持不足的挑战。
- 方法要点：集成RGB-D感知、YOLOv8检测、COMPOSER活动识别、D* Lite路径规划和多模态LLM-VLM交互框架。
- 实验或效果：系统准确率约80%，用户研究显示高接受度和积极感知。

## 摘要（原文）

> This paper presents PISHYAR, a socially intelligent smart cane designed by our group to combine socially aware navigation with multimodal human-AI interaction to support both physical mobility and interactive assistance. The system consists of two components: (1) a social navigation framework implemented on a Raspberry Pi 5 that integrates real-time RGB-D perception using an OAK-D Lite camera, YOLOv8-based object detection, COMPOSER-based collective activity recognition, D* Lite dynamic path planning, and haptic feedback via vibration motors for tasks such as locating a vacant seat; and (2) an agentic multimodal LLM-VLM interaction framework that integrates speech recognition, vision language models, large language models, and text-to-speech, with dynamic routing between voice-only and vision-only modes to enable natural voice-based communication, scene description, and object localization from visual input. The system is evaluated through a combination of simulation-based tests, real-world field experiments, and user-centered studies. Results from simulated and real indoor environments demonstrate reliable obstacle avoidance and socially compliant navigation, achieving an overall system accuracy of approximately 80% under different social conditions. Group activity recognition further shows robust performance across diverse crowd scenarios. In addition, a preliminary exploratory user study with eight visually impaired and low-vision participants evaluates the agentic interaction framework through structured tasks and a UTAUT-based questionnaire reveals high acceptance and positive perceptions of usability, trust, and perceived sociability during our experiments. The results highlight the potential of PISHYAR as a multimodal assistive mobility aid that extends beyond navigation to provide socially interactive support for such users.

