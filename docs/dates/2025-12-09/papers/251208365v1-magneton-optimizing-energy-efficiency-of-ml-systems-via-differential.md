---
layout: default
title: Magneton: Optimizing Energy Efficiency of ML Systems via Differential Energy Debugging
---

# Magneton: Optimizing Energy Efficiency of ML Systems via Differential Energy Debugging
**arXiv**：[2512.08365v1](https://arxiv.org/abs/2512.08365) · [PDF](https://arxiv.org/pdf/2512.08365.pdf)  
**作者**：Yi Pan, Wenbo Qian, Dedong Xie, Ruiyan Hu, Yigong Hu, Baris Kasikci  

**一句话要点**：提出Magneton通过差分能量调试优化机器学习系统的能源效率

**关键词**：能源效率优化, 差分能量调试, 机器学习系统, 能源分析工具, 软件能源浪费

## 3 点简述
- 核心问题：机器学习系统软件设计不良导致能源浪费，现有工具难以检测。
- 方法要点：基于相似系统能源消耗差异，设计差分能量调试方法，在算子级别定位高能耗代码。
- 实验或效果：应用于9个流行系统，诊断16个已知和8个未知能源低效案例，7个获开发者确认。

## 摘要（原文）

> The training and deployment of machine learning (ML) models have become extremely energy-intensive. While existing optimization efforts focus primarily on hardware energy efficiency, a significant but overlooked source of inefficiency is software energy waste caused by poor software design. This often includes redundant or poorly designed operations that consume more energy without improving performance. These inefficiencies arise in widely used ML frameworks and applications, yet developers often lack the visibility and tools to detect and diagnose them.
>   We propose differential energy debugging, a novel approach that leverages the observation that competing ML systems often implement similar functionality with vastly different energy consumption. Building on this insight, we design and implement Magneton, an energy profiler that compares energy consumption between similar ML systems at the operator level and automatically pinpoints code regions and configuration choices responsible for excessive energy use. Applied to 9 popular ML systems spanning LLM inference, general ML frameworks, and image generation, Magneton detects and diagnoses 16 known cases of software energy inefficiency and further discovers 8 previously unknown cases, 7 of which have been confirmed by developers.

