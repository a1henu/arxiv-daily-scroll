---
layout: default
title: Stable In-hand Manipulation for a Lightweight Four-motor Prosthetic Hand
---

# Stable In-hand Manipulation for a Lightweight Four-motor Prosthetic Hand
**arXiv**：[2601.07559v1](https://arxiv.org/abs/2601.07559) · [PDF](https://arxiv.org/pdf/2601.07559.pdf)  
**作者**：Yuki Kuroda, Tomoya Takahashi, Cristian C. Beltran-Hernandez, Kazutoshi Tanaka, Masashi Hamaya  

**一句话要点**：提出基于电机电流反馈的四电机假肢手稳定手内操纵方法，以解决重物旋转操作中的稳定性问题。

**关键词**：假肢手, 手内操纵, 电机电流反馈, 轻量化设计, 旋转操作, 稳定性控制

## 3 点简述
- 核心问题：轻量化假肢手在旋转操作中难以稳定处理重物，且控制器依赖预定义物体宽度。
- 方法要点：利用电机电流反馈估计物体宽度，协调食指位置以维持稳定抓持，结合优化单轴拇指设计。
- 实验或效果：在多种形状和重量的物体上实现高成功率，重物（如289克棱柱）成功率≥80%，并完成日常任务如盖瓶盖和调整笔姿。

## 摘要（原文）

> Electric prosthetic hands should be lightweight to decrease the burden on the user, shaped like human hands for cosmetic purposes, and designed with motors enclosed inside to protect them from damage and dirt. Additionally, in-hand manipulation is necessary to perform daily activities such as transitioning between different postures, particularly through rotational movements, such as reorienting a pen into a writing posture after picking it up from a desk. We previously developed PLEXUS hand (Precision-Lateral dEXteroUS manipulation hand), a lightweight (311 g) prosthetic hand driven by four motors. This prosthetic performed reorientation between precision and lateral grasps with various objects. However, its controller required predefined object widths and was limited to handling lightweight objects (of weight up to 34 g). This study addresses these limitations by employing motor current feedback. Combined with the hand's previously optimized single-axis thumb, this approach achieves more stable manipulation by estimating the object's width and adjusting the index finger position to maintain stable object holding during the reorientation. Experimental validation using primitive objects of various widths (5-30 mm) and shapes (cylinders and prisms) resulted in a 100% success rate with lightweight objects and maintained a high success rate (>=80) even with heavy aluminum prisms (of weight up to 289 g). By contrast, the performance without index finger coordination dropped to just 40% on the heaviest 289 g prism. The hand also successfully executed several daily tasks, including closing bottle caps and orienting a pen for writing.

