---
layout: default
title: AIRHILT: A Human-in-the-Loop Testbed for Multimodal Conflict Detection in Aviation
---

# AIRHILT: A Human-in-the-Loop Testbed for Multimodal Conflict Detection in Aviation
**arXiv**：[2511.18718v1](https://arxiv.org/abs/2511.18718) · [PDF](https://arxiv.org/pdf/2511.18718.pdf)  
**作者**：Omar Garib, Jayaprakash D. Kambhampaty, Olivia J. Pinon Fischer, Dimitri N. Mavris  

**一句话要点**：提出AIRHILT测试平台，用于评估航空多模态冲突检测系统

**关键词**：多模态冲突检测, 人机交互测试平台, 航空安全仿真, 标准化接口, 开源环境

## 3 点简述
- 核心问题：航空中多模态冲突检测缺乏统一评估环境，涉及通信和视觉数据整合。
- 方法要点：基于Godot引擎构建模块化测试平台，支持人机交互和标准化接口集成。
- 实验或效果：初步测试显示平均预警时间约7.7秒，ASR和视觉延迟分别为5.9秒和0.4秒。

## 摘要（原文）

> We introduce AIRHILT (Aviation Integrated Reasoning, Human-in-the-Loop Testbed), a modular and lightweight simulation environment designed to evaluate multimodal pilot and air traffic control (ATC) assistance systems for aviation conflict detection. Built on the open-source Godot engine, AIRHILT synchronizes pilot and ATC radio communications, visual scene understanding from camera streams, and ADS-B surveillance data within a unified, scalable platform. The environment supports pilot- and controller-in-the-loop interactions, providing a comprehensive scenario suite covering both terminal area and en route operational conflicts, including communication errors and procedural mistakes. AIRHILT offers standardized JSON-based interfaces that enable researchers to easily integrate, swap, and evaluate automatic speech recognition (ASR), visual detection, decision-making, and text-to-speech (TTS) models. We demonstrate AIRHILT through a reference pipeline incorporating fine-tuned Whisper ASR, YOLO-based visual detection, ADS-B-based conflict logic, and GPT-OSS-20B structured reasoning, and present preliminary results from representative runway-overlap scenarios, where the assistant achieves an average time-to-first-warning of approximately 7.7 s, with average ASR and vision latencies of approximately 5.9 s and 0.4 s, respectively. The AIRHILT environment and scenario suite are openly available, supporting reproducible research on multimodal situational awareness and conflict detection in aviation; code and scenarios are available at https://github.com/ogarib3/airhilt.

