---
layout: default
title: DarkEQA: Benchmarking Vision-Language Models for Embodied Question Answering in Low-Light Indoor Environments
---

# DarkEQA: Benchmarking Vision-Language Models for Embodied Question Answering in Low-Light Indoor Environments
**arXiv**：[2512.24985v1](https://arxiv.org/abs/2512.24985) · [PDF](https://arxiv.org/pdf/2512.24985.pdf)  
**作者**：Yohan Park, Hyunwoo Ha, Wonjun Jo, Tae-Hyun Oh  

**一句话要点**：提出DarkEQA基准，评估视觉语言模型在低光室内环境下的具身问答能力。

**关键词**：具身问答, 低光视觉, 视觉语言模型, 基准测试, 图像增强, 感知评估

## 3 点简述
- 现有基准在理想光照下评估VLMs，忽略低光条件对具身代理稳健性的核心挑战。
- DarkEQA在RAW空间模拟物理光照下降和传感器噪声，提供高保真视觉退化以隔离感知瓶颈。
- 评估多种VLMs和LLIE模型，系统揭示其在低光条件下的局限性，促进稳健性分析。

## 摘要（原文）

> Vision Language Models (VLMs) are increasingly adopted as central reasoning modules for embodied agents. Existing benchmarks evaluate their capabilities under ideal, well-lit conditions, yet robust 24/7 operation demands performance under a wide range of visual degradations, including low-light conditions at night or in dark environments--a core necessity that has been largely overlooked. To address this underexplored challenge, we present DarkEQA, an open-source benchmark for evaluating EQA-relevant perceptual primitives under multi-level low-light conditions. DarkEQA isolates the perception bottleneck by evaluating question answering from egocentric observations under controlled degradations, enabling attributable robustness analysis. A key design feature of DarkEQA is its physical fidelity: visual degradations are modeled in linear RAW space, simulating physics-based illumination drop and sensor noise followed by an ISP-inspired rendering pipeline. We demonstrate the utility of DarkEQA by evaluating a wide range of state-of-the-art VLMs and Low-Light Image Enhancement (LLIE) models. Our analysis systematically reveals VLMs' limitations when operating under these challenging visual conditions. Our code and benchmark dataset will be released upon acceptance.

